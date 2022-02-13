from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SurveysForm
from .models import Surveys


class SurveysDeleteView(LoginRequiredMixin, DeleteView):
    model = Surveys
    success_url = '/matcher/surveys'
    template_name = 'surveys/surveys_delete.html'
    login_url = "/login"

class SurveysUpdateView(LoginRequiredMixin, UpdateView):
    model = Surveys
    success_url = '/matcher/surveys'
    form_class = Surveys
    login_url = "/login"

class SurveysCreateView(LoginRequiredMixin, CreateView):
    model = Surveys
    success_url = '/matcher/surveys'
    form_class = Surveys
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
class SurveysListView(LoginRequiredMixin, ListView):
    model = Surveys
    context_object_name = "surveys"
    template_name = "surveys/surveys_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.surveys.all()

class SurveysDetailView(LoginRequiredMixin, DetailView):
    model = Surveys
    context_object_name = "survey"
    login_url = "/login"