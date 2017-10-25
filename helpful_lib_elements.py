from reportlab.lib.colors import red, green, blue, \
    Color, HexColor, CMYKColor
from reportlab.lib.units import inch, cm, mm
from reportlab.lib.pagesizes import letter, legal, \
    elevenSeventeen
from reportlab.lib.styles import getSampleStyleSheet, \
    ParagraphStyle, ListStyle


# ParagraphStyle
normal = getSampleStyleSheet()["Normal"]
bullet = getSampleStyleSheet()["Bullet"]

# ListStyle
ul = getSampleStyleSheet()["UnorderedList"]

# dict
print(getSampleStyleSheet().byName)

# [red, green, blue, Color, HexColor, CMYKColor, letter, legal, elevenSeventeen, inch, cm,
#  mm, ParagraphStyle, ListStyle]
