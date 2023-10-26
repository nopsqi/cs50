from fpdf import FPDF, XPos


def main():
    pdf = FPDF(orientation="portrait", format="a4")
    pdf.set_font("Helvetica", size=30)
    # pdf.set_text_color(255, 255, 255)
    pdf.set_page_background("shirtificate.png")
    pdf.add_page()
    pdf.set_y(pdf.h / 2)
    pdf.set_x(pdf.w / 2)
    pdf.cell(text="John Harvard took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
