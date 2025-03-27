import fpdf
import os
from datetime import datetime


class Basics:
    def __init__(self):
        self.pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')

    def date(self):
        today = datetime.today().strftime("%B %d %Y")
        self.pdf.add_font('RobotoMono', '', "RobotoMono-ExtraLight.ttf", uni=True)
        self.pdf.set_y(-140)
        self.pdf.set_text_color(115,115,115)
        self.pdf.set_font('RobotoMono', '', 12)
        self.pdf.cell(0, 10, today, 0, 0, 'L')  # 'R' = right aligned


    def logo(self):
        self.pdf.set_margins(20, 15, 20)  # Set custom margins
        # self.pdf.set_auto_page_break(auto=True, margin=20)  # Bottom margin

        # Logo settings
        logo_path = "/fpdp/utils/logo.png"
        logo_width = 15
        logo_height = 7

        custom_right_margin = 5
        custom_bottom_margin = 5

        # Calculate position
        x_pos = self.pdf.w - custom_right_margin - logo_width
        y_pos = self.pdf.h - custom_bottom_margin - logo_height

        # Add logo
        self.pdf.image(logo_path, x=x_pos, y=y_pos, w=logo_width, h=logo_height)


    def add_page(self):
        self.pdf.add_page()


    def first_img(self):
        self.pdf.image("first_page_image.png", x=0, y=0, w=210, h=297)
        self.date()
        self.pdf.add_page()


    def heading1(self, heading: str = ""):
        self.pdf.set_font("times", style="b", size=16)
        self.pdf.cell(40, 10, heading)
        self.pdf.ln(10)


    def heading2(self, heading: str = ""):
        self.pdf.set_font("times", style="b", size=14)
        self.pdf.cell(40, 10, heading)
        self.pdf.ln(10)


    def heading3(self, heading: str = ""):
        self.pdf.set_font("times", style="b", size=12)
        self.pdf.cell(40, 10, heading)
        self.pdf.ln(10)

    # def heading4(self, heading: str = ""):
    #     self.pdf.set_font("times", style="b", size=10)
    #     self.pdf.cell(40, 10, heading)
    #     self.pdf.ln(10)

    def body(self, body_text: str = ""):
        self.pdf.set_font("times", size=10)
        self.pdf.multi_cell(0, 5, body_text, align="J")
        self.pdf.ln(2)

    def line(self):
        self.pdf.line(10, 20, 200, 20)

    def save(self, file_name: str = "output.pdf"):
        self.pdf.output(file_name)

    def italic(self, text):
        self.pdf.set_font("times", style="I", size=10)
        self.pdf.multi_cell(0, 5, text, align="J")
        self.pdf.ln(10)


    def numbering_points(self,items):
        for i, item in enumerate(items, start=1):
            # self.pdf.cell(10, 5, , ln=False)  # Numbering
            self.pdf.multi_cell(0, 5, f"\t\t\t\t{i}. "+item)  # Text content
        self.pdf.ln(3)

    def bullet_points(self, items):
        for i, item in enumerate(items, start=1):
            self.pdf.set_font("times", style="b", size=25)
            self.pdf.cell(10, 1, "\t\t.", ln=False)  # Numbering
            self.pdf.set_font("times", size=10)
            self.pdf.multi_cell(0, 5,  item)  # Text content
        self.pdf.ln(3)


    def column(self, columns, data):
        super().column()
        self.pdf.columns = columns
        self.pdf.data = data
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_table(self, columns, data):
        """Generate a table with columns and data."""
        self.pdf.set_font("Arial", size=10)
        col_width = self.pdf.w / (len(columns) + 1)
        row_height = 10

        # Print column headers (Bold, White Text, Dark Background)
        self.pdf.set_font("Arial", style='B', size=10)  # Bold for header
        self.pdf.set_text_color(255, 255, 255)  # White text
        self.pdf.set_fill_color(65, 79, 99)  # Dark background

        for col in columns:
            self.pdf.cell(col_width, row_height, col, border=1, align="L", fill=True)

        self.pdf.ln(row_height)  # Move to the next line
        self.pdf.set_text_color(0, 0, 0)  # Reset text color
        self.pdf.set_font("Arial", style='', size=10)  # Normal text for rows

        # Print table rows with alternating colors
        for row_idx, row in enumerate(data):
            if row_idx % 2 == 0:
                self.pdf.set_fill_color(255, 255, 255)  # White background
            else:
                self.pdf.set_fill_color(242, 242, 242)  # Light gray background

            for item in row:
                self.pdf.cell(col_width, row_height, str(item), border=1, align="L", fill=True)

            self.pdf.ln(row_height)  # Move to the next line
        self.pdf.ln(10)

    def disclaimer(self, disc: str = ""):
        self.pdf.set_font("times",style='I', size=10)
        self.pdf.multi_cell(0, 5, disc, align="J")
        self.pdf.ln(2)


    def code(self, body_text):
        # self.pdf.set_font("courier", size=10)
        # self.pdf.set_fill_color(65, 79, 99)
        # self.pdf.set_font("Courier", size=10)  # Monospace font like GitHub
        # self.pdf.set_fill_color(240, 240, 240)  # Light grey background
        # self.pdf.set_text_color(0, 0, 0)  # Black text
        # self.pdf.multi_cell(0, 5, body_text, align="J")
        # self.pdf.ln(2)

        """Create a GitHub-style code block with a grey background."""
        self.pdf.set_font("Courier", size=10)  # Monospace font like GitHub
        self.pdf.set_fill_color(240, 240, 240)  # Light grey background
        self.pdf.set_text_color(0, 0, 0)  # Black text
        self.pdf.multi_cell(0, 5, body_text, fill=True)  # Box around text
        self.pdf.ln(5)  # Add spacing after the block


if __name__ == "__main__":
    obj = Basics()
    obj.add_page()

    obj.heading1("heading _ 1")
    obj.line()
    obj.heading2("heading _ 2")
    obj.heading3("heading _ 3")
    obj.body(
        "hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer hello this is ganesh shinde you are a very good programmer")
    obj.numbering_points(["ganesh","siddhant","pratik shinde"])
    obj.add_table(["ID", "Name", "Age", "City"],[1, "Alice", 24, "New York"])
    obj.save()

    os.system("open output.pdf")






