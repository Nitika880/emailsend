import mimetypes
import smtplib,ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from bs4 import BeautifulSoup as BS
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender_email = "hiring@visiontrek.in"
sender_name = "Nitika"
receiver_email = "hl433976@gmail.com"
receiver_name = 'Nitin'
password = "hiring$10121G"

email_html = open('im.html')
email_body = email_html.read()
filename = 'download.jpg'


print("sending....")
msg = MIMEMultipart()
msg['To'] = formataddr((receiver_name,receiver_email))
msg['From'] = formataddr((sender_name,sender_email))
msg['Subject'] = "To Special idiot :  " + receiver_name
msg.attach(MIMEText(email_body,'html'))
try:
    with open(filename,'rb') as attachment:
        part = MIMEBase("application","octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition",
                    f'attachment;filename= {filename}',)
    msg.attach(part)
except Exception as e:
    print("no attachment")
try:
    server = smtplib.SMTP('mail.eoutlooks.com',587)
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,msg.as_string())
    print("email sent")
except Exception as e:
    print(e)
finally:
    print("closin")
    server.quit()