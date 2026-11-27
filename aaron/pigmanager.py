from core.component import Component
from core.eventhandler import AppEvent

class PigManager(Component):
    def __init__(self, enemies, enabled=True):
        super().__init__(enabled)
        self.enemies = enemies
        self.on_pigs_dead = AppEvent()
        self.checked_pigs = False

    def update(self, params=None):
        if self.checked_pigs == True:
            return

        for enemy in self.enemies:
            try:
                bool(enemy)
            except ReferenceError:
                self.on_pigs_dead.invoke()
                self.checked_pigs = True
                break
        
        # print(self.enemies)
