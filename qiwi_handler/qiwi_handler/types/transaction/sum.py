from qiwi_handler.utils.methods import MakeDict


class Sum(MakeDict):
    def __init__(self,
                 amount: int = None,
                 currency: int = None):
        self.amount = amount
        self.currency = currency



