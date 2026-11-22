from core.component import Component

class PrintComponent(Component):
    def __init__(self, enabled=True):
        super().__init__(enabled)
    
    def start(self, params=None):
        print("I have started!")
        return
    
    def update(self, params=None):
        print("I am updating")
        return

    def late_update(self, params=None):
        print("I am LATE updating")
        return
