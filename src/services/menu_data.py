import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(then, source_path: str) -> None:
        then.pratos_menu = {}
        # Dicionaro para armazenas os pratos

        with open(source_path, "r") as file:
            #  abre o arquivo com o with para garantir o fechamento

            for dishesRows in csv.DictReader(file):
                # itera sobre as linhas do arquivo
                # e le as linhas como dicionario

                value_dish = dishesRows["dish"]
                # armazena o valor da coluna

                if value_dish not in then.pratos_menu:
                    # if para verificar se o prato atual esta na no dicionario

                    then.pratos_menu[value_dish] = Dish(
                        value_dish, float(dishesRows["price"]))
                    # se o prato n estiver no dicionario ele é adicionado
                    # com a chave value_dish e o valor é convertido para float

                then.pratos_menu[value_dish].add_ingredient_dependency(
                    # add uma dependência de ingrediente ao prato atual

                    Ingredient(dishesRows["ingredient"]),
                    # Cria uma instância da classe Ingredient
                    # com o nome do ingrediente

                    int(dishesRows["recipe_amount"]),
                    # converte a quantidade da receita convertida para int
                    # e add essa dependência ao prato atual
                )

        then.dishes = set(then.pratos_menu.values())
        # da ao atributo dishes do objeto MenuData um conjunto
        # com os valores do dicionário pratos_menu.
        # se tiver pratos duplicados, ele remove
        # e armazena os pratos exclusivos do menu.
