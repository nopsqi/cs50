from fpdf import FPDF


def main():
    pdf = FPDF(orientation="portrait", format="a4")
    pdf.set_font("Helvetica", size=36)
    # pdf.set_text_color(255, 255, 255)
    pdf.set_page_background("shirtificate.png")
    pdf.add_page()
    pdf.cell(None, None, "John Harvard took CS50", 1)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
