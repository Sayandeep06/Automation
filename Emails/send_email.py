import smtplib
from email.mime.text import MIMEText

# Defining the smtp server
smtp_server = 'smtp.gmail.com'
port = 587 #TLS
sender_email = 'sayanawsacc@gmail.com'
receiver_email = 'sayanawsacc@gmail.com'
message = 'This is an automated message'

# Create a MIMEText object for email content
msg = MIMEText(message)
msg['Subject'] = 'Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email

#Set up the connection to the SMTP server
with smtplib.SMTP(smtp_server, port) as server:
    #Start TLS encryption
    server.starttls()
    
    #login to Gmail account
    password = input("Enter your Gmail password and press enter: ")
    server.login(sender_email, password)
    
    #Send the email
    server.sendmail(sender_email, [receiver_email], msg.as_string())
 