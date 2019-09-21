from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('',views.EventListView.as_view(),name='event_list_view'),
    path('<int:pk>/',views.EventDetailView.as_view(),name='event_detail_view'),
]
