from django.urls import path

from .views import DetectionListCreateAPIView


urlpatterns = [
    path(
        "detections/",
        DetectionListCreateAPIView.as_view(),
        name="detections",
    ),
]