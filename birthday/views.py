# views.py
from django.shortcuts import render

def birthday_message(request):
    nombre_destinatario = "Maythe"  # Nombre de la persona a quien le estás deseando un feliz cumpleaños
    tu_nombre = "Alexander"  # Tu nombre
    gif_url = "/img/bday-875.gif"  # Reemplaza esta URL con la ruta de tu GIF en el proyecto

    context = {
        'Maythe': nombre_destinatario,
        'Alexander': tu_nombre,
        '/img/bday-875.gif': gif_url,
    }

    return render(request, 'birthday.html', context)


