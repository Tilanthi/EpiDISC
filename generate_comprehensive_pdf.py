#!/usr/bin/env python3
"""
Generate comprehensive EPIDISC PDF User Manual with architecture diagram
"""

import os
import sys
from pathlib import Path

# Try to import required libraries
try:
    from reportlab.lib.pagesizes import A4, letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
    from reportlab.platypus.flowables import HRFlowable, KeepTogether
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib import colors
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("Warning: reportlab not available")

# Markdown is optional - we parse manually
try:
    import markdown
except ImportError:
    print("Note: markdown module not available (optional)")
    pass

try:
    from PIL import Image as PILImage, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("Warning: PIL not available")

def create_architecture_diagram(output_path="epidisc_architecture_diagram.png"):
    """Create a high-quality architecture diagram"""
    if not PIL_AVAILABLE:
        print("PIL not available, skipping diagram creation")
        return None

    # Create a large image for the architecture diagram
    width = 1200
    height = 1600
    img = PILImage.new('RGB', (width, height), color='#f8f9fa')
    draw = ImageDraw.Draw(img)

    # Color scheme
    colors = {
        'header': '#2c3e50',
        'user_interface': '#3498db',
        'medical': '#e74c3c',
        'biology': '#27ae60',
        'capabilities': '#9b59b6',
        'memory': '#f39c12',
        'text': '#2c3e50',
        'white': '#ffffff',
        'border': '#34495e',
        'light_blue': '#ecf0f1',
    }

    # Title
    title_y = 30
    draw.rectangle([(50, title_y), (width-50, title_y+80)], fill=colors['header'], outline=colors['border'])
    try:
        # Try to use a better font
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except:
        # Fallback to default
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    title = "EPIDISC System Architecture v1.0.0"
    draw.text((width//2, title_y+40), title, fill=colors['white'], font=font_large, anchor="mm")

    # Layer 1: User Interface
    layer1_y = title_y + 120
    draw.rectangle([(50, layer1_y), (width-50, layer1_y+100)],
                   fill=colors['user_interface'], outline=colors['border'], width=3)
    draw.text((width//2, layer1_y+50), "USER INTERFACE LAYER",
              fill=colors['white'], font=font_medium, anchor="mm")

    # Layer 1 components
    comp_y = layer1_y + 120
    components = [
        ("Natural Language Queries", 150),
        ("Dashboard (Port 8790)", 400),
        ("Multi-Specialty Consultation", 650),
        ("Patient Records", 900),
    ]

    for comp_text, comp_x in components:
        draw.rectangle([(comp_x, comp_y), (comp_x+200, comp_y+60)],
                       fill=colors['light_blue'], outline=colors['border'])
        draw.text((comp_x+100, comp_y+30), comp_text,
                  fill=colors['text'], font=font_small, anchor="mm")

    # Arrow down
    arrow_y = comp_y + 90
    draw.polygon([(width//2, arrow_y), (width//2-30, arrow_y-30), (width//2+30, arrow_y-30)],
                 fill=colors['border'])

    # Layer 2: Medical Specialty Layer
    layer2_y = arrow_y + 50
    draw.rectangle([(50, layer2_y), (width-50, layer2_y+100)],
                   fill=colors['medical'], outline=colors['border'], width=3)
    draw.text((width//2, layer2_y+50), "MEDICAL SPECIALTY LAYER",
              fill=colors['white'], font=font_medium, anchor="mm")

    # Layer 2 components
    comp_y = layer2_y + 120
    specialties = [
        ("Cardiology", 100, "#e67e22"),
        ("Epilepsy v3.0.0", 280, "#c0392b"),
        ("General Practice", 480, "#e67e22"),
        ("Orthopedics", 680, "#e67e22"),
    ]
    specialties_row2 = [
        ("Pharmacology", 180, "#e67e22"),
        ("Neurology", 400, "#e67e22"),
        ("Emergency Med", 620, "#e67e22"),
    ]

    for spec_text, spec_x, spec_color in specialties:
        draw.rectangle([(spec_x, comp_y), (spec_x+160, comp_y+60)],
                       fill=spec_color, outline=colors['border'])
        draw.text((spec_x+80, comp_y+30), spec_text,
                  fill=colors['white'], font=font_small, anchor="mm")

    comp_y += 80
    for spec_text, spec_x, spec_color in specialties_row2:
        draw.rectangle([(spec_x, comp_y), (spec_x+160, comp_y+60)],
                       fill=spec_color, outline=colors['border'])
        draw.text((spec_x+80, comp_y+30), spec_text,
                  fill=colors['white'], font=font_small, anchor="mm")

    # Arrow down
    arrow_y = comp_y + 90
    draw.polygon([(width//2, arrow_y), (width//2-30, arrow_y-30), (width//2+30, arrow_y-30)],
                 fill=colors['border'])

    # Layer 3: Biological Knowledge Layer
    layer3_y = arrow_y + 50
    draw.rectangle([(50, layer3_y), (width-50, layer3_y+100)],
                   fill=colors['biology'], outline=colors['border'], width=3)
    draw.text((width//2, layer3_y+50), "BIOLOGICAL KNOWLEDGE LAYER (Preserved)",
              fill=colors['white'], font=font_medium, anchor="mm")

    # Layer 3 components
    comp_y = layer3_y + 120
    bio_domains = [
        ("Molecular Biology", 80, "#27ae60"),
        ("Biochemistry", 260, "#27ae60"),
        ("Genetics", 420, "#27ae60"),
        ("Cell Biology", 560, "#27ae60"),
        ("Biophysics", 720, "#27ae60"),
        ("Bioinformatics", 880, "#27ae60"),
    ]
    bio_domains_row2 = [
        ("Genomics", 180, "#229954"),
        ("Proteomics", 340, "#229954"),
        ("Systems Biology", 520, "#229954"),
        ("Comp. Biology", 720, "#229954"),
    ]

    for bio_text, bio_x, bio_color in bio_domains:
        draw.rectangle([(bio_x, comp_y), (bio_x+140, comp_y+50)],
                       fill=bio_color, outline=colors['border'])
        draw.text((bio_x+70, comp_y+25), bio_text,
                  fill=colors['white'], font=font_small, anchor="mm")

    comp_y += 70
    for bio_text, bio_x, bio_color in bio_domains_row2:
        draw.rectangle([(bio_x, comp_y), (bio_x+140, comp_y+50)],
                       fill=bio_color, outline=colors['border'])
        draw.text((bio_x+70, comp_y+25), bio_text,
                  fill=colors['white'], font=font_small, anchor="mm")

    # Arrow down
    arrow_y = comp_y + 80
    draw.polygon([(width//2, arrow_y), (width//2-30, arrow_y-30), (width//2+30, arrow_y-30)],
                 fill=colors['border'])

    # Layer 4: Advanced Capabilities Layer
    layer4_y = arrow_y + 50
    draw.rectangle([(50, layer4_y), (width-50, layer4_y+100)],
                   fill=colors['capabilities'], outline=colors['border'], width=3)
    draw.text((width//2, layer4_y+50), "ADVANCED CAPABILITIES LAYER",
              fill=colors['white'], font=font_medium, anchor="mm")

    # Layer 4 components
    comp_y = layer4_y + 120
    capabilities = [
        ("Causal Reasoning", 100),
        ("Meta-Learning", 280),
        ("Swarm Intelligence", 480),
        ("Counterfactual Analysis", 700),
    ]
    capabilities_row2 = [
        ("Innovative Research Synthesis", 150),
        ("Evidence Integration", 450),
        ("Meta-Context Engine", 750),
    ]

    for cap_text, cap_x in capabilities:
        draw.rectangle([(cap_x, comp_y), (cap_x+180, comp_y+50)],
                       fill=colors['light_blue'], outline=colors['border'])
        draw.text((cap_x+90, comp_y+25), cap_text,
                  fill=colors['text'], font=font_small, anchor="mm")

    comp_y += 70
    for cap_text, cap_x in capabilities_row2:
        draw.rectangle([(cap_x, comp_y), (cap_x+180, comp_y+50)],
                       fill=colors['light_blue'], outline=colors['border'])
        draw.text((cap_x+90, comp_y+25), cap_text,
                  fill=colors['text'], font=font_small, anchor="mm")

    # Arrow down
    arrow_y = comp_y + 80
    draw.polygon([(width//2, arrow_y), (width//2-30, arrow_y-30), (width//2+30, arrow_y-30)],
                 fill=colors['border'])

    # Layer 5: Memory & Privacy Layer
    layer5_y = arrow_y + 50
    draw.rectangle([(50, layer5_y), (width-50, layer5_y+100)],
                   fill=colors['memory'], outline=colors['border'], width=3)
    draw.text((width//2, layer5_y+50), "MEMORY & PRIVACY LAYER",
              fill=colors['white'], font=font_medium, anchor="mm")

    # Layer 5 components
    comp_y = layer5_y + 120
    privacy_features = [
        ("Persistent Memory", 150, "#d68910"),
        ("Anti-Hallucination", 350, "#d68910"),
        ("Local Storage", 550, "#d68910"),
        ("HIPAA/GDPR Compliant", 750, "#d68910"),
    ]

    for feat_text, feat_x, feat_color in privacy_features:
        draw.rectangle([(feat_x, comp_y), (feat_x+180, comp_y+60)],
                       fill=feat_color, outline=colors['border'])
        draw.text((feat_x+90, comp_y+30), feat_text,
                  fill=colors['white'], font=font_small, anchor="mm")

    # Footer
    footer_y = height - 80
    draw.rectangle([(50, footer_y), (width-50, footer_y+60)],
                   fill=colors['header'], outline=colors['border'])
    draw.text((width//2, footer_y+30), "EPIDISC v1.0.0 - Private Medical Consultation System",
              fill=colors['white'], font=font_medium, anchor="mm")

    # Save the image
    img.save(output_path, 'PNG', quality=95)
    print(f"Architecture diagram saved to {output_path}")
    return output_path


def markdown_to_pdf(md_file, pdf_file, diagram_path):
    """Convert markdown to PDF with reportlab"""
    if not REPORTLAB_AVAILABLE:
        print("Error: reportlab not available")
        return False

    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

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

    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=9,
        textColor=HexColor('#7f8c8d'),
        spaceAfter=8,
        fontName='Courier',
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

    # Parse markdown and add to story
    lines = md_content.split('\n')
    in_code_block = False
    code_buffer = []

    for line in lines:
        # Handle code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            if code_buffer:
                code_text = '<br/>'.join(code_buffer)
                story.append(Paragraph(code_text, code_style))
                code_buffer = []
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        # Handle headings
        if line.startswith('# '):
            story.append(Paragraph(line[2:], heading1_style))
        elif line.startswith('## '):
            story.append(Paragraph(line[3:], heading2_style))
        elif line.startswith('### '):
            story.append(Paragraph(line[4:], heading3_style))
        elif line.startswith('#### '):
            story.append(Paragraph(line[5:], ParagraphStyle('H4', parent=heading3_style, fontSize=10)))
        # Handle horizontal rules
        elif line.startswith('---'):
            story.append(HRFlowable(width='100%', thickness=1, color=HexColor('#bdc3c7')))
            story.append(Spacer(1, 0.2*inch))
        # Handle images
        elif line.startswith('![[') and ']]' in line:
            # This is where we'll insert the architecture diagram
            if diagram_path and os.path.exists(diagram_path):
                img = Image(diagram_path, width=5*inch, height=6*inch)
                story.append(img)
                story.append(Spacer(1, 0.3*inch))
        # Handle lists
        elif line.startswith('- ') or line.startswith('* '):
            bullet_text = f"• {line[2:]}"
            story.append(Paragraph(bullet_text, body_style))
        elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
            num_text = line[line.index('. ')+2:]
            story.append(Paragraph(num_text, body_style))
        # Handle tables (simplified)
        elif line.startswith('|') and line.endswith('|'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) > 1:
                table_data = [[Paragraph(p, body_style) for p in parts]]
                story.append(Table(table_data, colWidths=[1*inch]*len(parts)))
        # Handle empty lines
        elif not line.strip():
            story.append(Spacer(1, 0.1*inch))
        # Handle regular text
        else:
            # Convert markdown formatting to HTML
            line = line.replace('**', '<b>').replace('**', '</b>')
            line = line.replace('*', '<i>').replace('*', '</i>')
            line = line.replace('`', '<font face="Courier">').replace('`', '</font>')

            # Handle URLs
            if '[' in line and '](' in line:
                import re
                line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)

            story.append(Paragraph(line, body_style))

    # Build PDF
    try:
        doc.build(story)
        print(f"PDF generated successfully: {pdf_file}")
        return True
    except Exception as e:
        print(f"Error building PDF: {e}")
        return False


def main():
    """Main function"""
    print("EPIDISC Comprehensive PDF Generator")
    print("=" * 50)

    # Create architecture diagram
    print("\n1. Creating architecture diagram...")
    diagram_path = create_architecture_diagram()

    if not diagram_path:
        print("Warning: Could not create architecture diagram")

    # Convert markdown to PDF
    print("\n2. Converting markdown to PDF...")
    md_file = "EPIDISC_Comprehensive_Manual.md"
    pdf_file = "EPIDISC_Comprehensive_Manual.pdf"

    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found")
        return False

    success = markdown_to_pdf(md_file, pdf_file, diagram_path)

    if success:
        print(f"\n✅ PDF generated successfully: {pdf_file}")
        print(f"📊 Architecture diagram: {diagram_path}")
        return True
    else:
        print("\n❌ Failed to generate PDF")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
