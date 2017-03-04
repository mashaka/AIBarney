from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from rest_framework.authtoken.models import Token
from app.methods import prepare_user

def get_token(request):
    if request.user:
        prepare_user(user)
        token,_ = Token.objects.get_or_create(user=request.user)
        url = "chatbot://?token=" + token.key
    else:
        url = "chatbot://error"
    response = HttpResponse(url, status=302)
    response['Location'] = url
    return response

@login_required
def get_facebook_token(request):
    q=get_object_or_404(UserSocialAuth,user=request.user,provider='facebook')
    return HttpResponse(str(q.extra_data))

def signup(request):
    return render(request, 'signup.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})
