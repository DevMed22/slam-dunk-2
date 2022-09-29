from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    success_url = reverse_lazy ('login')
    form_class = UserCreationForm
    template_name = 'registration/signup.html'