import datetime
import random
from string import digits

from allauth.account.forms import SignupForm

from django.conf import settings
from django.core.mail import send_mail


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(random.sample(digits, 6))
        user.code = code
        user.save()

        sending_time = datetime.datetime.now().replace(microsecond=0)

        send_mail(
            subject=f'Activation code [{sending_time}]',
            message=f'Your activation code: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )

        return user