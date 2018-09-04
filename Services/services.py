from .db.db import DBService
from .logic.logic import LogicService
from .math.math import MathService


class Services:

    def __init__(self):
        self.db_service = DBService()
        self.logic_service = LogicService(self)
        self.math_service = MathService(self)
