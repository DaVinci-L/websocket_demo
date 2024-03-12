import time

from channels.generic.websocket import WebsocketConsumer


# Create your views here.
class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
        接收消息
        :param text_data: 客户端发送的消息
        :return:
        """
        print(text_data)
        poetry_list = [
            "云想衣裳花想容",
            "春风拂槛露华浓",
            "若非群玉山头见",
            "会向瑶台月下逢",
            "测试Gitpython"
        ]
        for i in poetry_list:
            time.sleep(0.5)
            self.send(i)
