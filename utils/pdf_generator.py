"""
Generates a styled Career Roadmap PDF using reportlab.
Falls back to a plain text PDF if reportlab is unavailable.
"""


def generate_roadmap_pdf(target_role: str, roadmap_data: dict) -> bytes:
    """
    Generate a career roadmap PDF.
    Returns bytes of the PDF file.
    """
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.colors import HexColor, white, black
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer,
            Table, TableStyle, HRFlowable
        )
        from reportlab.lib.units import cm
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        import io

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm,
        )

        # Colors
        DARK = HexColor("#0a0a0f")
        PURPLE = HexColor("#6c63ff")
        GREEN = HexColor("#43e97b")
        YELLOW = HexColor("#f7b731")
        LIGHT = HexColor("#e8e8f0")
        MUTED = HexColor("#6b6b8a")
        SURFACE = HexColor("#12121a")

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "Title",
            fontName="Helvetica-Bold",
            fontSize=26,
            textColor=LIGHT,
            alignment=TA_CENTER,
            spaceAfter=6,
        )
        subtitle_style = ParagraphStyle(
            "Subtitle",
            fontName="Helvetica",
            fontSize=12,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=20,
        )
        section_style = ParagraphStyle(
            "Section",
            fontName="Helvetica-Bold",
            fontSize=14,
            textColor=PURPLE,
            spaceAfter=8,
            spaceBefore=16,
        )
        body_style = ParagraphStyle(
            "Body",
            fontName="Helvetica",
            fontSize=10,
            textColor=LIGHT,
            spaceAfter=4,
            leading=16,
        )
        label_style = ParagraphStyle(
            "Label",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=GREEN,
            spaceAfter=4,
        )
        muted_style = ParagraphStyle(
            "Muted",
            fontName="Helvetica-Oblique",
            fontSize=9,
            textColor=MUTED,
            spaceAfter=2,
        )

        story = []

        # Header
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph("⚡ Career Roadmap", title_style))
        story.append(Paragraph(f"Target Role: {target_role}", subtitle_style))
        story.append(HRFlowable(color=PURPLE, thickness=2, width="100%"))
        story.append(Spacer(1, 0.4*cm))

        # Summary
        current_level = roadmap_data.get("current_level", "")
        gap_summary = roadmap_data.get("gap_summary", "")
        if current_level or gap_summary:
            story.append(Paragraph("Current Assessment", section_style))
            if current_level:
                story.append(Paragraph(f"<b>Current Level:</b> {current_level}", body_style))
            if gap_summary:
                story.append(Paragraph(f"<b>Gap Analysis:</b> {gap_summary}", body_style))
            story.append(Spacer(1, 0.3*cm))

        # Stages
        stages = roadmap_data.get("stages", [])
        stage_colors = [PURPLE, YELLOW, GREEN]
        level_labels = ["🔵 BEGINNER", "🟡 INTERMEDIATE", "🟢 ADVANCED"]

        for i, stage in enumerate(stages):
            color = stage_colors[i % len(stage_colors)]
            level = stage.get("level", f"Stage {i+1}")
            timeline = stage.get("timeline", "")
            skills = stage.get("skills", [])
            resources = stage.get("resources", [])
            milestones = stage.get("milestones", [])

            # Stage header table
            header_data = [[
                Paragraph(f"{level_labels[i] if i < len(level_labels) else level}", ParagraphStyle(
                    "SH", fontName="Helvetica-Bold", fontSize=13, textColor=white
                )),
                Paragraph(f"⏱ {timeline}", ParagraphStyle(
                    "SH2", fontName="Helvetica", fontSize=11, textColor=white, alignment=1
                ))
            ]]
            header_table = Table(header_data, colWidths=["70%", "30%"])
            header_table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,-1), color),
                ("ROWBACKGROUNDS", (0,0), (-1,-1), [color]),
                ("TOPPADDING", (0,0), (-1,-1), 10),
                ("BOTTOMPADDING", (0,0), (-1,-1), 10),
                ("LEFTPADDING", (0,0), (-1,-1), 14),
                ("RIGHTPADDING", (0,0), (-1,-1), 14),
                ("ROUNDEDCORNERS", (0,0), (-1,-1), [8,8,8,8]),
            ]))
            story.append(header_table)
            story.append(Spacer(1, 0.3*cm))

            if skills:
                story.append(Paragraph("Skills to Acquire:", label_style))
                skill_text = " · ".join(skills)
                story.append(Paragraph(skill_text, body_style))
                story.append(Spacer(1, 0.2*cm))

            if milestones:
                story.append(Paragraph("Milestones:", label_style))
                for m in milestones:
                    story.append(Paragraph(f"  ✓ {m}", body_style))
                story.append(Spacer(1, 0.2*cm))

            if resources:
                story.append(Paragraph("Learning Resources:", label_style))
                for r in resources:
                    story.append(Paragraph(f"  • {r}", muted_style))
                story.append(Spacer(1, 0.3*cm))

            story.append(HRFlowable(color=HexColor("#2a2a3d"), thickness=1, width="100%"))
            story.append(Spacer(1, 0.3*cm))

        # Footer
        story.append(Spacer(1, 1*cm))
        story.append(Paragraph(
            "Generated by ResumeAI Intelligence Platform · Powered by Gemini AI",
            ParagraphStyle("Footer", fontName="Helvetica-Oblique", fontSize=8, textColor=MUTED, alignment=TA_CENTER)
        ))

        # Build with dark background
        def dark_background(canvas, doc):
            canvas.saveState()
            canvas.setFillColor(DARK)
            canvas.rect(0, 0, A4[0], A4[1], fill=True, stroke=False)
            canvas.restoreState()

        doc.build(story, onFirstPage=dark_background, onLaterPages=dark_background)
        return buffer.getvalue()

    except ImportError:
        # Fallback: plain text "PDF" using fpdf2
        try:
            from fpdf import FPDF
            import io

            pdf = FPDF()
            pdf.add_page()
            pdf.set_fill_color(10, 10, 15)
            pdf.rect(0, 0, 210, 297, "F")
            pdf.set_text_color(232, 232, 240)
            pdf.set_font("Helvetica", "B", 20)
            pdf.cell(0, 12, f"Career Roadmap: {target_role}", ln=True, align="C")
            pdf.ln(5)

            stages = roadmap_data.get("stages", [])
            for stage in stages:
                pdf.set_font("Helvetica", "B", 13)
                pdf.set_text_color(108, 99, 255)
                pdf.cell(0, 10, f"{stage.get('level','')} — {stage.get('timeline','')}", ln=True)
                pdf.set_font("Helvetica", "", 10)
                pdf.set_text_color(232, 232, 240)
                for skill in stage.get("skills", []):
                    pdf.cell(0, 6, f"  • {skill}", ln=True)
                pdf.ln(3)

            return bytes(pdf.output())
        except Exception:
            # Ultimate fallback: return minimal PDF bytes
            return _minimal_text_pdf(target_role, roadmap_data)


def _minimal_text_pdf(target_role: str, roadmap_data: dict) -> bytes:
    """Ultra-minimal PDF generation without external libraries."""
    import io

    lines = [f"Career Roadmap: {target_role}", "=" * 50, ""]
    stages = roadmap_data.get("stages", [])
    for stage in stages:
        lines.append(f"[{stage.get('level','')}] — {stage.get('timeline','')}")
        for skill in stage.get("skills", []):
            lines.append(f"  • {skill}")
        for res in stage.get("resources", []):
            lines.append(f"  > {res}")
        lines.append("")

    text = "\n".join(lines)

    # Encode as simple text-based PDF
    content = f"""%PDF-1.4
1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj
2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj
3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Resources<<>>/Contents 4 0 R>>endobj
4 0 obj<</Length {len(text) + 50}>>
stream
BT /F1 12 Tf 50 750 Td 12 TL
({text[:200]}) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f
0000000009 00000 n
0000000058 00000 n
0000000115 00000 n
0000000266 00000 n
trailer<</Size 5/Root 1 0 R>>
startxref
400
%%EOF"""
    return content.encode("latin-1", errors="replace")
