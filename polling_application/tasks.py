from celery import Celery
import time
import smtplib

from django.http import HttpResponse
app =Celery('tasks',broker='redis://localhost:6379/0')

@app.task
def sendMail(email,roleapplied):

	try:
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login('vamsi7632@gmail.com','lfvralhoakjbdwgb')
		sub = "Subject for the notification email"
		body = "Body of the email notification"
		notification_message = f"Subject:{sub}\n{body}"
		time.sleep(5)
		server.sendmail('vamsi7632@gmail.com',email,"Hello Whatsapp")
		server.quit()
		return HttpResponse("Mail Sent Successfully")
	except Exception as e:
		return e 