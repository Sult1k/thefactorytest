from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from tgmessages.models import tgMessage
from tgmessages.api.serializers import tgMessagesSerializer

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def get_tg_messages(request):

    try:
        tgmsgs = tgMessage.objects.filter(author_id=request.user.id)
        #tgmsgs = tgMessage.objects.all()
    except tgMessage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = tgMessagesSerializer(tgmsgs, many=True)
        return Response(serializer.data)