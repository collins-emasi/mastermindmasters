from django.db import models


class Pillars(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class VisionMissionAbout(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"
