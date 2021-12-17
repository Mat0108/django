from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from listings.models import User
from .forms import NameForm

g_user = None
# Create your views here.
def user(request):
    users = User.objects.all()
    return render(request,'listings/user.html',context={"user" : g_user,"users":users, "bool":False})

def login(request):
    return render(request,'listings/login.html')

def get_name(request):
    global g_user
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
                    g_user = user
                    return render(request, 'listings/user.html', {'form': form,"user":g_user,"users":users,"bool": False})
                    #return render(request,'listings/user.html',context={"user" : g_user,"users":users})
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('listings/user.html/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'listings/login.html', {'form': form})


def modif(request):
    global g_user
    users = User.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form2 = NameForm(request.POST)
        # check whether it's valid:
        if form2.is_valid():
            user = User.objects.get(pk=1)
            user.mail = form2.cleaned_data.get('mail')
            user.save()
            g_user.mail = form2.cleaned_data.get('mail')
            return render(request,'listings/user.html',context={"form": form2,"user":g_user,"bool":False,"users":users})
    # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('listings/user.html/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form2 = NameForm()
        mail_object = User._meta.get_field('mail')
        form2.fields['mail'].initial=g_user.mail
        return render(request,'listings/user.html',context={"form": form2,"user" : g_user,"users":users,'bool':True})
    return render(request,'listings/user.html',context={"form": form2,"user" : g_user,"users":users,'bool':False})
       