from src.models.dish import Dish
import pytest
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    bebida = Dish('coca-cola', 8.50)
    comida_estranha = Dish('escargot', 120.00)
    comida_boa = Dish('Strogonof', 17.00)

    # Verificações de igualdade do nome dos pratos
    assert bebida.name == 'coca-cola'
    assert comida_estranha.name == 'escargot'
    assert comida_boa.name == 'Strogonof'

    # Verificações de desigualdade entre os pratos
    assert bebida != comida_estranha
    assert comida_boa == comida_boa

    # Verifica o preço da bebida
    assert bebida.price == 8.50

    # Verificações de hash dos pratos
    assert hash(bebida) != hash(comida_estranha)
    assert hash(comida_boa) == hash(comida_boa)

    # Verifica a representação do objeto comida_boa
    assert repr(comida_boa) == "Dish('Strogonof', R$17.00)"

    # Cria um objeto Dish chamado podrinho com nome haburguer e preço 6.00
    podrinho = Dish('haburguer', 7.85)

    # Cria um objeto Ingredient chamado component1 com nome bacon
    baccon = Ingredient('bacon')

    # Adiciona uma dependência de ingrediente ao podrinho
    podrinho.add_ingredient_dependency(baccon, 1)

    # Verifica se component1 está na lista de ingredientes do podrinho
    assert baccon in podrinho.get_ingredients()

    # Verifica se a restrição ANIMAL_MEAT está na
    # lista de restrições do podrinho
    assert Restriction.ANIMAL_MEAT in podrinho.get_restrictions()

    # Verifica se uma exceção de ValueError é
    # lançada ao criar um com preço negativo
    with pytest.raises(ValueError):
        Dish("pudim", -6)
