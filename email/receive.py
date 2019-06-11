import smtplib
import time
import imaplib
import email

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "bnp.supplier" + ORG_EMAIL
FROM_PWD    = "!Test1337"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        #typ, data = conn.search(None,'(UNSEEN SUBJECT "%s")' % subject)

        type, data = mail.search(None, '(UNSEEN)') # 'All', '(UNSEEN SUBJECT "%s")' % subject
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(943,first_email_id, -1):
            typ, data = mail.fetch(str(i), '(RFC822)' )
            print("status:", typ)
            #typ, data = conn.store(num,'-FLAGS','\\Seen')
            msg = email.message_from_string(data[0][1].decode("utf-8"))
            print(msg)

    except Exception as e:
        print("Exception:", str(e))

read_email_from_gmail()
