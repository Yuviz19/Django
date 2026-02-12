from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html',{"rooms":rooms})

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {"rooms": room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm
    if request.method == "POST":
        form = RoomForm(request.POST) # so we are passing the form input data into the RoomForm
        if form.is_valid(): # and if that data is valid, we go ahead and save it
            form.save()
            return redirect('home') # direct reference via name

    context = {"Form": form}
    return render(request, 'base/room_form.html', context)
