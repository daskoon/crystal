from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import os

def create_presentation():
    prs = Presentation()
    
    # helper for slide with title and content
    def add_slide(title_text, content_text):
        slide_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(slide_layout)
        title = slide.shapes.title
        title.text = title_text
        
        tf = slide.placeholders[1].text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content_text
        p.font.size = Pt(18)

    # 1. Title Slide
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Crystal Shadows: Strategic Relaunch"
    subtitle.text = "2026 Executive Strategy & Digital Transformation Briefing\nAuthored by 13-Division AI Agency"

    # Report Contents to Slidify
    report_dir = "c:/Users/transmacsual/projects/crystal/antigravitys_take/"
    reports = [
        ("Market Intelligence", "market_intelligence_deepdive.md"),
        ("Financial Strategy", "financial_feasibility_projections.md"),
        ("Tech Architecture", "technical_architecture_blueprint.md"),
        ("UX/UI Specification", "ux_ui_specification.md"),
        ("SEO & Visibility", "seo_visibility_strategy.md"),
        ("Brand Identity", "brand_identity_guide.md"),
        ("Security & Legal", "security_legal_audit.md"),
        ("Accessibility", "accessibility_inclusive_audit.md"),
        ("SRE & Reliability", "performance_reliability_report.md"),
        ("Psychology & Nudge", "behavioral_psychology_analysis.md"),
        ("Support & SOPs", "client_success_support_sop.md")
    ]

    for title, filename in reports:
        path = os.path.join(report_dir, filename)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Basic cleaning for slide readability
            clean_content = content.replace('# ', '').replace('## ', '').replace('### ', '').replace('* ', '- ')
            lines = clean_content.split('\n')
            summary = "\n".join(lines[0:8]) + "..."
            add_slide(title.upper(), summary)

    output_path = "c:/Users/transmacsual/projects/crystal/antigravitys_take/Masterpiece_Strategic_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation generated at: {output_path}")

if __name__ == "__main__":
    create_presentation()
