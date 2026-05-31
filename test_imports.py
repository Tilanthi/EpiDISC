#!/usr/bin/env python3
import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    from reportlab.lib.pagesizes import A4
    print("✓ reportlab imported successfully")
except ImportError as e:
    print(f"✗ reportlab import failed: {e}")

try:
    from PIL import Image
    print("✓ PIL imported successfully")
except ImportError as e:
    print(f"✗ PIL import failed: {e}")

print("Test complete")
