from django.views.generic import CreateView
from TimeOffRequest.forms import TimeOffRequestForm
from TimeOffRequest.models import time_off_request_model


class TimeOffRequestView(CreateView):
    model = TimeOffRequestModel
    form_class = TimeOffRequestForm
    template_name = 'TimeOffRequest.html'
    success_url = 'Home.html'  # Specify the URL to redirect to after successful form submission

    def form_valid(self, form):
        # Additional logic can be added here before saving the form
        # For example, you might want to associate the request with the logged-in user
        form.instance.employee_id = self.request.user.employee.employee_id
        return super().form_valid(form)
