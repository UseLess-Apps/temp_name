from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404


from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, "jobs/index.html", context)


def job_info(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, "jobs/job.html", {'job': job})
