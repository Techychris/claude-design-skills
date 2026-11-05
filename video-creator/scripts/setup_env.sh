#!/usr/bin/env bash
# Setup for video-creator skill. Idempotent — safe to run multiple times.
set -e

echo "[1/3] Installing Python deps..."
pip install --quiet --break-system-packages edge-tts pillow praat-parselmouth syllables 2>/dev/null || pip install --quiet edge-tts pillow praat-parselmouth syllables

echo "[2/3] Trusting system CAs in certifi (required behind TLS-intercepting proxies)..."
# edge-tts hardcodes ssl.create_default_context(cafile=certifi.where()).
# In sandboxed environments the egress proxy re-signs TLS with its own CA,
# which lives in the system store but NOT in certifi's bundle. Append it once.
CERTIFI_BUNDLE=$(python3 -c "import certifi; print(certifi.where())")
SYSTEM_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
if [ -f "$SYSTEM_BUNDLE" ] && ! grep -q "VIDEO_CREATOR_CA_MERGED" "$CERTIFI_BUNDLE" 2>/dev/null; then
  update-ca-certificates >/dev/null 2>&1 || true
  { echo ""; echo "# VIDEO_CREATOR_CA_MERGED"; cat "$SYSTEM_BUNDLE"; } >> "$CERTIFI_BUNDLE" 2>/dev/null \
    || echo "  (certifi bundle not writable — set SSL_CERT_FILE instead)"
fi

echo "[3/3] Checking ffmpeg..."
if ! command -v ffmpeg >/dev/null; then
  echo "WARNING: ffmpeg not found. Install with: apt-get install -y ffmpeg"
else
  ffmpeg -version | head -1
fi

echo "Setup complete."
