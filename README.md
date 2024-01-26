<h1>Introduction</h1>
<p>This is an application developed using python's one of the best framework "django", this applicationn is a polling application which will get some of the details from another application this link will direscts you to that repository where you can download it[https://github.com/VamsiKrishnaGurram/Django_Api.git], in short this is a polling website application developed for hiring prpose</p>
<div><h1>software Requirements</h1>
<h4>python </h4>
<h4>Django along with other modules required to run application</h4>
<h5>Below are the some Imports i made</h5>
import email from email.mime.multipart<br>
import from email.mime.text import MIMEText<br>
from django.shortcuts import render<br>
from django.http import HttpResponse<br>
from polling_application.models import *<br>
import requests<br>
import smtplib<br>
from django.core.mail import send_mail<br>
from celery import Celery<br>
import time
</div>
<br>
<h1>Notably, the code imports modules from Django, email handling, database models, HTTP requests, SMTP (Simple Mail Transfer Protocol), and Celery for asynchronous task processing.</h1>








