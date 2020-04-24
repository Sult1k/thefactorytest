from django.shortcuts import render, redirect
from tgmessages.models import tgMessage
from tgmessages.api.serializers import tgMessagesSerializer

def tgmessages_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        tgmessages = []
        tgmsgs = tgMessage.objects.filter(author_id=request.user.id)
        serializer = tgMessagesSerializer(tgmsgs, many=True)
        resp = serializer.data
        for each in resp:
            tgmessages.append([each['author_id'], each['body'], each['date_created']])
    except:
        tgmessages = ['У вас нет сообщений']

    context = {'tgmessages': tgmessages}
    return render(request, 'tgmessages/show.html', context)


# Create your views here.
