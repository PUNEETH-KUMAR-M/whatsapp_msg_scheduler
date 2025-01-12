import pywhatkit as kit
from datetime import datetime


def send_message(phone_number, message, hour, minute):
    """Send a scheduled WhatsApp message."""
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"Message sent to {phone_number} at {hour}:{minute}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    phone_number = ""  # Replace with the recipient's phone number
    message = "Hello! i am testing whatsapp scheduler using python"

    now = datetime.now()
    hour = 10
    minute = 55 # Schedule it 2 minutes from now


    # Ensure that the minute doesn't exceed 59
    if minute >= 60:
        minute -= 60
        hour += 1

    # Call the function to send the message
    send_message(phone_number, message, hour, minute)
