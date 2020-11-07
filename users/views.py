from django.shortcuts import render, redirect
from django.contrib import messages
from.forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')## Gibt eine HttpResponseRedirect an die entsprechende URL für die übergebenen Argumente zurück
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) ## render (), um die HttpResponse zu erstellen, die an den Browser zurückgesendet wird



