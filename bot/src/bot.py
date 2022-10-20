import logging
import json

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
    WebAppInfo,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ContextTypes,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, token: str):
        """Initialize the bot.

        Args:
            token (str): The bot's token.
        """
        self.token = token
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher
        self.register_handlers()
        logger.debug("Bot initialized.")

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        logger.debug("Start command issued.")
        user = update.effective_user
        update.message.reply_text(
            "Please press the button below to choose a color via the WebApp.",
            reply_markup=ReplyKeyboardMarkup.from_button(
                KeyboardButton(
                    text="Open the color picker!",
                    web_app=WebAppInfo(url="https://python-telegram-bot.org/static/webappbot"),
                ),
            ),
        )

    def help_command(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        logger.debug("Help command issued.")
        update.message.reply_text("Help!")

    def echo(self, update: Update, context: CallbackContext) -> None:
        """Echo the user message."""
        logger.debug("Echoing message.")
        update.message.reply_text(update.message.text)

    def web_app_data(self, update: Update, context: ContextTypes.bot_data) -> None:
        """Print the received data and remove the button."""
        logger.debug("Web app data received.")
        data = json.loads(update.effective_message.web_app_data.data)
        update.message.reply_html(
            text=f"You selected the color with the HEX value <code>{data['hex']}</code>. The "
            f"corresponding RGB value is <code>{tuple(data['rgb'].values())}</code>.",
            reply_markup=ReplyKeyboardRemove(),
        )

    def register_handlers(self):
        """Register the bot's handlers."""
        # on different commands - answer in Telegram
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("help", self.help_command))

        # on web app data
        self.dispatcher.add_handler(MessageHandler(Filters.status_update, self.web_app_data))

        # on non command i.e message - echo the message on Telegram
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))

        logger.debug("Handlers registered.")

    def run(self):
        """Launch the bot."""
        logger.info("Bot started.")
        self.updater.start_polling()
        self.updater.idle()
