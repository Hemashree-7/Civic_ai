from django.urls import path

from .views import (
    ComplaintCreateView,
    ComplaintListView,
    ComplaintStatusUpdateView,
    OfficerComplaintListView,
    AnalyticsView
)

urlpatterns = [

    path('create/', ComplaintCreateView.as_view(), name='create-complaint'),

    path('my-complaints/', ComplaintListView.as_view(), name='my-complaints'),

    path('update/<int:pk>/', ComplaintStatusUpdateView.as_view(), name='update-complaint'),

    path('officer-dashboard/', OfficerComplaintListView.as_view(), name='officer-dashboard'),

    path('analytics/', AnalyticsView.as_view(), name='analytics'),

]