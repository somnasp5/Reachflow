import os

import smtplib

from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


def send_email(

    receiver_email,

    subject,

    body,

    attachment_path=None
):

    sender_email = os.getenv(
        "EMAIL_ADDRESS"
    )

    app_password = os.getenv(
        "EMAIL_APP_PASSWORD"
    )
    print("EMAIL:", sender_email) 
    print("PASSWORD:", app_password)

    msg = EmailMessage()

    msg["Subject"] = subject

    msg["From"] = sender_email

    msg["To"] = receiver_email

    msg.set_content(body)

    # ATTACH FILE

    if attachment_path:

        with open(
            attachment_path,
            "rb"
        ) as f:

            file_data = f.read()

            file_name = os.path.basename(
                attachment_path
            )

        msg.add_attachment(

            file_data,

            maintype="application",

            subtype="octet-stream",

            filename=file_name
        )

    # GMAIL SMTP

    with smtplib.SMTP_SSL(

        "smtp.gmail.com",

        465

    ) as smtp:

        smtp.login(
            sender_email,
            app_password
        )

        smtp.send_message(msg)

    return True
