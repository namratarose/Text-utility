# This file is not created by default. This is created by the user
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.GET.get("text", "default")
    print(djtext)
    removepunc = request.GET.get("removepunc", "off")
    fullcaps = request.GET.get("fullcaps", "off")
    newlineremover = request.GET.get("newlineremover", "off")
    extraspaceremover = request.GET.get("extraspaceremover", "off")
    charcount = request.GET.get("charcount", "off")

    if removepunc == "on":
        punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Punctuations removed", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Fully Capitalized", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed + char
        params = {"purpose": "New line removed", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        analyzed = 0
        for char in djtext:
            analyzed += 1
        params = {"purpose": "Chararcter counted", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("Error")


# def capfirst(request):
#     return HttpResponse("Captalize first letter <a href='/'>back</a>")
# def newlineremove(request):
#     return HttpResponse("New line remover <a href='/'>back</a>")
# def spaceremove(request):
#     return HttpResponse("Spacerempver <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("Char count <a href='/'>back</a>")
