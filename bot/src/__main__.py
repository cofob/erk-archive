import logging
from os import environ

from .bot import Bot


def main():
    # Initialize the logger
    logging.getLogger("pyrogram").setLevel(environ.get("PYROGRAM_LOG_LEVEL", "WARNING"))
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=environ.get("LOG_LEVEL", "INFO"),
    )

    for var in ["TOKEN", "API_ID", "API_HASH", "DOMAIN"]:
        if environ.get(var) is None:
            raise ValueError(f"Environment variable {var} is not set.")

    bot = Bot(environ["TOKEN"], int(environ["API_ID"]), environ["API_HASH"], environ["DOMAIN"])
    bot.run()


if __name__ == "__main__":
    main()
