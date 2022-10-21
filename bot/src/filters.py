from json import JSONDecodeError, loads

from pyrogram import filters
from pyrogram.types import Message

from .types import WebAppTypes


def webapp_filter(type: WebAppTypes | None = None):
    """Filter for WebView status updates.

    Args:
        type (WebAppTypes | None): The type of the update. If None, no check is performed.
    """

    async def webapp(_, __, message: Message) -> bool:
        """Check if the message is a WebView status update."""

        # Check if the message is a status update
        if message.web_app_data is None:
            return False

        # Deserialize the data
        try:
            data = loads(message.web_app_data.data)
        except JSONDecodeError:
            return False

        # Check if the type matches
        if type is not None and data.get("type") != type.value:
            return False

        # Return True if the message is passed all the checks
        return True

    # Return the filter
    return filters.create(webapp)
