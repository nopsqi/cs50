from fpdf import FPDF, Align


def main():
    pdf = FPDF(orientation="portrait", format="a4")
    pdf.set_margin(13)
    pdf.set_font("Helvetica")
    pdf.add_page()

    pdf.set_y(pdf.h / 10)
    pdf.set_font_size(40)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=(pdf.w - pdf.l_margin - pdf.r_margin), text="CS50 Shirtificate", border=1, align=Align.C)

    pdf.set_y(pdf.get_y() + 10)
    pdf.image("shirtificate.png", x=Align.C, w=(pdf.w - pdf.l_margin - pdf.r_margin))

    pdf.set_y(pdf.h / 2)
    pdf.set_font_size(25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=(pdf.w - pdf.l_margin - pdf.r_margin), text="John Harvard took CS50", border=1, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
