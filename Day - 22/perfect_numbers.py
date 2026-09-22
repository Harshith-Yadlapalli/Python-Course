import smtplib
from email.message import EmailMessage

sender = "nayan919sharma@gmail.com"
password = "nwogtcklorohfpqo"

contacts = [
    {"name": "Nayan", "email": "nayansharma032@gmail.com"},
    {"name": "yadagiri", "email": "yadagiribanda7@gmail.com"},
    {"name": "Ruthvik", "email": "ruthvikbandari9@gmail.com"},
]

count = 0
number = 1
with open("Day - 22/perfect_numbers.txt", "w") as file:
    while count < 4:
        sum_of_divisors = 0

        # Find the proper divisors
        for i in range(1, number):
            if number % i == 0:
                sum_of_divisors += i

        # Check if the number is perfect
        if sum_of_divisors == number:
            print(number)

            file.write(str(number) + "\n")

            count += 1

        number += 1

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender, password)
for contact in contacts:

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = contact["email"]
    msg["Subject"] = "First 5 Perfect Numbers"

    message = f"""
Hello {contact["name"]},

Here are the first 5 Perfect Numbers.

Regards,
Nayan Sharma
"""

    msg.set_content(message)

    with open("Day - 22/perfect_numbers.txt", "rb") as file:
        file_data = file.read()

    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="plain",
        filename="perfect_numbers.txt"
    )
    server.send_message(msg)

    print(f"Mail sent to {contact['email']}")

server.quit()
print("All Emails sent Successfully!")