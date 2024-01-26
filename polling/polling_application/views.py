import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render
from django.http import HttpResponse
from polling_application.models import *
import requests
import smtplib
from django.core.mail import send_mail
from celery import Celery
import time
# Create your views here.
uname=''
email1 =" "
supermail=''

def home(request):
	return render(request, 'login.html')
def submitVote(request):
    pass


def loginpage(request):
	if(request.POST.get('username')):
		uname = request.POST.get("username")
		pword = request.POST.get("password")
		email1=uname
		supermail=email1
		print(supermail)
		# print("values received",uname,pword)
		list_of_emails = logindetails.objects.all().values_list('email',flat=True)
		if email1 in list_of_emails:
			if pword == logindetails.objects.get(email=email1).password:
				roless = requests.get('http://127.0.0.1/Get_Roles').json

				return render(request,'index.html',{'roless':roless}) # login successfully
			else :
				return render(request,'login.html',{'error':'wrong credentials'})
		else :

			return render(request,'login.html',{'error':'Details Not Found'})
	else:
		return render(request,'login.html')

def regsubmit(request):
	uname = request.POST.get('name')
	password = request.POST.get('password')
	email1 = request.POST.get('email')
	list_of_emails= logindetails.objects.all().values_list('email',flat=True)
	if email1 in list_of_emails:
		return render(request,'login.html',{'error':'Email already registered'})
	else:
		logindetails( username=uname, password=password, email=email1 ).save()
		return HttpResponse("<h1>Page found</h1>")
	

def homee(request):
	roless = requests.get('http://127.0.0.1/Get_Roles').json
	return render(request,'index.html',{'roless':roless})

def Submit_btn(request):
	# name = request.POST.get('Rolename')
	# global email1
	# print('---->',email1)email = request.GET.get('emailid')
	email = request.POST.get("mail")
	print(email)
	status = sendMail(email,"data")
	return HttpResponse(status)


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
		server.sendmail('vamsi7632@gmail.com',email,"Hello Whatsapp")
		server.quit()
		return HttpResponse("Mail Sent Successfully")
	except Exception as e:
		return e 


# def Submit_btn(request):
#     if request.method == 'POST':
#         email1 = request.POST.get('username')

#         try:
#             # Setup email server
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.ehlo()
#             server.starttls()
#             server.ehlo()

#             # Login to email server (replace with your email and password)
#             server.login('vamsi7632@gmailcom', 'sjsa icxt bsbb ekwe')

#             # Compose email
#             subject = "Your application received Successfully"
#             body = "Your email body content here"
#             msg = MIMEMultipart()
#             msg['From'] = 'vamsi7632@gmail.com'
#             msg['To'] = 'gurramvamsikrishna1@gmail.com'
#             msg['Subject'] = subject
#             msg.attach(MIMEText(body, 'plain'))

#             # Send email
#             server.sendmail('vamsi7632@gmail.com','gurramvamsikrishna1@gmail.com', msg.as_string())

#             # Quit server
#             server.quit()

#             return HttpResponse("Mail Sent Successfully")
#         except Exception as e:
#             return HttpResponse(f"Error: {e}")
#     else:
#         return HttpResponse("Invalid Request")




	# return HttpResponse("<h1>Page found</h1>")

'''
def Submit_btn(request):
    status = sendMail('gurramvamsikrishna1@gmail.com')
    return HttpResponse(status)

def sendMail(receiver):
    try:
        send_mail(
            'Subject: You have received a notification',
            'Message body here',
            'gurramvamsikrishna1@gmail.com',
            [receiver],
            fail_silently=False,
        )
        return "Mail sent successfully!"
    except Exception as e:
        return str(e)
		'''