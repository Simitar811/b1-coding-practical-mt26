class Controller:
    def __init__(self, kp=0.15,kd=0.6):
        self.kp = kp
        self.kd = kd
    def step(self,current_error: float, previous_error: float):
        action = self.kp*current_error + self.kd*(current_error - previous_error)
        return action