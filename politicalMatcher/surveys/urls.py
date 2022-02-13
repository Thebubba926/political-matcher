from django.urls import path

from . import views

urlpatterns = [
    path('surveys', views.SurveysListView.as_view(), name="surveys.list"),
    path('surveys/<int:pk>', views.SurveysDetailView.as_view(), name="surveys.detail"),
    path('surveys/<int:pk>/edit', views.SurveysUpdateView.as_view(), name="surveys.update"),
    path('surveys/<int:pk>/delete', views.SurveysDeleteView.as_view(), name="surveys.delete"),
    path('surveys/new', views.SurveysCreateView.as_view(), name="surveys.new"),
]