from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redirect to the login page if the user is not authenticated
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the user object to the template
        return context