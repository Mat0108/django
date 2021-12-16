from django.shortcuts import render
from django.http import HttpResponse
from listings.models import User
from django.http import HttpResponseRedirect
from .forms import NameForm
# Create your views here.
def user(request):
    users = User.objects.all()

    return render(request,'listings/user.html',context={"user" : user})

def login(request):
    return render(request,'listings/login.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            users = User.objects.all()
            for user in users:
               
                mail_object = User._meta.get_field('mail')
                mail = mail_object.value_from_object(user)
                password_object = User._meta.get_field('password')
                password = password_object.value_from_object(user)
                if (mail == form.cleaned_data.get("mail") and password == form.cleaned_data.get("password")):
                    return HttpResponseRedirect('user/')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('listings/user.html/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'listings/login.html', {'form': form})
def edit_mail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            users = User.objects.all()
            for user in users:
               
                mail_object = User._meta.get_field('mail')
                mail = mail_object.value_from_object(user)
                password_object = User._meta.get_field('password')
                password = password_object.value_from_object(user)
                if (mail == form.cleaned_data.get("mail") and password == form.cleaned_data.get("password")):
                    return HttpResponseRedirect('user/')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('listings/user.html/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'listings/login.html', {'form': form})
