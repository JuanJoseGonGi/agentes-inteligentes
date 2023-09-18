from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from money_model import MoneyModel
from money_agent import MoneyAgent


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
    num_row_width = 50
    num_row_height = 50

    grid = CanvasGrid(agent_portrayal, num_row_width, num_row_height, 500, 500)
    server = ModularServer(
        MoneyModel,
        [grid],
        "Money Model",
        {"agents_amount": 100, "width": num_row_width, "height": num_row_height},
    )
    server.port = 8521
    server.launch()


if __name__ == "__main__":
    run()
