import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate




def multipart(send_from, send_to, subject, text, files=None):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    
    #smtp = smtplib.SMTP(server)
    #smtp.sendmail(send_from, send_to, msg.as_string())
    #smtp.close()
    return msg

def send(send_from, send_to, username, password, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(send_from, send_to, msg if type(msg) == str else msg.as_string())
    server.quit()


send_from = 'bnp.supplier@gmail.com'
send_to = 'daniil@jcatalog.club'
msg = 'Why,Oh why!'
msg = multipart(send_from, [send_to], "This is my subject", "Hello world", ['kek.txt']) 
username = 'bnp.supplier@gmail.com'
password = '!Test1337'
send(send_from, send_to, username, password, msg)
