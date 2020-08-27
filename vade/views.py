from django.shortcuts import render
from .forms import EmailForm
from .models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def staff_test(user):
    return user.is_staff


@user_passes_test(staff_test)
def email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            users = User.objects.all()
            for user in users:
                subject = cd['title']
                message = cd['mail']
                send_mail(subject, message, 'admin@vade.com',
                          [user.email])

    else:
        form = EmailForm()

    return render(request, 'vade/sendmail.html', {'form': form})
