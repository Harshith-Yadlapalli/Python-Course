# import smtplib
# sender = "nayan919sharma@gmail.com"
# receiver = "yadagiribanda7@gmail.com"
# password = ""
# msg = """ hi yadagiri
# How are u bro? hope u are doing good. im studying well in Codegnan, hope u are studying well too

# Thanks & Regards,
# Nayan Sharma"""
# server = smtplib.SMTP("smtp.gmail.com",587)
# server.starttls()
# server.login(sender,password)
# server.sendmail(sender,receiver,msg)
# server.quit()
# print("Mail has been sent successfully")

#----------------------------------------------------------------------------------------
#                                       CREATE THE EMAIL
#----------------------------------------------------------------------------------------
import smtplib
from email.message import EmailMessage

# Sender email details
sender = "nayan919sharma@gmail.com"
password = "your_app_password"
# Receiver email details
receiver = "receiver@gmail.com"
# Create the email
msg = EmailMessage()
# Add sender
msg["From"] = sender
# Add receiver
msg["To"] = receiver
# Add subject
msg["Subject"] = "Prime Numbers"
# Add email content
msg.set_content("""
Hello,

Please find the prime numbers from 2 to 100 attached.

Thanks & Regards,
Nayan
""")
#----------------------------------------------------------------------------------------
#                                       ATTACH THE FILE
#----------------------------------------------------------------------------------------

# Attach the file
with open("prime_numbers.txt", "rb") as file:
    file_data = file.read()
# Add the file as an attachment
msg.add_attachment(
    file_data,
    maintype="text",
    subtype="plain",
    filename="prime_numbers.txt"
)
# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
# Start a secure connection
server.starttls()
# Login to the sender's email
server.login(sender, password)
# Send the email
server.send_message(msg)
# Close the server connection
server.quit()
# Display success message
print("Mail sent successfully!")

#----------------------------------------------------------------------------------------
#                           BULK MAIL SENDING
#----------------------------------------------------------------------------------------
import smtplib
from email.message import EmailMessage
# Sender email details
sender = "nayan919sharma@gmail.com"
password = "your_app_password"

# List of contacts
contacts = [
    {"name": "Nayan", "email": "nayan@gmail.com"},
    {"name": "Rohan", "email": "rohan@gmail.com"},
]

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
# Start a secure connection
server.starttls()
# Login to sender email
server.login(sender, password)
# Send email to each contact
for contact in contacts:

    # Create email message
    msg = EmailMessage()

    # Add sender
    msg["From"] = sender

    # Add receiver
    msg["To"] = contact["email"]

    # Add subject
    msg["Subject"] = f"Hello {contact['name']}!"

    # Create the email message
    message = f"""
Hello {contact["name"]},

I hope you are doing well.

Regards,
Nayan
"""

    # Add message content
    msg.set_content(message)

    # Send the email
    server.send_message(msg)

    # Display the sent email
    print(f"Mail sent to {contact['email']}")
# Close the server connection
server.quit()
# Display successful completion
print("All emails sent successfully!")