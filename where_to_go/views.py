from django.shortcuts import render

def show_places(requests):
    return render(requests, 'index.html')
