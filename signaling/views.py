import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

SIGNALING_DATA = {}  # In-memory store for signaling data

@csrf_exempt
def signaling(request, room_name):
    global SIGNALING_DATA

    if request.method == "POST":
        # Save offer/answer or ICE candidates to the signaling store
        data = json.loads(request.body)
        SIGNALING_DATA.setdefault(room_name, []).append(data)
        return JsonResponse({"status": "success"})

    elif request.method == "GET":
        # Retrieve the stored signaling messages for the room
        messages = SIGNALING_DATA.get(room_name, [])
        SIGNALING_DATA[room_name] = []  # Clear messages after retrieval
        return JsonResponse({"messages": messages})

def index(request):
    return render(request, 'index.html')