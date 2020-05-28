import smtplib, ssl

# Create a secure SSL context

port = 587  # For starttls
smtp_server = "email.briq-institute.org"
sender_email = "Andrea.Amelio@briq-institute.org"
receiver_email = "some@recipient.help"
password = input("Type your password and press enter:")
message = """\
Subject: Ciao

Lore ipsum ."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
