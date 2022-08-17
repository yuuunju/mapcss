from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request, 'second.html')

def home(request):
    return render(request, 'first.html')
