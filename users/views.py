from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegForm, StaffUpdateForm, DberUpdateForm, EmailChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            messages.success(request, f'Account created successfully for {username}')

            Profile.objects.get_or_create(user = request.user)

            user = authenticate(username = username, password = pwd)
            login(request, user)

            return redirect('home')
    else :
        form = RegForm()

    return render(request, 'users/register.html', {'form' : form})

@login_required
def update_staff(request):

    if request.method == 'POST':
        p_form = StaffUpdateForm(request.POST,
                                    instance=request.user.profile)

        if p_form.is_valid():
            request.user.profile.save()
            p_form.save()

    else:
        p_form = StaffUpdateForm(instance=request.user.profile)

    context = {
        'p_form' : p_form
    }
    return render(request, 'users/update_staff.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })

@login_required
def change_email(request):

    user = request.user
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            form.save()

            user.email = form.cleaned_data['email']
            user.save()

            return redirect('change_email')

    else:
        form = EmailChangeForm()

    return render(request, 'users/change_email.html', {
        'form': form
    })
# Create your views here.
