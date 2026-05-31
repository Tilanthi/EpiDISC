#!/usr/bin/env python3
"""
Simplified PDF generator for EPIDISC manual
"""

import sys
import os
import re

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
    from reportlab.platypus.flowables import HRFlowable
    from reportlab.lib import colors
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("Error: reportlab not available")
    sys.exit(1)

try:
    from PIL import Image as PILImage, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("Error: PIL not available")
    sys.exit(1)


def clean_markdown_text(text):
    """Convert markdown to simple HTML for reportlab"""
    # Remove HTML special characters
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')

    # Handle bold text **text**
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)

    # Handle italic text *text*
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)

    # Handle code `text`
    text = re.sub(r'`([^`]+)`', r'<font face="Courier">\1</font>', text)

    return text


def create_pdf(md_file, pdf_file, diagram_path):
    """Create PDF from markdown file"""

    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)

    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#3498db'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica',
    )

    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold',
    )

    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#e74c3c'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold',
    )

    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=HexColor('#3498db'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold',
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=HexColor('#2c3e50'),
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
    )

    # Add title page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("EPIDISC", title_style))
    story.append(Paragraph("Medical Discovery and Intelligence System for Consultation", subtitle_style))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("Version 1.0.0", ParagraphStyle('Version', parent=body_style, alignment=TA_CENTER)))
    story.append(Paragraph("May 2026", ParagraphStyle('Date', parent=body_style, alignment=TA_CENTER)))
    story.append(Paragraph("Author: Tilanthi", ParagraphStyle('Author', parent=body_style, alignment=TA_CENTER)))
    story.append(PageBreak())

    # Process markdown lines
    in_code_block = False
    in_table = False
    skip_next = False

    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue

        line = line.rstrip()

        # Skip empty lines
        if not line:
            story.append(Spacer(1, 0.1*inch))
            continue

        # Handle code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            story.append(Paragraph(f"<font face='Courier'>{line}</font>", body_style))
            continue

        # Handle horizontal rules
        if line.startswith('---'):
            story.append(HRFlowable(width='100%', thickness=1, color=HexColor('#bdc3c7')))
            story.append(Spacer(1, 0.2*inch))
            continue

        # Handle headings
        if line.startswith('# '):
            text = clean_markdown_text(line[2:])
            story.append(Paragraph(text, heading1_style))
        elif line.startswith('## '):
            text = clean_markdown_text(line[3:])
            story.append(Paragraph(text, heading2_style))
        elif line.startswith('### '):
            text = clean_markdown_text(line[4:])
            story.append(Paragraph(text, heading3_style))
        elif line.startswith('#### '):
            text = clean_markdown_text(line[5:])
            story.append(Paragraph(text, ParagraphStyle('H4', parent=heading3_style, fontSize=10)))

        # Handle architecture diagram marker
        elif '[[ARCHITECTURE_DIAGRAM]]' in line:
            if os.path.exists(diagram_path):
                img = Image(diagram_path, width=5.5*inch, height=7*inch, hAlign='CENTER')
                story.append(img)
                story.append(Spacer(1, 0.3*inch))

        # Handle lists
        elif line.startswith('- ') or line.startswith('* '):
            text = clean_markdown_text(f"• {line[2:]}")
            story.append(Paragraph(text, body_style))
        elif re.match(r'^\d+\. ', line):
            text = clean_markdown_text(re.sub(r'^\d+\. ', '', line))
            story.append(Paragraph(text, body_style))

        # Handle table rows
        elif line.startswith('|') and line.endswith('|'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if parts and all(p or i == len(parts)-1 for i, p in enumerate(parts)):
                # Simple table handling
                table_text = ' | '.join(parts)
                text = clean_markdown_text(table_text)
                story.append(Paragraph(text, body_style))

        # Handle checkboxes
        elif line.startswith('- ') and '[' in line:
            text = clean_markdown_text(line[2:])
            story.append(Paragraph(text, body_style))

        # Handle regular text
        else:
            text = clean_markdown_text(line)
            story.append(Paragraph(text, body_style))

    # Build PDF
    try:
        doc.build(story)
        print(f"✓ PDF generated successfully: {pdf_file}")
        return True
    except Exception as e:
        print(f"✗ Error building PDF: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function"""
    print("EPIDISC PDF Generator")
    print("=" * 50)

    md_file = "User_manual/EPIDISC_User_Manual_Comprehensive.md"
    pdf_file = "User_manual/EPIDISC_User_Manual_Comprehensive.pdf"
    diagram_path = "User_manual/epidisc_architecture_diagram.png"

    if not os.path.exists(md_file):
        print(f"✗ Error: {md_file} not found")
        return False

    # Ensure User_manual directory exists
    os.makedirs("User_manual", exist_ok=True)

    print(f"\nGenerating PDF from {md_file}...")
    success = create_pdf(md_file, pdf_file, diagram_path)

    if success:
        print(f"\n✅ PDF generated successfully!")
        print(f"📄 Output: {pdf_file}")
        if os.path.exists(diagram_path):
            print(f"📊 Architecture diagram: {diagram_path}")
        return True
    else:
        print("\n❌ Failed to generate PDF")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
