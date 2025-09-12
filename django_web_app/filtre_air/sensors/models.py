from django.db import models
import random

class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    air_quality = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_fake_data():
        return SensorData.objects.create(
            temperature=round(random.uniform(18, 30), 2),
            humidity=round(random.uniform(30, 70), 2),
            air_quality=random.randint(1, 100)
        )
