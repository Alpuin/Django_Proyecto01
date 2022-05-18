from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def inicio(request):

    return HttpResponse("Front page")


def hola_mundo(request):

    return HttpResponse("Hello world")


def segunda_vista(request):

    return HttpResponse("<br><br>This is a second view")


def dia_hoy(request):

    dia = datetime.now()

    documento_texto = f"Today is: <br> {dia}"

    return HttpResponse(documento_texto)


def mis_datos(self, nombre, edad):

    documento_texto = f"Data<br><br>My name is: {nombre} <br>My age is: {edad}"

    return HttpResponse(documento_texto)


def calcular_anio_nacimiento(self, anio):

    anio_actual = datetime.now().year

    nacimiento = anio_actual - int(anio)

    return HttpResponse(f"<br>My birth year is: {nacimiento}")


def calcular_edad(self, fecha_nacimiento):

    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

    print(type(fecha_nacimiento))

    intervalo_tiempo = datetime.now() - fecha_nacimiento

    dias_por_anio = 365.25

    http_response = '''
    <br><br>
    I'm {years} years, {months} months, {days} days old.
    '''.format(
        years = int(intervalo_tiempo.days // dias_por_anio),
        months = int((intervalo_tiempo.days % dias_por_anio) // 30),
        days = int((intervalo_tiempo.days % dias_por_anio) % 30),
    )

    return HttpResponse(http_response)


def probando_template(self):

    miHtml = open ("C:/Users/Matt/Documents/CoderHouse/Python/CLASS_17_DJANGO_I/Proyecto01/Proyecto01/Templates/Template.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)