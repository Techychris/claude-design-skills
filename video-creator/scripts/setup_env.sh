#!/usr/bin/env bash
# Setup for video-creator skill. Idempotent — safe to run multiple times.
#
# Two environments:
#   - claude.ai sandbox (detected by /mnt/user-data): system pip install plus the
#     certifi CA merge that edge-tts needs behind the sandbox's TLS proxy.
#   - anyone's own computer: installs into ./.venv and changes nothing system-wide.
#     It never edits certifi and never runs apt-get. Activate with:
#       source .venv/bin/activate
set -e

PKGS="edge-tts pillow praat-parselmouth syllables"

if [ -d /mnt/user-data ]; then
  echo "[1/3] Sandbox detected: installing Python deps..."
  pip install --quiet --break-system-packages $PKGS 2>/dev/null || pip install --quiet $PKGS

  echo "[2/3] Trusting system CAs in certifi (required behind the sandbox's TLS proxy)..."
  # edge-tts hardcodes ssl.create_default_context(cafile=certifi.where()).
  # The sandbox egress proxy re-signs TLS with its own CA, which lives in the
  # system store but NOT in certifi's bundle. Append it once.
  CERTIFI_BUNDLE=$(python3 -c "import certifi; print(certifi.where())")
  SYSTEM_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
  if [ -f "$SYSTEM_BUNDLE" ] && ! grep -q "VIDEO_CREATOR_CA_MERGED" "$CERTIFI_BUNDLE" 2>/dev/null; then
    update-ca-certificates >/dev/null 2>&1 || true
    { echo ""; echo "# VIDEO_CREATOR_CA_MERGED"; cat "$SYSTEM_BUNDLE"; } >> "$CERTIFI_BUNDLE" 2>/dev/null \
      || echo "  (certifi bundle not writable — set SSL_CERT_FILE instead)"
  fi
else
  echo "[1/3] Local machine: installing Python deps into ./.venv ..."
  if [ ! -d .venv ]; then
    python3 -m venv .venv || { echo "ERROR: python3 -m venv failed (on Debian/Ubuntu: sudo apt install python3-venv)"; exit 1; }
  fi
  ./.venv/bin/pip install --quiet --upgrade pip
  ./.venv/bin/pip install --quiet $PKGS
  echo "  Use ./.venv/bin/python to run the scripts, or: source .venv/bin/activate"

  echo "[2/3] Skipping the certifi change (only needed in the sandbox)."
  echo "  If edge-tts fails with CERTIFICATE_VERIFY_FAILED behind a corporate proxy, run with"
  echo "  SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt set instead of editing certifi."
fi

echo "[3/3] Checking ffmpeg..."
if ! command -v ffmpeg >/dev/null; then
  echo "WARNING: ffmpeg not found. Ask the person to install it (e.g. sudo apt install ffmpeg, brew install ffmpeg, or winget install ffmpeg)."
else
  ffmpeg -version | head -1
fi

echo "Setup complete."
