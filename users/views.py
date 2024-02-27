from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """Logs the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('news_content:index'))


def register(request):
    """Registers and logs in a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid:
            try:
                new_user = form.save()
                #Authenticates the new user
                authenticated_user = authenticate(username=new_user.username,
                        password=request.POST['password1'])
                #Logs in the authenticated user, redirect to homepage
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('news_content:index'))
            except ValueError as e:
                # Handle validation errors
                if 'username' in str(e):
                    form.add_error('username', str(e))
                if 'password' in str(e):
                    form.add_error('password1', str(e))

    context = {'form': form}
    return render(request, 'users/register.html', context)
