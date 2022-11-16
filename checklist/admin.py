from django.contrib import admin

# Register your models here.

from .models import AntesInicisaoC, AntesUsuarioSSC, Paciente, Cirurgia, SalaEsperaCC
# ,SalaEsperaCC, AntesInicisaoC, AntesUsuarioSSC

admin.site.register(Paciente)
admin.site.register(Cirurgia)
admin.site.register(SalaEsperaCC)
admin.site.register(AntesInicisaoC)
admin.site.register(AntesUsuarioSSC)
# AntesInicisaoC
# AntesUsuarioSSC
