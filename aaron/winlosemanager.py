from core.component import Component
from core.eventhandler import AppEvent

class WinLoseManager(Component):
    def __init__(self, enabled=True):
        super().__init__(enabled)