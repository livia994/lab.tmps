class ExternalNotificationService:
    def send_message(self, message):
        print(f"[System Notification] {message}")
class NotificationAdapter:
    def __init__(self, service):
        self.service = service

    def notify_user(self, user, message):
        self.service.send_message(user.email, message)
class Observer:
    def update(self, message):
        pass

class UserNotificationObserver(Observer):
    def __init__(self, user):
        self.user = user

    def update(self, message):
        print(f"[Notification to {self.user.name}] {message}")
