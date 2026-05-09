from secrets import token_hex

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}{reverse('users:confirm_email', kwargs={'token': token})}"
        send_mail(
            subject="Подтверждение регистрации",
            message=f"Для подтверждения регистрации перейдите по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class LogoutConfirmView(LoginRequiredMixin, TemplateView):
    template_name = "users/logout.html"


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))



