import random

from rovers.rover import Rover


class Insomniac(Rover):
    def __init__(self, x, y, direction, board, rid=None, sleep_rate=0.5, wake_rate=0.5):
        super().__init__(x=x, y=y, direction=direction, board=board, rid=rid)
        self.sleep_rate = sleep_rate
        self.wake_rate = wake_rate
        self.awake = True

    @staticmethod
    def rover_type(abbr=False):
        if abbr:
            return "I"
        return "Insomniac"

    def process(self, instruction):
        if self.awake and random.random() <= self.sleep_rate:
            self.awake = False
            self.print_message(f"{self.id} fell asleep")
            return

        if not self.awake and random.random() <= self.wake_rate:
            self.awake = True
            self.print_message(f"{self.id} woke up")

        if not self.awake:
            self.print_message(f"{self.id} is asleep")
            return

        super().process(instruction)
