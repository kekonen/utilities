import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import argparse
import os

username = os.environ['GMAIL_USERNAME']
password = os.environ['GMAIL_PASSWORD']

parser = argparse.ArgumentParser(description='Send Gmail from command line')

parser.add_argument('-f',
                    metavar='from',
                    type=str,
                    default=username + '@gmail.com',
                    help='Sender')

parser.add_argument('-t',
                    metavar='to',
                    type=str,
                    nargs='*',
                    help='Receivers')

parser.add_argument('-s',
                    metavar='Subject',
                    type=str,
                    help='Subject')

parser.add_argument('--files',
                    metavar='files',
                    type=str,
                    nargs='*',
                    help='Files to attach')

parser.add_argument('--text',
                    metavar='text',
                    type=str,
                    nargs='*',
                    help='Files to attach')

parser.add_argument('--tf',
                    metavar='textfile',
                    type=argparse.FileType('r', encoding='UTF-8'),
                    help='File containing text for sending')

args = parser.parse_args()

send_from = args.f
send_to = args.t
subject = args.s
files = args.files
text = args.text

if text and type(text) == list:
    text = ' '.join(text)
elif not text and args.tf:
    text = args.tf.read()
elif not text and not args.tf:
    text = ''

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
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    return msg

def send(send_from, send_to, username, password, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(send_from, send_to, msg if type(msg) == str else msg.as_string())
    server.quit()


msg = multipart(send_from, send_to, subject, text, files) 

send(send_from, send_to, username, password, msg)
