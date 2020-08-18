from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the scraper index.")


def new_view(request):
    return HttpResponse("<b>This is a new view >:)))</b>")