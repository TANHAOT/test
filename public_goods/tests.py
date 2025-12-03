from otree.api import Bot
from .models import Player
from .pages import Contribute, Results

class PlayerBot(Bot):
    def play_round(self):
        yield Contribute, dict(contribution=cu(10))
        yield Results
