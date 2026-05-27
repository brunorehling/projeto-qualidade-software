class RestaurantePage:
    URL = "https://local-eats-unisenac.vercel.app/static/login.html"

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(self.URL)

    def realizar_login(self, email, senha):
        self.page.get_by_role("textbox", name="teste@teste.com").fill(email)
        self.page.get_by_role("textbox", name="Sua senha secreta").fill(senha)
        self.page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    def abrir_restaurante(self, nome):
        self.page.get_by_role("link", name=nome).click()

    def descricao_visivel(self, texto):
        self.page.wait_for_selector(f"text={texto}")
        return self.page.get_by_text(texto).is_visible()