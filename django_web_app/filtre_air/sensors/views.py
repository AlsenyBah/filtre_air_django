from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData

def dashboard(request):
    return render(request, "sensors/dashboard.html")

def get_data(request):
    data = SensorData.generate_fake_data()
    return JsonResponse({
        "temperature": data.temperature,
        "humidity": data.humidity,
        "air_quality": data.air_quality,
        "timestamp": data.timestamp.strftime("%H:%M:%S")
    })
