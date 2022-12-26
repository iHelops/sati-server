from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


class MailService:
    def __init__(self):
        self.sender_address = os.environ.get("SENDER_ADDR")
        self.sender_pass = os.environ.get("SENDER_PASS")
        self.smtp_port = int(os.environ.get("SMTP_PORT"))
        self.smtp_server = os.environ.get("SMTP_HOST")

    def _send_mail(self, receiver: str, subject: str, content: str, content_type: str = 'plain'):
        message = MIMEMultipart("alternative")
        message['From'] = self.sender_address
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(content, content_type))

        session = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
        session.login(self.sender_address, self.sender_pass)
        text = message.as_string()
        session.sendmail(self.sender_address, receiver, text)
        session.quit()

    def send_activation_mail(self, receiver, key):
        env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
        template = env.get_template('./service/activation.html')
        html = template.render(
            link=f'{os.environ.get("API_URL")}/api/user/activate/{key}'
        )

        self._send_mail(receiver=receiver, subject='Активация аккаунта Sati', content=html, content_type='html')
