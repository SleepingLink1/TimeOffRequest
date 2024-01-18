from django.shortcuts import render, redirect
from TimeOffRequest.forms import LoginForm


def account_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process the login data (authenticate the user, etc.)
            # Redirect to the appropriate page on successful login
            return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'accountLogin.html', {'form': form})
