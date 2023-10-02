from mesa import Model, DataCollector
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from money_agent import MoneyAgent


class MoneyModel(Model):
    def __init__(self, agents_amount: int, width: int, height: int) -> None:
        self.agents_amount = agents_amount
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        self.datacollector = DataCollector(
            model_reporters={
                "Wealthy": self.count_wealthy_agents,
                "No Wealthy": self.count_no_wealthy_agents,
            },
        )

        for i in range(self.agents_amount):
            newAgent = MoneyAgent(i, self)
            self.schedule.add(newAgent)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(newAgent, (x, y))

    def step(self) -> None:
        self.schedule.step()
        self.datacollector.collect(self)

    def count_wealthy_agents(self) -> int:
        return sum([1 for a in self.schedule.agents if a.wealth > 0])

    def count_no_wealthy_agents(self) -> int:
        return sum([1 for a in self.schedule.agents if a.wealth == 0])
