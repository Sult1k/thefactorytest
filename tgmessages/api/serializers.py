from rest_framework import serializers

from tgmessages.models import tgMessage

class tgMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = tgMessage
        fields = ['author_id', 'body', 'date_created']

class tgSendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = tgMessage
        fields =['body',]