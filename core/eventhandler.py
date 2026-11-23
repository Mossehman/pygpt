# Provides a clean way to attach functions dynamically to certain calls without hardcoding

class AppEvent:

    def __init__(self):
        self.event_listeners = []
        self.event_listeners_onetime = []

    # f is a function that we append to the list of event listeners
    def add_listener(self, f):
        self.event_listeners.append(f)

    def add_listener_oneshot(self, f):
        self.event_listeners_onetime.append(f)

    def invoke(self, params=None):
        for func in self.event_listeners:
            if (func is None):
                continue
            func(params)
        for func in self.event_listeners_onetime:
            if (func is None):
                continue
            func(params)
        self.event_listeners_onetime.clear() # clear the one time listeners


    def remove_listener(self, f):
        self.event_listeners.remove(f)

    def clear_listeners(self):
        self.event_listeners_onetime.clear() # clear the one time listeners
        self.event_listeners.clear() # Create a new set and discard the original