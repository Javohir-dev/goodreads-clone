from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserCreateForm, UserLoginForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, "users/register.html", context)
    
    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect("users:login")
        else:
            context = {
                'form': create_form
            }
            return render(request, "users/register.html", context)



class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        return render(request, "users/login.html", {'login_form': login_form})
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect('landing_page')
        else:
            return render(request, "users/login.html", {'login_form': login_form})

