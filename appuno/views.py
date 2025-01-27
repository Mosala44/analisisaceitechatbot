from django.shortcuts import render

# Create your views here.


def chatbot(req):
    return render(req, 'index.html')
def resumen(req):
    return render(req, 'resumen.html')