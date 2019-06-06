from django.shortcuts import render
from .models import Job
# Create your views here.
def rj(request):
    jobs = Job.objects
    return render(request, 'jobs/rj.html', {'jobs':jobs})
