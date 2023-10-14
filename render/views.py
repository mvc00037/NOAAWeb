# Create your views here.
from django.shortcuts import render
import requests, datetime, pytz
from .models import imagenApt

#def index(request):
#    imagenes = imagenApt.objects.all()
#    context=  { "imagenes":imagenes}
#    return render(request, 'render/index.html', context)

def index(request):
    return render(request, 'render/index.html', {})

def prediction(request,idSat ):
    sat_data = []
    url = 'https://api.n2yo.com/rest/v1/satellite/radiopasses/{}/36.76/-3.44/500/10/40/&apiKey=8LTCAG-YNFHC9-K96TEM-4WW6'

    r = requests.get(url.format(idSat)).json()
    iterator = r['info']['passescount']

    for i in range(iterator):
        satResponse = {
            'satname': r['info']['satname'],
            'satId': r['info']['satid'],
            "transactionscount": r['info']['transactionscount'],
            'startAz': r['passes'][i]['startAz'],
            'endAz': r['passes'][i]['endAz'],
            'maxEl' :  r['passes'][i]['maxEl'],
            "startUTC": datetime.datetime.fromtimestamp(r['passes'][i]['startUTC'],tz= pytz.timezone('Europe/Madrid')).strftime('%Y-%m-%d %H:%M:%S'),
            "endUTC": r['passes'][i]['endUTC'],
            "maxEl": r['passes'][i]['maxEl'],
        }
        sat_data.append(satResponse)
    context = {'sat_data': sat_data}

    return render(request, 'render/predictionTable.html', context)