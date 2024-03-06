import pandas as pd
import os

def initialize_email_file():
    # Define the path to the Excel file
    excel_file = 'emails.xlsx'
    
    # Check if the file already exists
    if not os.path.exists(excel_file):
        # Define the columns for the Excel file
        columns = ['TO', 'FROM', 'CONTENT', 'Unique_id']
        
        # Create a DataFrame with the specified columns
        df = pd.DataFrame(columns=columns)
        
        # Write the DataFrame to an Excel file
        df.to_excel(excel_file, index=False)
        print(f"'{excel_file}' has been created with the columns: {', '.join(columns)}")
    else:
        print(f"'{excel_file}' already exists.")

if __name__ == "__main__":
    initialize_email_file()
