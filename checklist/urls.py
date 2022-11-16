from django.urls import path


from .views import AntesInicisaoCCreate, AntesInicisaoCUpdate, AntesUsuarioSSCCreate, AntesUsuarioSSCUpdate, CirurgiaCreate, CirurgiaUpdate, IndexView, PacienteCreate, PacienteUpdate, SalaEsperaCCCreate, SalaEsperaCCUpdate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('cadastrar/', BaseView.as_view(), name='base'),
    # Create
    path('Create/Paciente/',
         PacienteCreate.as_view(), name='CreatePaciente'),
    path('Create/Cirurgia/',
         CirurgiaCreate.as_view(), name='CreateCirurgia'),
    path('Create/SalaEsperaCC/',
         SalaEsperaCCCreate.as_view(), name='CreateSalaEsperaCC'),
    path('Create/AntesInicisaoC/',
         AntesInicisaoCCreate.as_view(), name='CreateAntesInicisaoC'),
    path('Create/AntesUsuarioSSC/',
         AntesUsuarioSSCCreate.as_view(), name='CreateAntesUsuarioSSC'),

    # Upddate

    path('Update/Paciente/<int:pk>',
         PacienteUpdate.as_view(), name='UpdatePaciente'),
    path('Update/Cirurgia/<int:pk>',
         CirurgiaUpdate.as_view(), name='UpdateCirurgia'),
    path('Update/SalaEsperaCC/<int:pk>',
         SalaEsperaCCUpdate.as_view(), name='UpdateSalaEsperaCC'),
    path('Update/AntesInicisaoC/<int:pk>',
         AntesInicisaoCUpdate.as_view(), name='UpdateAntesInicisaoC'),
    path('Update/AntesUsuarioSSC/<int:pk>',
         AntesUsuarioSSCUpdate.as_view(), name='UpdateAntesUsuarioSSC'),
]
