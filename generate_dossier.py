from fpdf import FPDF
import os

class CrystalDossier(FPDF):
    def header(self):
        # Professional header with background logic
        self.set_fill_color(5, 5, 7) # Deep Shadow
        self.rect(0, 0, 210, 40, 'F')
        self.set_font('helvetica', 'B', 16)
        self.set_text_color(255, 255, 255)
        self.cell(0, 20, 'CRYSTAL SHADOWS: MASTERPIECE RELAUNCH', ln=True, align='C')
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 5, 'Strategic Intelligence & Executive Briefing', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | Confidential Strategic Document | (c) 2026 Crystal Shadows', align='C')

def generate_dossier():
    pdf = CrystalDossier()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title Page
    pdf.add_page()
    pdf.set_y(80)
    pdf.set_font('helvetica', 'B', 24)
    pdf.set_text_color(5, 5, 7)
    pdf.cell(0, 20, 'EXECUTIVE DOSSIER', ln=True, align='C')
    pdf.set_font('helvetica', '', 14)
    pdf.cell(0, 10, 'A 360-Degree Analysis of the Digital Transformation', ln=True, align='C')
    pdf.ln(20)
    pdf.set_font('helvetica', 'I', 10)
    pdf.multi_cell(0, 5, "This document consolidates the expertise of 13 specialized AI divisions, covering everything from market intelligence and technical architecture to behavioral psychology and legal compliance.", align='C')

    # Content Directory
    report_dir = "c:/Users/transmacsual/projects/crystal/antigravitys_take/"
    reports = [
        "market_intelligence_deepdive.md",
        "financial_feasibility_projections.md",
        "technical_architecture_blueprint.md",
        "ux_ui_specification.md",
        "seo_visibility_strategy.md",
        "brand_identity_guide.md",
        "security_legal_audit.md",
        "accessibility_inclusive_audit.md",
        "performance_reliability_report.md",
        "behavioral_psychology_analysis.md",
        "client_success_support_sop.md"
    ]

    for report_file in reports:
        path = os.path.join(report_dir, report_file)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pdf.add_page()
            # Clean up markdown headers for PDF display
            title = report_file.replace('.md', '').replace('_', ' ').upper()
            pdf.set_font('helvetica', 'B', 14)
            pdf.set_text_color(100, 59, 159) # Astral Purple
            pdf.cell(0, 10, title, ln=True)
            pdf.ln(5)
            
            pdf.set_font('helvetica', '', 10)
            pdf.set_text_color(0, 0, 0)
            # Remove MD artifacts and sanitize unicode
            clean_content = content.replace('# ', '').replace('## ', '').replace('### ', '').replace('* ', '- ')
            # Sanitize smart quotes and other common unicode issues for FPDF latin-1
            clean_content = clean_content.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"').replace('\u2013', '-').replace('\u2014', '--')
            # Final safety encoding/decoding
            clean_content = clean_content.encode('latin-1', 'replace').decode('latin-1')
            
            pdf.multi_cell(0, 5, clean_content)
    
    output_path = "c:/Users/transmacsual/projects/crystal/antigravitys_take/Masterpiece_Executive_Dossier.pdf"
    pdf.output(output_path)
    print(f"Dossier generated at: {output_path}")

if __name__ == "__main__":
    generate_dossier()
