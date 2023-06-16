from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # definindo os ingredientes
    req_1_ingrediente_1 = Ingredient("manteiga")
    req_1_ingrediente_2 = Ingredient("manteiga")
    req_1_ingrediente_3 = Ingredient("bacon")

    #  verificações simples de igualdade
    assert hash(req_1_ingrediente_1) == hash(req_1_ingrediente_2)
    assert hash(req_1_ingrediente_1) != hash(req_1_ingrediente_3)
    assert req_1_ingrediente_1 == req_1_ingrediente_2
    assert req_1_ingrediente_1 != req_1_ingrediente_3
    assert req_1_ingrediente_2.name == "manteiga"

    # verifica a representação em dormato de string
    assert repr(req_1_ingrediente_3) == "Ingredient('bacon')"

    # verifica se o conjunto dos ingredientes
    assert Ingredient("frango").restrictions == {
        Restriction.ANIMAL_MEAT, 
        Restriction.ANIMAL_DERIVED
    }

    # verifica se o conjunto dos ingredientes
    assert Ingredient("creme de leite").restrictions == {
        Restriction.LACTOSE, 
        Restriction.ANIMAL_DERIVED
    }

