from django.shortcuts import render

def index(request):
    return render(request, 'price/index.html')

def room(request, room_name):
    return render(request, 'price/room.html', {
        'room_name': room_name
    })

