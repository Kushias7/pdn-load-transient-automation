from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(csv_file, output="test_report.pdf"):

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("PDN Automated Load Transient Test Report", styles['Title']))
    elements.append(Spacer(1,20))

    import csv

    data = []
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    table = Table(data)

    elements.append(table)

    doc = SimpleDocTemplate(output)
    doc.build(elements)