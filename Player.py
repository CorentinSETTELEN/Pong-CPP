from Bar import Bar
from Const import Const


class Player:
    def __init__(self, playerN):
        self.score = 0
        self.bar = Bar(Const.BarOffset if playerN == 1 else Const.WinLength - Const.BarOffset - Bar.length,
                       Const.WinHeight // 2 - Bar.height // 2)

