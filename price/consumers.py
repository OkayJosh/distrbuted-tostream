import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import PriceIndex
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

class PriceIndexConsumer(AsyncConsumer):
    # #db connection    
    # async def connect(self):
    #     self.price = await database_sync_to_async(self.get_name)()

    def get_price(self):
        return PriceIndex.objects.all()

    # # Receive message from WebSocket
    # async def receive(self):
    #     text_data_json = json.loads(self.price)
    #     message = text_data_json['message']
    
    async def websocket_connect(self, event):
        self.price = await database_sync_to_async(self.get_price)()
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        text_data_json = json.loads(self.price)
        await self.send({
            "type": "websocket.send",
            "text": event["text_data_json"],
        })

        # # Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'price_message',
        #         'message': message
        #     }
        # )