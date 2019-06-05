from django.shortcuts import render

# Create your views here.
def rj(request):
    return render(request, 'jobs/rj.html')
