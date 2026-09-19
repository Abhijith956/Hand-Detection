from rest_framework import serializers

from .models import Detection


class DetectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detection
        fields = [
            "id",
            "hand",
            "confidence",
            "created_at",
        ]

    def validate_hand(self, value):
        if value not in ["LEFT", "RIGHT"]:
            raise serializers.ValidationError(
                "Hand must be LEFT or RIGHT."
            )

        return value

    def validate_confidence(self, value):
        if not 0 <= value <= 1:
            raise serializers.ValidationError(
                "Confidence must be between 0 and 1."
            )

        return value