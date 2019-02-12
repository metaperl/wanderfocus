"""Mind concentration application.

This program scripts out a time series of events designed to help a person train their mind to concentrate.
It instructs the user to do one of two things: concentrate or allow-the-mind-to-wander.
"""

from dataclasses import dataclass
import random

from icecream import ic


class Action:
    pass

class PayAttention(Action):
    pass

class WanderingMind(Action):
    pass

@dataclass
class Episode:
    """The smallest controllable unit within a session."""
    wander: int    # The percentage of time within this episode that the mind should wander
    every: int = 5 # how often an event will occur within this episode

    @property
    def pay_attention(self):
        return PayAttention()

    @property
    def wandering_mind(self):
        return WanderingMind()

    @property
    def should_pay_attention(self):
        """Decide if you should pay attention.

        You should pay attention if the RNG returns a number larger than the percentage of
        time that you can allow the mind to wander."""
        return random.randint(1,100) > self.wander

    @property
    def should_wander(self):
        return not self.pay_attention

    @property
    def decide(self):
        if self.should_pay_attention:
            return self.pay_attention
        else:
            return self.wandering_mind

    def run(self):
        for time_slice in range(0, 60, self.every):
            action = self.decide
            ic(time_slice, action)


def main():
    e = Episode(wander=70)
    e.run()

if __name__ == '__main__':
    main()
