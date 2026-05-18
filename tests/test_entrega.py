import pytest
from src.entrega import calcular_entrega

def test_taxa_fixa_para_distancia_de_2km():
    assert calcular_entrega(2) == 5.00

def test_taxa_fixa_para_distancia_de_3km():
    assert calcular_entrega(3) == 5.00

def test_taxa_proporcional_para_distancia_de_5km():
    assert calcular_entrega(5) == 8.00

def test_erro_para_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_entrega(-1)