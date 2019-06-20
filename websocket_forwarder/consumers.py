from channels.generic.websocket import AsyncWebsocketConsumer

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = f"group_{self.scope['url_route']['kwargs']['id']}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, **kwargs):
        await self.channel_layer.group_send(self.group_name, {
            'type': 'message',
            'kwargs': kwargs,
        })

    async def message(self, event):
        await self.send(**event['kwargs'])
