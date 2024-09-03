#generating pdf files from excel sheets
#automation programs-written as simple scripts without any gui.

import pandas as pd
import glob#creates list of filepaths
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf=FPDF(orientation="P",unit="mm",format="A4")

    pdf.add_page()

    filename=Path(filepath).stem

    invoice_nr, date=filename.split("-")

    pdf.set_font(family="Times",style="B", size=24)
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}",ln=1)

    pdf.ln()

    pdf.cell(w=50,h=8,txt=f"Date:{date}", ln=1)
    pdf.ln()

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    column = [items.replace("_"," ").title() for items in df.columns]
    pdf.set_font(family="Times", size=10, style="B")

    pdf.cell(w=30, h=8, txt=column[0], border=1)
    pdf.cell(w=45, h=8, txt=column[1], border=1)
    pdf.cell(w=35, h=8, txt=column[2], border=1)
    pdf.cell(w=30, h=8, txt=column[3], border=1)
    pdf.cell(w=30, h=8, txt=column[4], border=1, ln=1)


    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]),border=1)
        pdf.cell(w=45, h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)


    total=df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=45, h=8, txt="", border=1)
    pdf.cell(w=35, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)

    pdf.ln()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=30, h=8, txt=f"The total price is {total}",  ln=1)


    pdf.cell(w=30, h=8, txt="Ittismita",  ln=1)
    #pdf.image("")








pdf.output(f"pdfs/{invoice_nr}.pdf")