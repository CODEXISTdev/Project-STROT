from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def footer(self):
        # Get today's date
        today = datetime.today().strftime('%d-%m-%Y')

        # Set position 20 units from bottom
        self.set_y(-20)

        # Add logo at left
        self.image('logo.png', x=10, y=self.get_y(), w=30)

        # Set font for date
        self.set_font('Arial', 'I', 10)

        # Add date on the right side
        self.set_x(-50)  # move to right margin
        self.cell(0, 10, f"Date: {today}", 0, 0, 'R')  # 'R' = right aligned

# Create PDF
pdf = PDF()

# Add some pages
for i in range(3):
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"This is page {i + 1}", ln=True)

# Save the file
pdf.output("output_with_logo_and_date.pdf")
