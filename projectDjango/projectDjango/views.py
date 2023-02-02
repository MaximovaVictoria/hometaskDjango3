from django.shortcuts import render

def main(request):
    return render(request, 'Inputbutton.html')


def addtext(request):
    user_text = request.GET["usertext"]
    return render(request, "Pucturetable.html", {"usertext": user_text})
