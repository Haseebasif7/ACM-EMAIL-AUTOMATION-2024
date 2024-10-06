import pandas as pd
import yagmail
import os
import pdfkit
from dotenv import load_dotenv
from letterFunction import getLetterWithAttributes

load_dotenv()

def convert_html_to_pdf(html_content, name):
    output_filename = f"{name}_welcome_letter.pdf"
    try:
        pdfkit.from_string(
            html_content,
            output_filename,
            configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'),
            options = {
    'enable-local-file-access': '',    
    'page-size': 'Letter',             
    'margin-top': '0in',               
    'margin-right': '0in',             
    'margin-bottom': '0in',           
    'margin-left': '0in',              
    'encoding': 'UTF-8',
    'no-outline': None,
    'background': '',                   
    'dpi': 300,                        
    'page-height': '11.7in',             
    'page-width': '8.23in'             
}

        )
        print(f"Successfully created PDF: {output_filename}")
    except Exception as e:
        print(f"Failed to generate PDF for {name}. Error: {e}")
        output_filename = None
    return output_filename

def process_csv_and_send_emails(csv_file):
    # Attempt to read the CSV file
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: The file at {csv_file} was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return

    sender_email = os.getenv("MAIL")
    sender_password = os.getenv("PASS")  # Preferred to use app password

    yag = yagmail.SMTP(sender_email, sender_password)

    for index, row in data.iterrows():
        name = row['FULLNAME']
        role = row['SELECTPOSITION']
        department = row['SELECTON-DAYTEAM']
        recipient_email = row['EmailAddress']

        html_content = getLetterWithAttributes(name, role, department)

        pdf_file_path = convert_html_to_pdf(html_content, name)

        
        """
        if pdf_file_path:
            try:
                # Attach the generated PDF and send the email
                yag.send(to=recipient_email, subject=f"Welcome to the {department} Team, {name}!", contents=[pdf_file_path])
                print(f"Email sent to {name} at {recipient_email}.")
            except Exception as e:
                print(f"Failed to send email to {name}. Error: {e}")
        else:
            print(f"Skipping email to {name} as PDF generation failed.")
        """
