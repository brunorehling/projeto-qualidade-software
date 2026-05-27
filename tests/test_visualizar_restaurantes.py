import pytest

def test_visualizar_restaurantes(page):
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("brunorehling91@gmail.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("bruno123")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("link", name="Restaurante Sabor 0").click()
    
    page.wait_for_selector("text=Um ótimo lugar para experimentar comida autêntica")
    assert page.get_by_text("Um ótimo lugar para experimentar comida autêntica").is_visible()
