from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import MachineSerializer
from .models import Machine

# Create your views here.


class MachineListView(ListCreateAPIView):
    serializer_class = MachineSerializer
    queryset = Machine.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Machine.objects.all()
        clientquery = self.request.query_params
        print('---->>>', clientquery)
        # queryset = queryset.filter(id__gte=30)
        queryset = queryset.exclude(data__isnull=True)
        return queryset
