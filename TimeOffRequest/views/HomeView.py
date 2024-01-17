from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from TimeOffRequest.models import TimeOffRequestModel  # Import your TimeOffRequestModel

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve time-off requests from the database
        time_off_requests = TimeOffRequestModel.objects.all()
        context['time_off_requests'] = time_off_requests
        return context