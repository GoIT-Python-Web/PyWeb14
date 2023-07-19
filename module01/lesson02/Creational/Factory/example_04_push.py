class Message():
    def __init__(self, body, title):
        self.body = body
        self.title = title
    
    def send(self):
        pass


class AndroidPush(Message):

    def send_via_google_api(self):
        print('sinding to andoid')

    def send(self):
        self.send_via_google_api()

class IOSPush(Message):
    def send_via_apple_api(self):
        print('sinding to iphones')
    

    def send(self):
        self.send_via_apple_api()


class PushFactory:
    def __init__(self):
        self._vendors = ["IOS", "Android"]

    def create_push_notification(self, vendor, body, title):
        if vendor == "IOS":
            return IOSPush(body, title)
        elif vendor == "Android":
            return AndroidPush(body, title)
        else:
            raise ValueError(f"Invalid vendor: {vendor}")


body = "hello world"
title = "message"
users = [{"name": "John Dou", "device": "IOS"}, {"name": "Jack Johnes", "device": "Android"}]

factory = PushFactory()

notifications = [factory.create_push_notification(user.get("device"), body,title) for user in users]


for notification in notifications:
    notification.send()
