from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class TelmeView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data:',
            'form': HelloForm()
        }

    def get(self, request):
        return render(request, 'telme/index.html', self.params)
    
    def post(self, request):
        ch = request.POST.getlist('choice')
        self.params['result'] = 'selected: ' + str(ch) + '.'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'telme/index.html', self.params)
