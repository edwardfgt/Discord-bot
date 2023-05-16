import os
from dotenv import load_dotenv, find_dotenv
from configparser import ConfigParser
from dataclasses import dataclass

load_dotenv(find_dotenv())

@dataclass(frozen=True)
class APIkeys:
    TOKEN: str = os.getenv('TOKEN')

print(APIkeys.TOKEN)