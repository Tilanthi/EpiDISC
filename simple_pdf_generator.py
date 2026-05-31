#!/usr/bin/env python3
"""
Simple PDF generator for EPIDISC manual
"""

import sys
import os
from pathlib import Path

# Test imports
print("Testing imports...")
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
    from reportlab.platypus.flowables import HRFlowable
    from reportlab.lib import colors
    print("✓ reportlab imported successfully")
except ImportError as e:
    print(f"✗ reportlab import failed: {e}")
    sys.exit(1)

try:
    from PIL import Image as PILImage, ImageDraw, ImageFont
    print("✓ PIL imported successfully")
except ImportError as e:
    print(f"✗ PIL import failed: {e}")
    sys.exit(1)

try:
    import markdown
    print("✓ markdown imported successfully")
except ImportError as e:
    print(f"⚠ markdown import failed: {e} (not required, continuing anyway)")

print("\nAll imports successful!")

# Now let's try to generate a simple PDF to test
print("\nAttempting to generate test PDF...")

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

    doc = SimpleDocTemplate("test_output.pdf", pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    story.append(Paragraph("EPIDISC Test PDF", styles['Heading1']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("This is a test to verify PDF generation works.", styles['BodyText']))

    doc.build(story)
    print("✓ Test PDF generated successfully: test_output.pdf")
except Exception as e:
    print(f"✗ PDF generation failed: {e}")
    sys.exit(1)

print("\n✅ PDF generation is working!")
