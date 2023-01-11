class Identifizierbar(object):
    def __init__(self):
        self.id=hash(self)
