from django.urls import path

from .views import (
    CSRFTokenAPIView,
    LoginAPIView,
    DetectionListCreateAPIView,
    LogoutAPIView,
    RefreshTokenAPIView,
)

urlpatterns = [
    path("csrf/", CSRFTokenAPIView.as_view(), name="csrf"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path(
        "token/refresh/",
        RefreshTokenAPIView.as_view(),
        name="token_refresh",
    ),
    path(
        "logout/",
        LogoutAPIView.as_view(),
        name="logout",
    ),
    path(
        "detections/",
        DetectionListCreateAPIView.as_view(),
        name="detections",
    ),
]