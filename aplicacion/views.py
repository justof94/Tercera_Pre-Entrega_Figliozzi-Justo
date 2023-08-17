from django.shortcuts import render
from .models import *
from .form import *

# Create your views here.
def landing_page(request):
    return render(request, "aplicacion/base.html")

def equiposRed(request):
    contexto = {'equiposRed': EquipoRed.objects.all()}
    return render(request, "aplicacion/equiposRed.html", contexto)

def equiposTelecontrol(request):
    contexto = {'equiposRed': EquipoTelecontrol.objects.all()}
    return render(request, "aplicacion/equiposTelecontrol.html", contexto)

def equiposProteccion(request):
    contexto = {'equiposRed': EquipoProteccion.objects.all()}
    return render(request, "aplicacion/equiposProteccion.html", contexto)

def home(request):
        print(len(request.GET) != 0)
        if request.method == "POST":
            miForm = EquipoForm(request.POST)
            
            if miForm.is_valid():
                equipo_tipo = miForm.cleaned_data.get('equipo')
                equipo_nombre = miForm.cleaned_data.get('nombre')
                equipo_descripcion = miForm.cleaned_data.get('descripcion')
                equipo_nivel_tension = miForm.cleaned_data.get('nivel_tension')
                equipo_edificio = miForm.cleaned_data.get('edificio')
                equipo_gabinete = miForm.cleaned_data.get('gabinete')
                equipo_ip = miForm.cleaned_data.get('ip')
                equipo_mask = miForm.cleaned_data.get('mask')
                equipo_defGw = miForm.cleaned_data.get('defGw')

                if equipo_tipo == ['1']:
                    equipo = EquipoRed(nombre=equipo_nombre,
                                    descripcion=equipo_descripcion,
                                    nivel_tension=equipo_nivel_tension,
                                    edificio=equipo_edificio,
                                    gabinete=equipo_gabinete,
                                    ip=equipo_ip,
                                    mask=equipo_mask,
                                    defGw=equipo_defGw)
                
                elif equipo_tipo == ['2']:
                    equipo = EquipoTelecontrol(nombre=equipo_nombre,
                                    descripcion=equipo_descripcion,
                                    nivel_tension=equipo_nivel_tension,
                                    edificio=equipo_edificio,
                                    gabinete=equipo_gabinete,
                                    ip=equipo_ip,
                                    mask=equipo_mask,
                                    defGw=equipo_defGw)
                            
                elif equipo_tipo == ['3']:
                    equipo = EquipoProteccion(nombre=equipo_nombre,
                                    descripcion=equipo_descripcion,
                                    nivel_tension=equipo_nivel_tension,
                                    edificio=equipo_edificio,
                                    gabinete=equipo_gabinete,
                                    ip=equipo_ip,
                                    mask=equipo_mask,
                                    defGw=equipo_defGw) 
            equipo.save()
            return render(request, 'aplicacion/home.html', {'form': EquipoForm(), 'busqueda': BusquedaForm()})   

                  
        if len(request.GET) != 0:
            print("HOLAHOLAHOLAHOLA")
            miForm = BusquedaForm(request.GET)
            if miForm.is_valid():
                equipo_tipo = miForm.cleaned_data.get('equipo')
                equipo_busqueda = miForm.cleaned_data.get('busqueda')

                if equipo_tipo == ['1']:
                    resultado = EquipoRed.objects.filter(nombre__icontains=equipo_busqueda)
                    contexto = {"equipo": resultado, 'titulo': f'Equipos de Red que tiene como patron "{equipo_busqueda}"'}
                    return render(request, "aplicacion/buscarEquipo.html", contexto)

                if equipo_tipo == ['2']:
                    resultado = EquipoTelecontrol.objects.filter(nombre__icontains=equipo_busqueda)
                    contexto = {"equipo": resultado, 'titulo': f'Equipos de Telecontrol que tiene como patron "{equipo_busqueda}"'}
                    return render(request, "aplicacion/buscarEquipo.html", contexto)

                if equipo_tipo == ['3']:
                    resultado = EquipoProteccion.objects.filter(nombre__icontains=equipo_busqueda)
                    contexto = {"equipo": resultado, 'titulo': f'Equipos de Prtoeccuon que tiene como patron "{equipo_busqueda}"'}
                    return render(request, "aplicacion/buscarEquipo.html", contexto)
            
        else:
            return render(request, 'aplicacion/home.html', {'form': EquipoForm(), 'busqueda': BusquedaForm()})