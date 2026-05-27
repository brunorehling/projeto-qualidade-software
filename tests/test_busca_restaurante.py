from pytest_bdd import scenarios, given, when, then

scenarios('../features/busca_restaurantes.feature')

BASE_URL = "https://local-eats-unisenac.vercel.app/static/login.html"

@given('que o usuário está na página inicial')
def acessar_pagina(page):
    page.goto(BASE_URL)
    page.get_by_role("textbox", name="teste@teste.com").fill("brunorehling91@gmail.com")
    page.get_by_role("textbox", name="Sua senha secreta").fill("bruno123")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.wait_for_selector("#restaurantGrid")

@when('busca por "centro"')
def buscar_restaurante(page):
    page.get_by_role("textbox", name="Buscar por culinária ou").fill("centro")
    page.get_by_role("button", name="Buscar").click()

@when('não preenche o campo de busca')
def nao_buscar(page):
    pass

@then('o sistema deve exibir a lista de restaurantes')
def validar_resultados(page):
    page.wait_for_selector("#restaurantGrid")
    assert page.locator("#restaurantGrid").is_visible()