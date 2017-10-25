from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


w = 8 * inch
h = 6 * inch

title_fontsize = 100
top_margin = 10
side_margin = 50

points_style = getSampleStyleSheet()["Bullet"]


def slide_title(canvas: Canvas, title: str):
    canvas.setFontSize(title_fontsize)
    canvas.drawCentredString(w / 2, h - (title_fontsize + top_margin), title)


def slide_points(canvas: Canvas, points: list):
    draw_y = h
    for point in points:
        point = Paragraph(point, points_style)
        draw_y -= point.wrap()


def points_slide(canvas, title, points):
    pass


pdf = Canvas("./pdf_talk.pdf")

