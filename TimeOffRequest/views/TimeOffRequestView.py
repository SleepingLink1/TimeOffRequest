from django.shortcuts import render
from django.views import View
from TimeOffRequest.forms import TimeOffRequestForm
#TODO: create views for different pages and handle errors
class TimeOffRequestView(View):
    template_name = 'time_off_request_form.html'
    def get(self, request, *args, **kwargs):
        form = TimeOffRequestForm()
        context = {'form': form}
        return render(request, self.template_name, context)

