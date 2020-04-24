from django.urls import path

from tgmessages.api.views import (
    get_tg_messages,
)
app_name = 'tg_messages'
urlpatterns = [
    path('getmessage/', get_tg_messages, name='getmsgs-api'),
]

