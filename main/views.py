from django.shortcuts import render

def index(request):
    ''' ...Logic...'''
    return render(request, 'index.html')
