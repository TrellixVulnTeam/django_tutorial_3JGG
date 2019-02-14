from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    """
    UserCreationForm: creates a form for users to input information


    register.html

    in the registers.html file, you can extend files from other apps
    template folders

    register.html is using a CSRF token (Cross Reference forgery token) will
    protect our site from certain attacks

    form variable will create form. using "as_p" method will add p tags, making
    the page look more presentable

    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.clean_data.get('username')

    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
