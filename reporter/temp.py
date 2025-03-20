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
