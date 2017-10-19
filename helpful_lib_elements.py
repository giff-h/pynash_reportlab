from reportlab.lib.colors import red, green, blue, chartreuse, plum, darkorchid, Color, HexColor, CMYKColor
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, ListStyle
from reportlab.lib.units import inch, cm, mm


# ParagraphStyle
normal = getSampleStyleSheet()["Normal"]
bullet = getSampleStyleSheet()["Bullet"]

# ListStyle
ul = getSampleStyleSheet()["UnorderedList"]

# dict
print(getSampleStyleSheet().byName)
