from otree.api import Page, WaitPage
from .models import C, set_payoffs

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    pass

page_sequence = [Contribute, ResultsWaitPage, Results]
