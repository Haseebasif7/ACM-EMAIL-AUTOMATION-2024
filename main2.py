import pandas as pd
import yagmail
import os
import pdfkit
from dotenv import load_dotenv
from letterFunction import getLetterWithAttributes

load_dotenv()

csv_file = "C:/Users/Asif/Desktop/acm/ACM-EMAIL-AUTOMATION-2024/csvTest.csv"  
data = pd.read_csv(csv_file)


sender_email = os.getenv("MAIL")
sender_password = os.getenv("PASS")  # Preferred to use app password

yag = yagmail.SMTP(sender_email, sender_password)

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

def convert_html_to_pdf(html_content, name):
    output_filename = f"{name}_welcome_letter.pdf"  
    try:
        pdfkit.from_string(
            html_content,
            output_filename,
            configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'),
            options={
            'enable-local-file-access': '',  # Allow local file access
            'page-size': 'Letter',
            'margin-top': '0in',
            'margin-right': '0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'encoding': 'UTF-8',
            'no-outline': None
    }
        )
        print(f"Successfully created PDF: {output_filename}")
    except Exception as e:
        print(f"Failed to generate PDF for {name}. Error: {e}")
        output_filename = None
    return output_filename


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