class PlaceHolder:
    def __init__(self, epsilon, delta, K=10):
        self.epsilon = epsilon
        self.delta = delta
        self.K = K


    def update(self, record):
        pass

    def query(self):
        return 0

    def queryTopK(self):
        return {}
