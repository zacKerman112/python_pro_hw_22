from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import UserConfig
from .serializers import UserConfigSerializer
from .permissions import UserPermissions


class UserConfigListAPIView(ListAPIView):
    queryset = UserConfig.objects.all()
    serializer_class = UserConfigSerializer
    permission_classes = [UserPermissions]

    def get_queryset(self) -> QuerySet:
        """Getting the filtered queryset."""
        queryset = super().get_queryset()
        username_param = self.request.query_params.get("username")
        if username_param:
            queryset = queryset.filter(user__username=username_param)
        return queryset