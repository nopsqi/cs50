from fpdf import FPDF, XPos


def main():
    pdf = FPDF(orientation="portrait", format="a4")
    pdf.set_font("Helvetica", size=30)
    # pdf.set_text_color(255, 255, 255)
    pdf.add_page()
    pdf.set_y(pdf.h / 2)
    pdf.cell(w=(pdf.w - pdf.l_margin - pdf.r_margin), text="John Harvard took CS50", border=1, align="C")
    print(pdf.l_margin)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
