import os
import sys

from settings.config import settings

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

TORTOISE_ORM = settings.TORTOISE_ORM
