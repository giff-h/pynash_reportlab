from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

w = 5 * inch
h = 3 * inch
pdfmetrics.registerFont(ttfonts.TTFont("Respective", "./assets/Respective.ttf"))

style = getSampleStyleSheet()["Normal"]
style.fontName = "Respective"
style.fontSize = 40
style.leading = round(style.fontSize * 1.2)
p = Paragraph("You are invited", style)

pdf = Canvas("./invite.pdf", pagesize=(w, h))
pdf.drawImage("./assets/marble_bg.jpg", 0, 0, width=w, height=h)
_, y = p.wrap(w, h)
x = pdfmetrics.stringWidth(p.text, style.fontName, style.fontSize)
p.drawOn(pdf, (w - x) / 2, (h - y) / 2)
pdf.showPage()
pdf.save()
