import pandas as pd
import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

# Load the CSV file
csv_file = "csvTest.csv"  
data = pd.read_csv(csv_file)


sender_email = os.getenv("MAIL")
sender_password = os.getenv("PASS")  # Preferred to use app password

# Initialize yagmail with your Gmail credentials
yag = yagmail.SMTP(sender_email, sender_password)

for index, row in data.iterrows():
    # Extract details from the CSV
    name = row['FULLNAME']
    role = row['SELECTPOSITION']  
    department = row['SELECTON-DAYTEAM']
    recipient_email = row['EmailAddress']

    subject = f"Welcome to the {department} Team, {name}!"
    message = f"""
    Dear {name},

    Welcome to the team of the ACM - Developers' Day 2024. We are excited to have you on board and look forward to the contributions you will make as {role} in the {department} department.
    
    It is worth acknowledging that the team of DevDay plays a crucial role in shaping the future of our event. Your involvement will be essential in crafting strategies and ensuring that our objectives align with the needs of our community. We believe in fostering a positive and collaborative work environment where everyone can grow and succeed together.

    Our teams are committed to creating a supportive and inclusive environment where everyone's voices are heard and respected. We are confident that your addition to our team will further enhance our cohesion and effectiveness.

    Once again, welcome to the team! We are thrilled to have you with us and can't wait to see what we will achieve together.

    Best Regards,
    ACM - Developers' Day 2024 Team
    """
    try:
        yag.send(to=recipient_email, subject=subject, contents=message)
        print(f"Email sent to {name} at {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email to {name}. Error: {e}")
