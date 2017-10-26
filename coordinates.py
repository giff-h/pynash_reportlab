from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.colors import red, green, blue
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics, ttfonts

from copy import deepcopy


pdfmetrics.registerFont(ttfonts.TTFont("AbrilFatface", "./assets/AbrilFatface-Regular.ttf"))
pdfmetrics.registerFont(ttfonts.TTFont("IndieFlower", "./assets/IndieFlower.ttf"))
pdfmetrics.registerFont(ttfonts.TTFont("Saira", "./assets/Saira-Bold.ttf"))

pdf = Canvas("./graphics.pdf", pagesize=letter)
pdf.setFont("AbrilFatface", 100)
style = getSampleStyleSheet()["Normal"]

style1 = deepcopy(style)
style1.fontName = "AbrilFatface"
style1.fontSize = 100
style1.leading = 120
p1 = Paragraph("First thing drawn", style1)
_, y = p1.wrap(letter[0] - 60, letter[1] - 60)
p1.drawOn(pdf, 60, letter[1] - (60 + y))

pdf.setStrokeColor(red)
pdf.setLineWidth(5)
pdf.setFillColor(red)
pdf.circle(letter[0] // 2 + 50, letter[1] - 250, r=120, fill=1)

style2 = deepcopy(style)
style2.fontName = "IndieFlower"
style2.fontSize = 120
style2.leading = 144
style2.textColor = green
p2 = Paragraph("Third thing drawn", style2)
_, y = p2.wrap(letter[0] // 2, letter[1] - 280)
p2.drawOn(pdf, letter[0] // 2, letter[1] - (280 + y))

pdf.setStrokeColor(blue)
pdf.setLineWidth(20)
pdf.rect(100, 100, letter[0] - 120, letter[1] - 120)

style3 = deepcopy(style)
style3.fontName = "Saira"
style3.fontSize = 60
style3.leading = 72
p3 = Paragraph("Fifth third bank", style3)
_, y = p3.wrap(letter[0] - 120, 120)
p3.drawOn(pdf, 120, 120 - y)

pdf.drawImage("./assets/preds.png", 0, 200, width=letter[0], preserveAspectRatio=True)

pdf.showPage()
pdf.save()
