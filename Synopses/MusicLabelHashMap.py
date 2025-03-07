from Synopses.PlaceHolder import PlaceHolder


class MusicLabelHashMap:
    def __init__(self, epsilon, delta):
        self.epsilon = epsilon
        self.delta = delta
        self.map = {}

    def update(self, record):
        label = record[4]
        if label not in self.map:
            self.map[label] = PlaceHolder(self.epsilon, self.delta)
        self.map[label].update(record)

    def query(self, label):
        return self.map[label].query() if label in self.map else 0
