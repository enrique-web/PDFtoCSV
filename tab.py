import tabula
import os

def pdf_to_csv(input_pdf_path: str, output_csv_path: str, pages='all'):
    """
    Extract tables from a PDF and save them as a CSV file.

    Parameters:
    - input_pdf_path: str, path to the input PDF file.
    - output_csv_path: str, path to save the output CSV file.
    - pages: str or list, pages to extract tables from (default 'all').
    """
    try:
        # Read tables from PDF into a list of DataFrames
        dfs = tabula.read_pdf(input_pdf_path, pages=pages, multiple_tables=True)

        if not dfs:
            print("No tables found in the PDF.")
            return

        # Concatenate all tables into one DataFrame
        combined_df = dfs[0]
        for df in dfs[1:]:
            combined_df = combined_df.append(df, ignore_index=True)

        # Save combined DataFrame to CSV
        combined_df.to_csv(output_csv_path, index=False)
        print(f"CSV file saved to: {output_csv_path}")

    except Exception as e:
        print(f"Error processing PDF: {e}")

# Example usage
if __name__ == "__main__":
    input_pdf = "example.pdf"      # Replace with your PDF file path
    output_csv = "output.csv"      # Desired CSV output path
    pdf_to_csv(input_pdf, output_csv)
