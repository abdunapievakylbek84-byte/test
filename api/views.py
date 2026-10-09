from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all()
        completed_param = self.request.query_params.get('completed')
        if completed_param is not None:
            is_completed = completed_param.lower() in ['true', '1', 'yes']
            queryset = queryset.filter(completed=is_completed)
        return queryset
