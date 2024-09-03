#sending emails

import smtplib, ssl

#smtplib is a standard python library, used as a email library which creates email client sessions
#SMTP=Simple Mail Transfer protocol, standard protocol used to send email messages
#SSL=Secure Sockets Layer
import os


def send_email(message):
    host = "smtp.gmail.com"  # host stores address of the server we need to connect to. Here it is gmail
    port = 465  # port number is used to establish connection with the SMTP server
    username = "niki999it@gmail.com"
    password = os.getenv("PASSWORD")#creating a environment variable therby maing it more secure
    reciever = "niki999it@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # server.timeout=60
        server.login(username, password)
        server.sendmail(username, reciever, message)




