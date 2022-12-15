class Identifizierbar:
    def __init__(self, id_=-1):
        self.id = id_ if id_ != -1 else hash(self)
