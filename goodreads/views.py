from django.http import HttpResponse


def landing_page(request):
    return HttpResponse(f"<h1>Django is working.</h1>")