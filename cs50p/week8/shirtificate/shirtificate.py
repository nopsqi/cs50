from fpdf import FPDF


def main():
    pdf = FPDF(orientation="portrait", format="a4")
    pdf.set_font("Helvetica")
    pdf.set_page_background("shirtificate.png")
    pdf.add_page()
    pdf.cell(text="9")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
