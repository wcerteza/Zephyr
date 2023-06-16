from django.shortcuts import render


def stream(request):
    return render(request, "stream.html")
