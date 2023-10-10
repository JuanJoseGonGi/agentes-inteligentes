from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import Slider
from money_model import MoneyModel
from money_agent import MoneyAgent

WIDTH = 50
HEIGHT = 50
AGENTS_AMOUNT = 100

PARAMS = {
    "agents_amount": Slider(
        "Agents amount",
        AGENTS_AMOUNT,
        2,
        100,
        description="How many agents to include in the model?",
    ),
    "width": WIDTH,
    "height": HEIGHT,
}


def agent_portrayal(agent: MoneyAgent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "Layer": 1,
        "Color": "red",
        "r": 0.2,
    }

    if agent.wealth > 0:
        portrayal["Color"] = "green"
        portrayal["r"] = 0.5
        portrayal["Layer"] = 0

    return portrayal


def run():
    grid = CanvasGrid(agent_portrayal, WIDTH, HEIGHT, 500, 500)

    chart_wealth = ChartModule(
        [
            {
                "Label": "Wealthy",
                "label": "Wealthy",
                "backgroundColor": "rgba(0, 255, 0, 0.5)",
                "Color": "green",
            },
            {
                "Label": "No Wealthy",
                "label": "No Wealthy",
                "backgroundColor": "rgba(255, 0, 0, 0.5)",
                "Color": "red",
            },
        ],
    )

    server = ModularServer(
        MoneyModel,
        [grid, chart_wealth],
        "Money Model",
        PARAMS,
    )
    server.port = 8521
    server.launch()


if __name__ == "__main__":
    run()
