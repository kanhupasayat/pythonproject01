import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "iamkanhu7752@yahoo.com "
receiver_email = "kanhupasayat1@gmail.com"
subject = "Mai madarchod hoon"
message = "This is the message body of the email."

# Create a MIMEText object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the email
msg.attach(MIMEText(message, 'plain'))

# SMTP server configuration (e.g., for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "iamkanhu7752@yahoo.com "
smtp_password = "ssdkbbfmxfruynwj"

# Create an SMTP connection
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use TLS encryption
    server.login(smtp_username, smtp_password)  # Login to your email account
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)  # Send the email
    server.quit()  # Quit the SMTP server
    print("Email sent successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")