from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Register, Pdf, Contact


# Create your views here.
def Homepage(request):
    return render(request, 'quantum/first page.html', {'title': 'Aktu Quantum'})


def pdf_stock(request):
    var = Pdf.objects.all()
    return render(request, 'quantum/pdf_stock.html', {'var': var, 'title': 'pdf'})


def signup(request):
    return render(request, 'quantum/reg-login.html', {'title': 'Sign up form'})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['re_pass']

        if (username and name and email and pass2 and pass1) != '':
            if pass1 == pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=pass1, email=email)
                    user.save()
                    regs = Register(Username=username, Email=email, Password=pass1, Name=name)
                    regs.save()
                    return redirect('login')
            else:
                messages.info(request, 'password not matching')
                return redirect('register')
        else:
            messages.info(request, 'Please fill all the required fields')
            return redirect('register')
    else:
        return render(request, 'quantum/reg-login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username_sign_in']
        password = request.POST['pass_sign_in']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('pdf_stock')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'quantum/signin.html', {'title': 'login form'})


def contact(request):
    title = {'title': 'contact'}
    if request.method == 'POST':
        Your_name = request.POST.get('name')
        Your_email = request.POST.get('email')
        Your_subject = request.POST.get('subject')
        Your_message = request.POST.get('message')

        var_contact = Contact(Name=Your_name, Email_id=Your_email, Subject=Your_subject, Message=Your_message)
        if Your_name == '' or Your_message == '' or Your_subject == '' or Your_email == '':
            return render(request, 'quantum/contact.html')
        else:
            var_contact.save()
            return render(request, 'quantum/thanks.html')
    else:
        return render(request, 'quantum/contact.html', title)


def logout(request):
    auth.logout(request)
    return redirect('Homepage')
