from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from takeyourmeds.reminder.models import Reminder, ReminderTime

class ReminderTimeField(serializers.RelatedField):
    def to_representation(self, model):
        return model.cronstring

class ReminderSerializer(serializers.ModelSerializer):
    reminder_times = ReminderTimeField(many=True, read_only=True)

    def create(self, data):
        req = self.context['request']
        data['user_id'] = req.user.pk
        obj = super(ReminderSerializer, self).create(data)
        for reminder_time in req.data.get('reminder_times', []):
            ReminderTime.objects.create(
                reminder=obj,
                cronstring=reminder_time,
            )
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)

@api_view(('POST',))
def trigger_now(request):
    # FIXME: Move parameter to urlconf
    pk = request.data.get('id')
    reminder = Reminder.objects.get(pk=pk)
    reminder.dispatch_task()

    return Response({'message': "Triggered"})
