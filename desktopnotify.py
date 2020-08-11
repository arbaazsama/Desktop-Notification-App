import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="YOUR MESSAGE",
        message="MESSAGE",
        app_icon="ICON_LOCTAION",
        timeout=10,
    )
