# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
## LocalEats

---

## 👥 Integrantes do Grupo
- Bruno Beiró

---

## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**  
Recomendações

**Descrição da funcionalidade:**  
O sistema, com base nos estabeecimentos favoritos e no histório de pedidos, recomenda restaurantes para o usuario.

**O que o usuário espera:**  
Recomendações personalizadas, ele pode achar um restaurante apenas olhando a tela inicial, sem ter que pesquisar.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**
    Testaria as entradas e saídas

### 🔹 Cenários de teste

- Cenário 1:  
    Usuário novo, sem histórico de pedidos e sem favoritos.

    Entrada: nenhuma, pois não há dados para esse usuário.

    Comportamento esperado: O sistema deve exibir recomendações genéricas. Não deve quebrar nem mostrar tela vazia.

- Cenário 2:
    Usuário com histórico de pedidos (ex: sempre pede comida italiana) e alguns favoritos. 

    Entrada: histórico de pedidos e favoritos.

    Comportamento esperado: As recomendações devem priorizar restaurantes italianos. Pode também sugerir estabelecimentos similares aos favoritos.   

---

### 🔹 Possíveis erros identificados

- Recomendações vazias ou erro ao carregar a tela para usuários sem dados.

- Recomendações irrelevantes.

- Loop infinito de recomendações iguais sem variar.

- Misturar dados de um usuário com outro.
---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```pseudo
    O sistema busca os restaurantes favoritos do usuario 
    e analisa as categorias a qual esse restaurante pertence , então faz 
    a mesma coisa com o histórico de pedidos, no final, o sistema coleta esses 
    dados, verifica quais as categorias mais recorrentes e
    recomenda os restaurantes com base nesses dados 
```

### 🔹 Situações a serem testadas

- Situação 1: O histórico de pedidos e os favoritos estão vazios, o sistema faz a recomendação genérica.

- Situação 2: O cliente favorita um restaurante, e faz um pedido desse mesmo restaurante, o sistema recomenda restaurantes da mesma categoria, mas sem recomendar exclusivamente esses restaurantes.

- Situação 3: o cliente favorita varios restaurantes de algumas categorias diferentes e faz pedidos de todos eles, o sistema recomenda com base na quantidade de aparições da mesma categoria, dando preferencia a categoria com mais aparições.

- Situação 4: O cliente favorita varios restaurantes da mesma categoria, o sistema recomenda majoriatariamente os restaurantes da mesma categoria, mas não se limita apenas a isso, pois deve recomendar outros restaurantes de outras categorias, mas com menos aparições. 


### 🔹 Possíveis erros identificados

-  Buscar similares por categoria para cada pedido gera muitas consultas.
-  Se um restaurante for removido do catálogo, ele ainda estará no histórico.

## ⚖️ 4. Comparação entre as abordagens

Qual a principal diferença entre testar sem ver o código e com acesso ao código?

> Sem ver o código, o teste se resume a testar a funcionalidade na prática, fazendo uso do sistema como se fosse um usuário e verificando o resutado das ações que foram feitas durante o teste.

>Jã com o código aberto, é possivel verificar irregularidades no código e possiveis pontos onde o sistema pode falhar.

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-preta:
    Ajuda a encontrar problemas de conformidade aos requisitos, usabilidade, inconsistências na experiência do usuário.
Caixa-branca:
    Código mal planejado, excesso de complexidade, tratamento incorreto de valores nulos, caminhos nunca executados, problemas de desempenho.

## 💡 5. Reflexão no contexto do LocalEats

Qual abordagem parece mais importante neste momento do projeto?

    Como as inconsistencias ja identificadas peos usuários, acredito que seja mais importante os testes de caixa branca, pois os problemas de usabilidade ja foram identificados, então é hora de testar e idebntificar os erros no código. 

Apenas uma abordagem seria suficiente? Por quê?

    Não, pois por mais que os usuários tenham relatado os problemas do sistema, os testes de caixa preta feitos pelos desenvolvedores e QA podem gerar insights sobre os problemas, que os usuários nçao conhecem, ajudando a resolver o problema no código.

## 🚀 Conclusão

_Resuma o que o grupo aprendeu com a atividade_

Difenrença entre testes de caixa branca e caixa preta, que são termos que não tinha conhecimento.