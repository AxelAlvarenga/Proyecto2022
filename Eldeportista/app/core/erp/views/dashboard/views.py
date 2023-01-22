
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin




class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'templates/dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['panel'] = 'Panel de administrador'
        return contex
