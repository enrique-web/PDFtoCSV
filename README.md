
# PDFtoCSV

Convert PDF tables to CSV format easily using Python.

## Description

PDFtoCSV is a lightweight Python utility designed to extract tables from PDF documents and convert them into CSV files. This tool is useful for data extraction, analysis, and automation workflows where tabular data is embedded inside PDFs.

## Features

- Extract tables from PDF files
- Convert extracted tables into CSV format
- Simple and easy-to-use Python interface
- Supports multiple pages and tables per PDF
- Minimal dependencies

## Installation

Clone the repository:

```
git clone https://github.com/enrique-web/PDFtoCSV.git
cd PDFtoCSV
```

Install required dependencies:

```
pip install -r requirements.txt
```

*Note: The project may use libraries such as `tabula-py`, `camelot-py`, or `pdfplumber` for PDF table extraction.*

## Usage

Basic usage example:

```
from pdf_to_csv import convert_pdf_to_csv

input_pdf = "sample.pdf"
output_csv = "output.csv"

convert_pdf_to_csv(input_pdf, output_csv)
print("CSV file generated successfully!")
```

Replace `sample.pdf` with your PDF file path and `output.csv` with the desired CSV output path.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

