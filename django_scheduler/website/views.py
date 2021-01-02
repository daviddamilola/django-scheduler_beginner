from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room

def welcome(request):
    all_rooms = Room.objects.all()
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all(), "rooms": all_rooms})


def about(request):
    return HttpResponse("Nothing to see about me")

def date(request):
    return HttpResponse('this page was served at' + str(datetime.now()))