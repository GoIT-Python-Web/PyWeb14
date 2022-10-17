from __future__ import annotations

from abc import abstractmethod, ABC


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to email: {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send {message} sms to phone: {self.phone}')


class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    person = Contact('Dima', 'dima@gmail.com', '+380663332211')
    notification_SMS = SMS(person.phone)
    notification_email = Email(person.email)
    notification_service = NotificationService(notification_email)
    notification_service.send('Hello bro')

# SMS -> Service
# Contact -> Service

# Contact -> SMS -> Service
