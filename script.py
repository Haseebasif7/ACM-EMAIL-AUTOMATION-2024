import pandas as pd
import os
import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
from letterFunction import getLetterWithAttributes
from datetime import datetime
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    filename='email_automation.log',
    level=logging.DEBUG,  # Set to DEBUG to capture all messages
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def convert_html_to_pdf(html_content, name):
    output_filename = f"{name}_welcome_letter.pdf"
    try:
        pdfkit.from_string(
            html_content,
            output_filename,
            configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'),
            options={
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
        logging.info(f"Successfully created PDF: {output_filename}")
    except Exception as e:
        logging.error(f"Failed to generate PDF for {name}. Error: {e}")
        output_filename = None
    return output_filename

def send_email(recipient_email, subject, html_content, pdf_file_path, image_path):
    sender_email = os.getenv("MAIL")
    sender_password = os.getenv("PASS")  # Preferred to use app password

    # Create the email container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Attach the PDF file
    if pdf_file_path:
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
            pdf_attachment.add_header(
                'Content-Disposition',
                f'attachment; filename="{os.path.basename(pdf_file_path)}"'
            )
            pdf_attachment.add_header('Content-ID', '<pdfAttachment>')  # Ensure no "noname" issue
            msg.attach(pdf_attachment)

    # Attach the image
    with open(image_path, 'rb') as img_file:
        img_attachment = MIMEImage(img_file.read())
        img_attachment.add_header('Content-ID', '<acmLogo>')  # This ID is used in the HTML for embedding the image
        img_attachment.add_header('Content-Disposition', 'inline; filename="acmLogo.jpeg"')  # Make image inline
        msg.attach(img_attachment)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.send_message(msg)
            logging.info(f"Email sent to {recipient_email}.")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}. Error: {e}")


def process_csv_and_send_emails(csv_file):
    # Attempt to read the CSV file
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        logging.error(f"Error: The file at {csv_file} was not found.")
        return
    except pd.errors.EmptyDataError:
        logging.error("Error: The file is empty.")
        return
    except pd.errors.ParserError:
        logging.error("Error: The file could not be parsed.")
        return

    failed_emails = []

    for index, row in data.iterrows():
        name = row['FULLNAME']
        role = row['SELECTPOSITION']
        department = row['SELECTON-DAYTEAM']
        recipient_email = row['EmailAddress']

        # Generate HTML content using the provided function
        html_content = getLetterWithAttributes(name, role, department)

        # Construct the final HTML email with the header and body (with logo)
        final_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                width: 80%;
                max-width: 500px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                border: 5px solid rgb(13, 95, 145);
                border-radius: 5px;
            }}
            .email-header {{
                padding: 10px;
                text-align: center;
                color: rgb(0, 0, 0);
            }}
            .email-body {{
                padding: 20px;
            }}
            .email-body h2 {{
                color: black;
            }}
            .email-footer {{
                text-align: center;
                font-size: 12px;
                color: #999;
                padding: 20px 0;
                border-top: 1px solid #e0e0e0;
            }}
            .email-footer a {{
                text-decoration: none;
            }}
        </style> 
        </head>

        <body>
            <div class="email-container">
                <div class="email-header">
                    <img src="cid:acmLogo" style="width: 50%; border-radius:10px;" alt="ACM Logo">
                    <h1>Welcome to ACM</h1>
                </div>

                <!-- Body -->
                <div class="email-body">
                    <h2>Hello!</h2>
                    <p>Welcome to the ACM community. We are excited to have you!</p>
                </div>

                <!-- Footer -->
                <div class="email-footer">
                    <p>Regards,<br>ACM Team</p>
                </div>
            </div>
        </body>
</html>
        """

        pdf_html_content = html_content.replace(
            '<img src="cid:acmLogo" style="width: 50%; border-radius:10px;" alt="ACM Logo">',
            ''
        )

        pdf_file_path = convert_html_to_pdf(pdf_html_content, name)

        image_url = 'C:/Users/Asif/Desktop/acm2/ACM-EMAIL-AUTOMATION-2024/acmLogo.jpeg'

        try:
            send_email(recipient_email, f"Welcome to the {department} Team, {name}!", final_html, pdf_file_path, image_url)
            # Record the timestamp
            data.at[index, 'EmailSentTimestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            failed_emails.append(row)
            

    data.to_csv(csv_file, index=False)
    
    if failed_emails:
        failed_df = pd.DataFrame(failed_emails)
        failed_csv_file = 'failed_email_recipients.csv'
        failed_df.to_csv(failed_csv_file, index=False)
        logging.info(f"Failed email recipients saved to {failed_csv_file}.")
        


