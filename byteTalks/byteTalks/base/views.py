from django.shortcuts import render

rooms = [
    {"id": 1, "name": "Learn Python Together"},
    {"id": 2, "name": "Designn With Me"},
    {"id": 3, "name": "Frontend Developers"}
]

def home(request):
    return render(request, 'base/home.html',{"rooms":rooms})

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {"rooms": room}
    return render(request, 'base/room.html', context)
