from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import UserRegisterForm, UserUpdateForm, ProfilUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Der Account für {username} wurde erstellt. Sie können sich nun einloggen!')
            return redirect('login')## Gibt eine HttpResponseRedirect an die entsprechende URL für die übergebenen Argumente zurück
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) ## render (), um die HttpResponse zu erstellen, die an den Browser zurückgesendet wird

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilUpdateForm(request.POST, 
                                  request.FILES, 
                                  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Der Account wurde aktualisiert.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)




