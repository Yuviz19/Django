from django.shortcuts import render


def main_app(request):
    return render(request, "myapp/my_app.html")
