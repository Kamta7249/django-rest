from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user1')
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    ordering_fields = ['name','city']







    # filter_backends = [SearchFilter]
    # search_fields = ['city']
    # search_fields = ['name','city']
    # search_fields = ['^name']



    # filter_backends = [DjangoFilterBackend]
    # # filterset_fields = ['city']
    # filterset_fields = ['name','city']
