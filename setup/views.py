from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import SignUpForm


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_invalid(self, form):
        error_list = []
        for field, errors in form.errors.items():
            for error in errors:
                if field == '__all__':
                    error_list.append(error)
                else:
                    field_obj = form.fields.get(field)
                    label = field_obj.label if (field_obj and field_obj.label) else field.title()
                    error_list.append(f"{label}: {error}")

        if error_list:
            if len(error_list) == 1:
                messages.error(self.request, error_list[0])
            else:
                formatted_errors = "<br>".join(f"• {e}" for e in error_list)
                messages.error(self.request, f"<strong>Erros no cadastro:</strong><br>{formatted_errors}")

        return super().form_invalid(form)
    
    success_message = "Conta criada com sucesso! Você já pode fazer login."


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f"Bem-vindo, {user.username}!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Nome de usuário ou senha inválidos. Tente novamente.")
        return super().form_invalid(form)