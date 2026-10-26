class Logger:
    def log_message(self, text: str):
        print(f"Logging: {text}")

class SystemAlert:
    def __init__(self, message: str):
        self.message = message

    # SystemAlert depends on a Logger object strictly during this call
    def send_alert(self, logger_device: Logger):
        logger_device.log_message(self.message)


# --- Running the code ---
# 1. Instantiate the individual tool objects independently
my_logger = Logger()
critical_alert = SystemAlert("High CPU usage detected!")

# 2. Execute the function call passing the required dependent device
critical_alert.send_alert(my_logger)
