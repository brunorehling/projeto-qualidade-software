Feature: Busca de restaurantes

  Scenario: Busca válida retorna resultados
    Given que o usuário está na página inicial
    When busca por "centro"
    Then o sistema deve exibir a lista de restaurantes

  Scenario: Campo de busca vazio mantém a listagem
    Given que o usuário está na página inicial
    When não preenche o campo de busca
    Then o sistema deve exibir a lista de restaurantes