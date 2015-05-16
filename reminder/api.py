from rest_framework import routers, serializers, viewsets

from .models import Reminder

class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminder


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
