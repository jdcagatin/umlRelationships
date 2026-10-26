from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> bool:
        pass

# EmailNotification realizes/implements NotificationSender
class EmailNotification(NotificationSender):
    def send_notification(self, message: str) -> bool:
        print(f"Sending email with message: '{message}'")
        return True


# --- Running the code ---
# 1. Instantiate the concrete implementation class
sender = EmailNotification()

# 2. Invoke the realized method
success = sender.send_notification("Your order has been shipped!")
print(f"Notification Status: {success}")
