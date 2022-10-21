import logging
from os import environ

from .bot import Bot


def main(token: str, api_id: str, api_hash: str, domain: str):
    # Initialize the logger
    logging.getLogger("pyrogram").setLevel(environ.get("PYROGRAM_LOG_LEVEL", "WARNING"))
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=environ.get("LOG_LEVEL", "INFO"),
    )

    bot = Bot(token, int(api_id), api_hash, domain)
    bot.run()


if __name__ == "__main__":
    for var in ["TOKEN", "API_ID", "API_HASH", "DOMAIN"]:
        if environ.get(var) is None:
            raise ValueError(f"Environment variable {var} is not set.")
    main(environ["TOKEN"], environ["API_ID"], environ["API_HASH"], environ["DOMAIN"])
