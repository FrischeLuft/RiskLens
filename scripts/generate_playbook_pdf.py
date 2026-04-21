"""Generate a simple PDF version of the RiskLens Russian guide."""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "RiskLens_Guide_RU.md"
TARGET = ROOT / "docs" / "RiskLens_Guide_RU.pdf"
FONT_REGULAR = "/Library/Fonts/DejaVuSans.ttf"
FONT_BOLD = "/Library/Fonts/DejaVuSans-Bold.ttf"


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("RiskLensSans", FONT_REGULAR))
    pdfmetrics.registerFont(TTFont("RiskLensSansBold", FONT_BOLD))


def build_styles() -> dict[str, ParagraphStyle]:
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "GuideTitle",
            parent=styles["Title"],
            fontName="RiskLensSansBold",
            fontSize=22,
            leading=28,
            spaceAfter=12,
        ),
        "h1": ParagraphStyle(
            "GuideH1",
            parent=styles["Heading1"],
            fontName="RiskLensSansBold",
            fontSize=16,
            leading=20,
            spaceBefore=12,
            spaceAfter=6,
        ),
        "h2": ParagraphStyle(
            "GuideH2",
            parent=styles["Heading2"],
            fontName="RiskLensSansBold",
            fontSize=13,
            leading=17,
            spaceBefore=10,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "GuideBody",
            parent=styles["BodyText"],
            fontName="RiskLensSans",
            fontSize=10.5,
            leading=14,
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "GuideBullet",
            parent=styles["BodyText"],
            fontName="RiskLensSans",
            fontSize=10.5,
            leading=14,
            leftIndent=14,
            firstLineIndent=-8,
            spaceAfter=3,
        ),
    }


def markdown_to_story(markdown_text: str) -> list:
    styles = build_styles()
    story: list = []
    in_code_block = False

    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            story.append(Paragraph(escape(line), styles["body"]))
            continue

        if not line.strip():
            story.append(Spacer(1, 3))
            continue

        if line.startswith("# "):
            story.append(Paragraph(escape(line[2:].strip()), styles["title"]))
            continue

        if line.startswith("## "):
            story.append(Paragraph(escape(line[3:].strip()), styles["h1"]))
            continue

        if line.startswith("### "):
            story.append(Paragraph(escape(line[4:].strip()), styles["h2"]))
            continue

        if line.startswith("- "):
            story.append(Paragraph("&bull; " + escape(line[2:].strip()), styles["bullet"]))
            continue

        story.append(Paragraph(escape(line), styles["body"]))

    return story


def main() -> None:
    register_fonts()
    text = SOURCE.read_text(encoding="utf-8")
    doc = SimpleDocTemplate(
        str(TARGET),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="RiskLens Guide RU",
        author="Igor Pokhotelov",
    )
    doc.build(markdown_to_story(text))


if __name__ == "__main__":
    main()
