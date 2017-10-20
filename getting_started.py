from reportlab.pdfgen.canvas import Canvas

# This is your PDF writer
pdf = Canvas("./start.pdf")

# Everything is coordinate based
pdf.drawString(100, 100, "Hello, World!")

# Writes everything to a page, then moves onto another one
pdf.showPage()

# Performs the write to disk
pdf.save()
