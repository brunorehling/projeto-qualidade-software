from pages.RestaurantePage import RestaurantePage

def test_visualizar_restaurantes(page):
    restaurante = RestaurantePage(page)
    restaurante.acessar()
    restaurante.realizar_login("brunorehling91@gmail.com", "bruno123")
    restaurante.abrir_restaurante("Restaurante Sabor 0")

    assert restaurante.descricao_visivel("Um ótimo lugar para experimentar comida autêntica")