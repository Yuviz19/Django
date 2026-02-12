from django.forms import ModelForm
from .models import Room

# a form for the room
class RoomForm(ModelForm):

    # the metadata of the class
    class Meta:
        model = Room
        fields = '__all__'