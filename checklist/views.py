from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView

from .models import Paciente, Cirurgia
from .forms import PacienteForm, CirurgiaForm, SalaEsperaCCForm, AntesInicisaoCForm, AntesUsuarioSSCForm


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


###################
class PacienteCreate(CreateView):
    form_class = PacienteForm

    template_name = 'forms/form01.html'

    success_url = reverse_lazy('index')


class CirurgiaCreate(CreateView):
    form_class = CirurgiaForm

    template_name = 'forms/form02.html'

    success_url = reverse_lazy('index')


class SalaEsperaCCCreate(CreateView):
    form_class = SalaEsperaCCForm

    template_name = 'forms/form03.html'

    success_url = reverse_lazy('index')


class AntesInicisaoCCreate(CreateView):
    form_class = AntesInicisaoCForm

    template_name = 'forms/form04.html'

    success_url = reverse_lazy('index')


class AntesUsuarioSSCCreate(CreateView):
    form_class = AntesUsuarioSSCForm
    fields = '__all__'

    template_name = 'forms/form05.html'

    success_url = reverse_lazy('index')


############## UPDATE##############################


class PacienteUpdate(UpdateView):
    model = Paciente

    fields = '__all__'
    template_name = 'forms/form01.html'

    success_url = reverse_lazy('index')


class CirurgiaUpdate(UpdateView):
    model = Cirurgia
    fields = '__all__'
    template_name = 'forms/form02.html'

    success_url = reverse_lazy('index')


class SalaEsperaCCUpdate(UpdateView):
    form_class = SalaEsperaCCForm

    template_name = 'forms/form03.html'

    success_url = reverse_lazy('index')


class AntesInicisaoCUpdate(UpdateView):
    form_class = AntesInicisaoCForm
    template_name = 'forms/form04.html'

    success_url = reverse_lazy('index')


class AntesUsuarioSSCUpdate(UpdateView):
    form_class = AntesUsuarioSSCForm

    template_name = 'forms/form05.html'

    success_url = reverse_lazy('index')
