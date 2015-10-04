from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from takeyourmeds.reminders.models import Reminder

class ReminderTimeField(serializers.RelatedField):
    def to_representation(self, model):
        return model.cronstring

class ReminderSerializer(serializers.ModelSerializer):
    times = ReminderTimeField(many=True, read_only=True)

    def create(self, data):
        req = self.context['request']
        data['user_id'] = req.user.pk
        obj = super(ReminderSerializer, self).create(data)
        for x in req.data.get('times', []):
            obj.times.create(cronstring=x)
        return obj

    class Meta:
        model = Reminder
        fields = (
            'times',
            'message',
            'audiourl',
            'telnumber',
        )

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.reminders.all()
