from django import forms

class EquipoForm(forms.Form):
    EQUIPOS = (
                (1, "RED"),
                (2, "TELECONTROL"),
                (3, "PROTECCION") ,
     )
    equipo = forms.MultipleChoiceField(label='Equipo a cargar', choices=EQUIPOS, required=True, )
    nombre = forms.CharField(label='Nombre', max_length=50, required=True)
    descripcion = forms.CharField(label='Descripción', max_length=50, required=True)
    nivel_tension = forms.CharField(label='Nivel de Tensión', max_length=50, required=True)
    edificio = forms.CharField(label='Edificio', max_length=50, required=True)
    gabinete = forms.CharField(label='Gabinete', max_length=50, required=True)
    ip = forms.CharField(label='Dirección IP', max_length=50, required=True)
    mask = forms.CharField(label='Máscara de Subred', max_length=50, required=True)
    defGw = forms.CharField(label='Default Gateway', max_length=50)

class BusquedaForm(forms.Form):
    EQUIPOS = (
                (1, "RED"),
                (2, "TELECONTROL"),
                (3, "PROTECCION") ,
     )
    equipo = forms.MultipleChoiceField(label='Equipo a buscar', choices=EQUIPOS, required=True, )
    busqueda = forms.CharField(max_length=50, required=True)
