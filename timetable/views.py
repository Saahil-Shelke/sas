# from django.http import HttpResponse, HttpResponseRedirect
# from django.views import View
from django.shortcuts import render
# Create your views here.



def createTT(request):
    context = {
        'title': 'Timetable',
        'page': 'createTT',
    }
    return render(request, 'timetable/tt.html', context)

def updateTT(request):
    context = {
        'title': 'Timetable',
        'page': 'updateTT',
    }
    return render(request, 'timetable/tt.html', context)