"""
This module export extracted data into a file.
- Accept a list of dictionary data parameter
- Accept filename and 'output.csv' as default filename and file format
"""
import pandas as pd


def export_data(data, filename='filename.xlsx'): #default output(xlsx)
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

    print(f"Data exported to {filename}")