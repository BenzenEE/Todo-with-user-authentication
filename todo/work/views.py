import email
import re
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import logout as lout
from django.contrib import messages
from .forms import Tform
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.

val = None

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if Test.objects.filter(email=email).exists():
            messages.info(request, 'Email already exist, Try using different email!!')
            return redirect('/')
        user = Test(name=name,email=email,password=password)
        user.save()
        messages.info(request, 'Registered successfully!!')
        mydict={'username':name}
        html_template = 'register_email.html'
        html_message = render_to_string(html_template, context=mydict)
        subject = 'Welcome to TODO list Verse'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        # temp = render_to_string('send_email.html', {'name':name})
        # ob = EmailMessage(
        #     'Thanks for registering TODO Verse',
        #     temp,
        #     settings.EMAIL_HOST_USER,
        #     [email],
        # )
        # ob.fail_silently=False
        # ob.send()

    return redirect('/')

def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            
            user = Test.objects.get(email=email,password=password)
            request.session['email']=user.email
            request.session['name']=user.name
            global val
            val = True
            return redirect('home')
        
        except Test.DoesNotExist as e:
            messages.info(request, 'Password or Email not exist!!')
    return redirect('/')


def home(request):
    global val
    if val == True:
        print(request.session['email'])
        tasks = Tlist.objects.filter(fok = request.session['email'])
        return render(request,'home.html',context={'tasks':tasks})
    else:
        return redirect('login')
    

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        #status = request.POST['status']
        email = request.session['email']
        temp = Test.objects.get(email=request.session['email'])
        #ob = Tlist.objects.create(title=title,status=status,fok=temp)
        ob = Tlist.objects.create(title=title,fok=temp)
        ob.save()
        return redirect('home')
    return render(request,'home.html')
    
def delete_task(request, id):
    Tlist.objects.get(pk = id).delete()
    return redirect('home')

def change_status(request, id, status):
    temp = Tlist.objects.get(pk = id)
    if(status == 'Pending'):
        temp.status = 'Complete'
        temp.save()
    else:
        temp.status = 'Pending'
        temp.save()
    return redirect('home')

def logout(request):
    lout(request)
    global val
    val = False
    return redirect('login')

def edit_task(request, id):
    global val
    if val == True:
        ob = Tlist.objects.get(pk = id)
        return render(request, 'edit.html', context={'ob':ob})
    else:
        return redirect('login')

def update_task(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        ob = Tlist.objects.get(pk = id)
        ob.title = title
        ob.save()
        return redirect('home')