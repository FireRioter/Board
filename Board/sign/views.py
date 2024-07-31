from board.models import CustomUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm

from django.shortcuts import render
from django.views.generic import UpdateView


class ConfirmUser(UpdateView):
    model = CustomUser
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = CustomUser.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'account/invalid_code.html')
            return render(self.request, 'account/email_confirmation_signup_messege')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})