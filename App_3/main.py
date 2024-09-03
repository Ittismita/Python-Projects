from fpdf import FPDF
import pandas as pd

pdf= FPDF(orientation="P",unit="mm",format="A4")
#orientation =P for portrait, L for landscape
#dimension in milimeteres - units=mm
pdf.set_auto_page_break(auto=False,margin=0)

df=pd.read_csv("topics (1).csv")

for index, row in df.iterrows():
    pdf.add_page()#parent page

    #set the header
    pdf.set_font(family="Times",style="B",size=12)
    pdf.set_text_color(100,100,100)#(r,g,b)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1,border=0)

    # instructors method to add lines in pdf
    for y in range(20,290,10):
        pdf.line(10,y,200,y)




    # my way of adding lines into the pdf
    #diving 265 breaklines by 10 i get 26.5 breaklines, at each breakline i will have a line
    #so range is upto 27(27 not included) so 26 lines
    #initial line of header was at y=21 so next will be at 31 next at 41 next 51 etc etc so 21+(i*10)
    """
    pdf.line(10,21,200,21)   #(x1,y1,x2,y2)
    for i in range(27):
        pdf.line(10,21+(10*i),200,21+(10*i))"""




    #set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=6)
    pdf.set_text_color(100, 100, 100)  # (r,g,b)
    pdf.cell(w=0, h=6, txt=row["Topic"], align="R", ln=1, border=0)





    for i in range(row["Pages"]-1):#child page
        pdf.add_page()


        #instructors method to add lines in pdf
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)

        # my way of adding lines into the pdf
        """for i in range(27):
            pdf.line(10, 21 + (10 * i), 200, 21 + (10 * i))"""


        # set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=6)
        pdf.set_text_color(100, 100, 100)  # (r,g,b)
        pdf.cell(w=0, h=6, txt=row["Topic"], align="R", ln=1, border=0)




#adding another page
"""pdf.add_page()

pdf.set_font(family="Times",style="I",size=12)
pdf.cell(w=0,h=12,txt="hii",align="L",ln=1,border=1)
pdf.cell(w=0,h=12,txt="hello",align="L",ln=1,border=1)
#ln is breakline
#align="L" =left
"""

pdf.output("output.pdf")

