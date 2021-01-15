from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/price/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/price/index/$', consumers.PriceIndexConsumer.as_asgi()),
]