import smtplib

from email.header import Header
from email.mime.text import MIMEText
from http import HTTPStatus

from fastapi import HTTPException

from src.settings import EMAIL_LOGIN, SMTP_HOST, SMTP_PORT, EMAIL_PASSWORD


class EmailService:
    async def send(self, recipients_emails: list[str], msg_text: str):
        msg = MIMEText(f'{msg_text}', 'plain', 'utf-8')
        msg['Subject'] = Header('Важно!!!', 'utf-8')
        msg['From'] = EMAIL_LOGIN
        msg['To'] = ', '.join(recipients_emails)

        s = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)

        try:
            s.starttls()
            s.login(EMAIL_LOGIN, EMAIL_PASSWORD)
            s.sendmail(msg['From'], recipients_emails, msg.as_string())
        except Exception as ex:
            print(ex)
            raise HTTPException(detail="Email service broken", status_code=HTTPStatus.BAD_GATEWAY)
        finally:
            s.quit()
