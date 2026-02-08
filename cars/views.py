print("CARREGOU cars.views CORRETO")

from django.shortcuts import render


def cars_view(request):
    return render(
        request,
         'cars.html',
         {'cars': {'model': 'Gol 1000 93'}}    
    )