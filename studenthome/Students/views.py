from rest_framework import generics
from django.shortcuts import render
from .models import student
from .serializers import Student_serializer

# Create your views here.
class StudentCreateListViewAPI(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = Student_serializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

student_create_list_view = StudentCreateListViewAPI.as_view()

class StudentDetailViewAPI(generics.RetrieveAPIView):
    queryset = student.objects.all()
    serializer_class = Student_serializer

student_detail_view = StudentDetailViewAPI.as_view()

class StudentUpdateViewAPI(generics.RetrieveUpdateAPIView):
    queryset = student.objects.all()
    serializer_class = Student_serializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.s_id:
            instance.s_id = instance.id
        instance.save()

student_update_view = StudentUpdateViewAPI.as_view()

class StudentDeleteViewAPI(generics.RetrieveDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = Student_serializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

student_delete_view = StudentDeleteViewAPI.as_view()