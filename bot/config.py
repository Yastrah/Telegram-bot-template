import configparser
from dataclasses import dataclass


def convertToBool(val: str) -> bool:
    if val.lower() in ["0", "false"]:
        return False
    return True

@dataclass
class Bot:
    name: str
    admin_id: list[int]
    use_redis: bool


@dataclass
class Logging:
    format: str
    datefmt: str
    debug: bool


class Settings:
    def __init__(self, file_path):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    @property
    def bot(self):
        bot_conf = self.config["bot"]

        return Bot(
            name=bot_conf["name"],
            admin_id=list(map(int, bot_conf["admin_id"].split())),
            use_redis=convertToBool(bot_conf["use_redis"]),
        )

    @property
    def logging(self):
        logging_conf = self.config["logging"]

        return Logging(
            format=logging_conf["format"],
            datefmt=logging_conf["datefmt"],
            debug=convertToBool(logging_conf["debug"]),
        )

settings = Settings("bot/bot.ini")