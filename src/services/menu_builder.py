import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> pd.DataFrame:

        # Lista de descrições dos itens do menu
        desc_itens = ["dish_name", "ingredients", "price", "restrictions"]

        # Criação de uma lista de dicionários com as informações dos pratos
        pratos_menu = [

            # Mapeamento das dscrições com os valores correspondentes
            # dict converte as tuplas resultantes em dicionarios, permitindo
            # organizar as informações dos pratos do menu de forma estruturada.
            dict(
                # zip combina as descrições dos itens com os valores iguais
                zip(desc_itens, [
                    index.name,
                    index.price,
                    index.get_restrictions(),
                    index.get_ingredients()
                ])
            )
            # Iteração sobre os pratos do menu
            for index in self.menu_data.dishes
            # Verifica se o prato não possui a restrição especificada
            if restriction not in index.get_restrictions()
        ]

        # Retorna um DataFrame do pandas contendo as informações dos pratos
        return pd.DataFrame(pratos_menu)
