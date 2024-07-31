from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from allauth.account.views import SignupView
from allauth.account.forms import LoginForm


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

class CustomSignupView(SignupView):
    # here we add some context to the already existing context
    def get_context_data(self, **kwargs):
        # we get context data from original view
        context = super(CustomSignupView,
                        self).get_context_data(**kwargs)
        context['login_form'] = LoginForm() # add form to context
        return context