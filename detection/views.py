from rest_framework import generics

from .models import Detection
from .serializers import DetectionSerializer


class DetectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Detection.objects.all().order_by("-created_at")
    serializer_class = DetectionSerializer