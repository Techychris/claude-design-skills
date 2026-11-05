import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_kit import Canvas

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "examples-output")
os.makedirs(OUT_DIR, exist_ok=True)

c = Canvas(9.5, 6.0, margin=0.35)

# ---- Business layer ----
c.archimate_element(1.3, 5.3, 1.7, 0.6, "Customer", layer="business", kind="active")
c.archimate_element(4.0, 5.3, 1.8, 0.6, "Place Order", layer="business", kind="behavior")
c.archimate_element(4.0, 4.2, 1.7, 0.55, "Order Service", layer="business", kind="service")

# ---- Application layer ----
c.archimate_element(4.0, 3.1, 1.7, 0.55, "Order API", layer="application", kind="service")
c.archimate_element(4.0, 2.0, 1.8, 0.6, "Order System", layer="application", kind="component")
c.archimate_element(7.2, 2.0, 1.7, 0.6, "Order Data", layer="application", kind="object")

# ---- Technology layer ----
c.archimate_element(4.0, 0.9, 1.7, 0.55, "Hosting", layer="technology", kind="service")
c.archimate_element(7.2, 0.9, 1.7, 0.6, "App Server", layer="technology", kind="node")

# ---- Relationships (per ArchiMate Cookbook sec. 4 semantics) ----
# Customer is assigned to perform Place Order
c.archimate_relationship((1.3, 5.0), (3.1, 5.3), kind="assignment")
# Order Service serves Place Order (the process)
c.archimate_relationship((4.0, 4.48), (4.0, 5.0), kind="serving")
# Order API (application service) serves Order Service (business service)
c.archimate_relationship((4.0, 3.38), (4.0, 3.925), kind="serving")
# Order System realizes Order API
c.archimate_relationship((4.0, 2.3), (4.0, 2.825), kind="realization")
# Order System accesses Order Data
c.archimate_relationship((4.9, 2.0), (6.35, 2.0), kind="access")
# Hosting (technology service) serves Order System
c.archimate_relationship((4.0, 1.18), (4.0, 1.7), kind="serving")
# App Server realizes Hosting
c.archimate_relationship((6.35, 0.9), (4.85, 0.9), kind="realization")

c.archimate_legend(0.4, -0.05, layers=("business", "application", "technology"))

c.save(os.path.join(OUT_DIR, "archimate-layered-view.png"))
print("saved")
