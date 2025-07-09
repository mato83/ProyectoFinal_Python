
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')  # O la página que quieras, por ejemplo, 'inicio'
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
