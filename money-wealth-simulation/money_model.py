from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from money_agent import MoneyAgent


class MoneyModel(Model):
    def __init__(self, agents_amount: int, width: int, height: int) -> None:
        self.agents_amount = agents_amount
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        for i in range(self.agents_amount):
            newAgent = MoneyAgent(i, self)
            self.schedule.add(newAgent)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(newAgent, (x, y))

    def step(self) -> None:
        self.schedule.step()
