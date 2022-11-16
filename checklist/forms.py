
from sqlite3 import Date
from django import forms
from .models import AntesInicisaoC, AntesUsuarioSSC, Cirurgia, Paciente, SalaEsperaCC
from django.forms import DateInput, ModelForm


class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'
        labels = {'nome': 'Nome', 'dataNascimento': 'Data Nascimento',
                  'nomeMae': 'Nome da Mãe', 'prontuario': 'Prontuário'}

        widgets = {'dataNascimento': DateInput(attrs={'type': 'date'})}


class CirurgiaForm(ModelForm):
    class Meta:
        model = Cirurgia
        fields = '__all__'


class SalaEsperaCCForm(ModelForm):
    class Meta:
        model = SalaEsperaCC
        fields = '__all__'


class AntesInicisaoCForm(ModelForm):
    class Meta:
        model = AntesInicisaoC
        fields = '__all__'


class AntesUsuarioSSCForm(ModelForm):
    class Meta:
        model = AntesUsuarioSSC
        fields = '__all__'
