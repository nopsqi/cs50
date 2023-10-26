from fpdf import FPDF


def main():
    pdf = FPDF()
    pdf.set_font("Helvetica")
    pdf.add_page(format=(210 * (1 - i/10), 297 * (1 - i/10)))
    pdf.cell(text="9")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
