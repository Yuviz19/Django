from django.shortcuts import render
from .models import Room
# rooms = [
#     {"id": 1, "name": "Learn Python Together"},
#     {"id": 2, "name": "Designn With Me"},
#     {"id": 3, "name": "Frontend Developers"}
# ]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html',{"rooms":rooms})

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {"rooms": room}
    return render(request, 'base/room.html', context)
