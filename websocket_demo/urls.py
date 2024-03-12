from django.contrib import admin
from django.urls import path

from api.views import ChatConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
]

websocket_urlpatterns = [
    # 前端请求websocket连接
    path('wx/', ChatConsumer.as_asgi()),
]
