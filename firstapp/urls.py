"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from tgmessages.views import (
    tgmessages_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    token_view,
    GetAuthToken,
)
from bot.views import (
    bot,
    #send_tg_message,
    send_tg_message_api,
)

from user_site.views import (
    home_view,
)

urlpatterns = [
    # templates
    path('admin/', admin.site.urls, name="admin"),
    path('', home_view, name="home"),
    path('tg_messages/', tgmessages_view, name="showmsgs"),
    #path('tg_messages/sendmessage/', send_tg_message, name="sendmsg"),
    # register / login / logout / get token pages
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('get-token/', token_view, name="gettoken"),
    # for telegram bot
    path('the_factory_kz_test_sultan_888xxx/', bot, name="bot"),
    # REST FRAMEWORK
    path('tg_messages/api/', include('tgmessages.api.urls', 'getmsgs-api')),
    path('tg_messages/api/sendmessage/', send_tg_message_api, name="sendmsgapi"),
    path('api/get-token/', GetAuthToken.as_view()),
]
