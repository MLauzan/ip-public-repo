from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from main.settings import EMAIL_HOST_USER

def login_user(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, "Credenciales inválidas")
        return redirect('login')
        
def create_user(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('mail')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
       
        if not (username and password and email):
            messages.error(request, "Los campos username, password y email son obligatorios")
            return redirect("create_page")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya se encuentra registrado")
            return redirect("create_page")
        
        try:
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            subject = 'Credenciales de acceso'
            message= f'Usuario: {username}, contraseña: {password}'
            recipient = email.strip()
            
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            
            messages.success(request, f"Usuario creado con éxito, enviamos tus credenciales a {email}")
            return redirect("create_page")
        except Exception as e:
            messages.error(request, f"No se pudo crear el usuario: {str(e)}")
            return redirect("create_page")
      