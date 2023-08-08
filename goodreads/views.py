from django.shortcuts import render


def landing_page(request):
    # print(request.COOKIES['example_cookie'])
    return render(request, "landing.html")