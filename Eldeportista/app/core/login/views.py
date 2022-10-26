from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login


class LoginFormView(FormView):
    form_class: AuthenticationForm
    template_name='login.html'
    success_url = reverse_lazy('erp:producto_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self,form):
        login(self.request , form.get_user())
        
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion '
        
        return context

