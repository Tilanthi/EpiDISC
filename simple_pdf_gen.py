#!/usr/bin/env python3
"""
Simple EPIDISC Manual PDF Generator
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
import re
import os

def parse_markdown_to_sections(md_file):
    """Parse markdown into sections"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = []
    current_section = None
    current_content = []

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for main heading
        if line.startswith('# ') and not line.startswith('## '):
            if current_section:
                sections.append((current_section, '\n'.join(current_content)))
            current_section = line.lstrip('#').strip()
            current_content = []
        elif line.startswith('## '):
            if current_section:
                sections.append((current_section, '\n'.join(current_content)))
            current_section = line.lstrip('#').strip()
            current_content = []
        else:
            current_content.append(line)
        i += 1

    # Add last section
    if current_section:
        sections.append((current_section, '\n'.join(current_content)))

    return sections

def create_simple_pdf():
    """Create PDF from markdown"""
    md_file = 'EPIDISC_USER_MANUAL_COMPLETE.md'
    pdf_file = 'EPIDISC_User_Manual.pdf'

    print("📄 Creating EPIDISC User Manual PDF...")

    # Parse markdown
    sections = parse_markdown_to_sections(md_file)

    # Create PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                                rightMargin=0.75*inch, leftMargin=0.75*inch,
                                topMargin=0.75*inch, bottomMargin=0.75*inch)

    # Get styles
    styles = getSampleStyleSheet()

    # Add custom styles
    styles.add(ParagraphStyle(
        name='Heading1',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        spaceBefore=20,
        alignment=TA_CENTER
    ))

    styles.add(ParagraphStyle(
        name='Heading2',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#764ba2'),
        spaceAfter=12,
        spaceBefore=10
    ))

    styles.add(ParagraphStyle(
        name='BodyText',
        parent=styles['BodyText'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY
    ))

    styles.add(ParagraphStyle(
        name='Code',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=9,
        textColor=colors.grey,
        leftIndent=20,
        backColor=colors.lightgrey,
        spaceAfter=10
    ))

    # Build story
    story = []

    # Title page
    story.append(Spacer(1.5*inch))
    story.append(Paragraph("EPIDISC User Manual and Complete Guide", styles['Heading1']))
    story.append(Spacer(0.5*inch))
    story.append(Paragraph("World-Class Medical Consultation and Research System", styles['Heading2']))
    story.append(Spacer(0.3*inch))
    story.append(Paragraph("Version 2.0.0 • Publication Date: May 31, 2026", styles['Normal']))
    story.append(PageBreak())

    # Process sections
    for title, content in sections:
        if title.strip():
            # Add heading
            if title.startswith('1. '):
                heading = title[3:].strip()
                story.append(Paragraph(heading, styles['Heading1']))
            elif title.startswith('2. '):
                heading = title[3:].strip()
                story.append(Paragraph(heading, styles['Heading2']))
            else:
                story.append(Paragraph(title, styles['Heading2']))
            story.append(Spacer(0.2*inch))

        # Process content (simplified)
        paragraphs = re.split(r'\n\n+', content)
        for para in paragraphs:
            if para.strip():
                # Check for code blocks
                if '```' in para:
                    # Skip complex formatting for now
                    continue

                # Convert markdown bold
                para = para.replace('**', '')

                # Clean up
                para = para.replace('*>', '').replace(' <', '')
                para = para.replace('> ', '> ')

                if len(para) > 10:  # Only add non-empty paragraphs
                    story.append(Paragraph(para, styles['BodyText']))
                    story.append(Spacer(0.1*inch))

        # Page break between major sections
        if title.startswith(('1. ', '2. ', '3. ', '4. ', '5. ')):
            story.append(PageBreak())

    # Add final page
    story.append(PageBreak())
    story.append(Paragraph("End of EPIDISC User Manual", styles['Heading1']))
    story.append(Spacer(0.3*inch))
    story.append(Paragraph("© 2026 EPIDISC. All rights reserved.", styles['Normal']))

    # Build PDF
    try:
        doc.build(story)
        print(f"✅ PDF created: {pdf_file}")
        print(f"📊 Size: {os.path.getsize(pdf_file) / 1024:.1f} KB")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = create_simple_pdf()
    if success:
        print("✅ EPIDISC User Manual PDF generated successfully!")
    else:
        print("💡 Alternative: Open EPIDISC_User_Manual.html in browser")
