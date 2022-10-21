from json import loads

from pyrogram.types import Message


def get_webapp_data(message: Message) -> dict:
    """Get the WebView data from a message.

    Args:
        message (Message): The message to get the data from.

    Returns:
        dict: The WebView data.
    """
    if message.web_app_data is None:
        return {}

    return loads(message.web_app_data.data)
