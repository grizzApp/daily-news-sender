import html
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib 
from app.config import EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT
from app.body import generate_email_body

def text_cleaner(articles):
    fields = ['title', 'description', 'content']
    cleaned_articles = []

    for article in articles:
        article = {
            key: html.unescape(value) if key in fields and isinstance(value, str) else value
            for key, value in article.items()
        }

        if 'content' in article and article['content']:
            article['content'] = re.sub(r'\[\+\d+\s+chars\]', '', article['content'])

        cleaned_articles.append(article)

    return cleaned_articles

def email_sender(articles):
    body = generate_email_body(articles)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Daily Tech News Update - Python'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT
    
    html_part = MIMEText(body, 'html')
    msg.attach(html_part)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
            server.send_message(msg)
    except Exception as exc:
        print(f"Something wrong: {exc}")
    else:
        print("Email sent successfully.")