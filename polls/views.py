from django.http import HttpResponse

def index(req):
    return HttpResponse("You are at the polls index")
