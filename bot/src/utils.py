from json import loads
from typing import Any

from pyrogram.types import Message


def get_webapp_data(message: Message) -> Any:
    """Get the WebView data from a message.

    Args:
        message (Message): The message to get the data from.

    Returns:
        Any: The deserialized WebApp data.
    """
    if message.web_app_data is None:
        return {}

    return loads(message.web_app_data.data)
