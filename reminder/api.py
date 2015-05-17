from rest_framework import serializers, viewsets

from .models import Reminder, ReminderTime


class ReminderTimeField(serializers.RelatedField):
    def to_representation(self, model):
        return model.cronstring


class ReminderSerializer(serializers.ModelSerializer):
    reminder_times = ReminderTimeField(many=True, read_only=True)

    def create(self, data):
        obj = super(ReminderSerializer, self).create(data)
        req = self.context['request']
        print req.data
        for reminder_time in req.data.get('reminder_times', []):
            rt = ReminderTime(
                reminder=obj,
                cronstring=reminder_time,
            )
            rt.save()
        return obj


    class Meta:
        model = Reminder
        fields = (
            'reminder_times',
            'message',
            'audiourl',
            'telnumber',
        )


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


