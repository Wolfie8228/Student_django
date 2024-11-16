from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_create_list_view), 
    path("student/<int:pk>/", views.student_detail_view),
    path("student/<int:pk>/update/", views.student_update_view),
    path("student/<int:pk>/delete/", views.student_delete_view)
]