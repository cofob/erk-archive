from .bot import Bot
from os import environ


def main():
    if "TOKEN" not in environ:
        raise Exception("No token found in environment variables.")

    bot = Bot(environ["TOKEN"])
    bot.run()


if __name__ == "__main__":
    main()
