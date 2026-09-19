from django.db import models

class Detection(models.Model):

    HAND_CHOICES = [
        ("LEFT", "Left"),
        ("RIGHT", "Right"),
    ]

    hand = models.CharField(
        max_length=5,
        choices=HAND_CHOICES
    )

    confidence = models.FloatField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.hand} - {self.confidence}"