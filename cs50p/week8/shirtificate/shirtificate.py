from fpdf import FPDF


def main():
    pdf = FPDF()
    pdf.set_font("Helvetica")
    pdf.set_page_background((252,212,255))
    for i in range(9):
        if i == 6:
            pdf.set_page_background("shirtificate.png")
        pdf.add_page(format=(210 * (1 - i/10), 297 * (1 - i/10)))
        pdf.cell(text=str(i))
    pdf.set_page_background(None)
    pdf.add_page(same=True)
    pdf.cell(text="9")
    pdf.output("varying_format.pdf")


if __name__ == "__main__":
    main()
