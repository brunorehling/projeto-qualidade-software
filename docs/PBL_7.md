# 🧩 Atividade PBL – Aula 10
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrante(s)
- Bruno Beiró Rehling

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Fluxo:
Navegação e visualização de restaurantes

🔎 **Descrição**
Permite navegar pela lista de restaurantes e visualizar os detalhes de um restaurante específico.

🎯 **Importância**
Base da experiência do usuário — sem esse fluxo funcionando, o usuário não consegue explorar opções nem avançar para o pedido.

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
python -m playwright codegen https://local-eats-unisenac.vercel.app/static/index.html
```

### 🔗 Link para o código gerado

👉 https://github.com/brunorehling/projeto-qualidade-software/tree/pbl_7/tests/codegen_visualizar_restaurantes.py

### 🧠 Observações

- O Codegen capturou o fluxo completo automaticamente
- Usou seletores por `role`, mais semânticos que seletores CSS
- Gerou ações desnecessárias: `.click()` antes de cada `.fill()`, `press("Enter")` duplicando o botão Entrar, e cliques em elementos sem finalidade de teste
- Nenhuma assertion foi gerada — exigiu refatoração

---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Link para o teste

👉 https://github.com/brunorehling/projeto-qualidade-software/tree/pbl_7/tests/test_visualizar_restaurantes.py

### 📌 O que o teste faz?

- Acessa a página de login
- Realiza autenticação com credenciais válidas
- Navega até o Restaurante Sabor 0
- Valida que as informações do restaurante são exibidas corretamente

---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 https://github.com/brunorehling/projeto-qualidade-software/tree/pbl_7/pages/RestaurantePage.py

### 🔗 Link para teste refatorado

👉 https://github.com/brunorehling/projeto-qualidade-software/tree/pbl_7/pages/test_RestaurantePage.py

### 🧠 Melhorias realizadas

- Separação entre teste e lógica de UI
- Seletores centralizados na classe `RestaurantePage`
- O teste agora espera o conteúdo carregar antes de verificar se está visível

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
python -m pytest -v
```

### 📊 Resultado

- Total de testes: 6
- Testes passaram: 6
- Testes falharam: 0

### 📸 Evidência

![evidencia](/img/tests_pbl7.png)

---

## 🔹 6. Análise crítica

- O teste rodava antes do conteúdo carregar na página, causando erro — foi necessário adicionar uma espera antes de verificar
- Se o texto da descrição do restaurante mudar, o teste quebra, pois ele busca pelo texto exato
- O Codegen ajudou a começar, mas gerou ações desnecessárias e sem nenhuma verificação de resultado
- O teste seria mais confiável se o sistema tivesse identificadores fixos nos elementos, sem depender do texto visível

---

## 🔹 7. Reflexão

- Testes automatizados não substituem testes manuais — cobrem fluxos repetitivos, não problemas de usabilidade
- Não vale automatizar todos os fluxos — priorizar os críticos: login, navegação, checkout
- Aumentam a confiança em deploys e reduzem dependência de validação manual

---

## 💡 Conclusão

A automação com Playwright e Pytest validou o fluxo principal do LocalEats com eficiência. O Page Object Model organizou o código e facilitou a manutenção. O principal aprendizado foi lidar com carregamento assíncrono e escolher seletores estáveis para garantir testes confiáveis.