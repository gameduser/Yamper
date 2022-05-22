from showdown.battle import Battle

from ..helpers import format_decision
from ..helpers import pick_yamper_move


class BattleBot(Battle):
    def __init__(self, *args, **kwargs):
        super(BattleBot, self).__init__(*args, **kwargs)

    def find_best_move(self):
        battles = self.prepare_battles(join_moves_together=True)
        yamper_move = pick_yamper_move(battles)
        return format_decision(self, yamper_move)