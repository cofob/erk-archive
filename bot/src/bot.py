import json
import logging

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from . import __version__
from .filters import webapp_filter
from .utils import get_webapp_data


class Bot:
    def __init__(self, bot_token: str, api_id: int, api_hash: str, domain: str):
        """Initialize the bot.

        Args:
            bot_token (str): The bot's token.
            api_id (int): The Telegram API ID.
            api_hash (str): The Telegram API hash.
            domain (str): The domain of the webapp.
        """
        self.logger = logging.getLogger(__name__)
        self.client = Client("bot", api_id, api_hash, bot_token=bot_token)
        self.domain = domain
        self.register_handlers()
        self.logger.debug("Bot initialized.")

    async def start(self, client: Client, message: Message):
        """Handle /start command."""
        self.logger.debug("Start command received.")
        await message.reply_text("Hello, world!")

    async def help(self, client: Client, message: Message):
        """Handle /help command."""
        self.logger.debug("Help command received.")
        await message.reply_text("Help message.")

    async def on_webapp(self, client: Client, message: Message):
        """Handle webapp status."""
        data = get_webapp_data(message)
        self.logger.debug(f"Webapp received: {data}")
        await message.reply_text("Data received: " + json.dumps(data))

    def register_handlers(self):
        """Register the handlers."""
        # Register /start command handler
        self.client.add_handler(MessageHandler(self.start, filters.command("start")))
        # Register /help command handler
        self.client.add_handler(MessageHandler(self.help, filters.command("help")))

        # Register WebView handler
        self.client.add_handler(MessageHandler(self.on_webapp, webapp_filter()))

        self.logger.debug("Handlers registered.")

    def run(self):
        """Launch the bot."""
        self.logger.info(f"Bot version v{__version__} started.")
        self.client.run()
