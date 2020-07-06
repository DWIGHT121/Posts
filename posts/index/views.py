from django.shortcuts import render


def index(self):
    return render(request, 'index.html')