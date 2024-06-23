from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, "Credenciales inválidas")
        return redirect('login')