# Aula 9 – Testes Unitários e TDD

## 👥 Integrantes
- Bruno Beiró Rehling

---

## 📁 Estrutura do Projeto

.  
├── src/  
│   ├── pedido.py  
│   ├── desconto.py  
│   └── entrega.py  
└── tests/  
    ├── test_pedido.py  
    ├── test_desconto.py  
    └── test_entrega.py  

---

## 🔹 1. Funcionalidades escolhidas

Cada integrante ficou responsável por uma regra de negócio do sistema.

---

### 👤 Bruno Rehling – Cálculo da taxa de entrega 

**Arquivo da implementação:** `/src/entrega.py`  
**Arquivo de testes:** `/tests/test_entrega.py`

#### Descrição
Verifica a distancia entre o restaurante e a localização do usuario e calcula a taxa de entrega.

#### Regras de negócio
- verifica a localização da entrega 
- calcula a distancia entre o restaurante e o local de entrega 
- retorna o valor da entrega

---

## 🔹 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta `/tests`.

---

### 🧪 Bruno Rehling – Testes (entrega)

#### Teste 1 – Taxa fixa para distância de 2km

- Cenário: A distância está abaixo do limite de 3km para o valor fixo de entrega.
- Resultado esperado: R$5,00 fixo.

##### TDD
- Red: função inexistente, falhou com ImportError
- Green: implementação mínima retornando 5.00 fixo
- Refactor: adicionada lógica condicional completa e validação de negativo

##### Refatoração
- Código evoluiu de retorno fixo para lógica condicional
- Separação clara entre os casos: negativo → erro, ≤3km → fixo, >3km → proporcional

##### Execução
- Resultado: Passou

---

#### Teste 2 – Taxa fixa para distância de 3km (limite exato)

- Cenário: Distância exatamente no limite de 3km ainda deve retornar taxa fixa.
- Resultado esperado: R$5,00 fixo.

##### TDD
- Red: função inexistente, falhou com ImportError
- Green: condição `if distancia <= 3` cobriu esse caso
- Refactor: uso de `<=` garante que o limite exato seja incluído na taxa fixa

##### Refatoração
- Teste de borda que valida o comportamento exato na fronteira da regra de negócio

##### Execução
- Resultado: Passou

---

#### Teste 3 – Taxa proporcional para distância de 5km

- Cenário: Distância acima de 3km deve aplicar taxa proporcional.
- Resultado esperado: R$8,00 → 5.00 + (5 - 3) × 1.50 = 8.00

##### TDD
- Red: implementação mínima retornava 5.00 fixo, falhou com `assert 5.0 == 8.0`
- Green: adicionado `return 5.00 + (distancia - 3) * 1.50`
- Refactor: fórmula mantida, ordem dos `if` ajustada

##### Refatoração
- Fluxo legível: valida negativo → caso fixo → caso proporcional

##### Execução
- Resultado: Passou

---

#### Teste 4 – Erro para distância negativa

- Cenário: Distância negativa é inválida e deve lançar erro.
- Resultado esperado: ValueError com mensagem "A distância não pode ser negativa."

##### TDD
- Red: `calcular_entrega(-1)` retornava 5.00 em vez de erro pois o `if distancia <= 3` vinha antes
- Green: adicionado `if distancia < 0: raise ValueError(...)` antes dos demais `if`
- Refactor: ordem dos `if` corrigida, bug real encontrado pelo TDD

##### Refatoração
- Bug revelado pelo teste: a ordem errada dos `if` fazia distância negativa retornar 5.00
- Sem o TDD esse erro passaria despercebido

##### Execução
- Resultado: Passou
---

## 🔹 3. Reflexão

### Foi difícil escrever testes antes do código?
Sim, pois exige uma mudança de mentalidade. O que eu costumo fazer é implementar primeiro e testar depois. Escrever o teste antes obriga a pensar no comportamento esperado da função antes de pensar em como ela funciona. Ajudou a deixar as regras de negócio mais claras desde o início.

---

### O TDD ajudou no desenvolvimento?
Sim. O ciclo Red → Green → Refactor acabou revelando um bug: a ordem errada dos `if` fazia `calcular_entrega(-1)` retornar `5.00` em vez de lançar erro. Sem o TDD, esse problema passaria despercebido e só apareceria em produção.

---

### Os testes aumentaram a confiança no código?
Sim. Após a refatoração, os 4 testes continuaram passando, o que garantiu que nenhuma mudança quebrou o comportamento esperado.

---

### O que melhorariam?
- Cobrir mais cenários de borda, como distância zero ou valores decimais (ex: 2.5km)

---

### Como isso ajuda no projeto?
No projeto do grupo, o sistema LocalEats lida com regras financeiras que impactam diretamente o valor cobrado do cliente. Testes automatizados garantem que alterações futuras, como mudança na taxa por km ou no limite de distância fixa, não quebrem silenciosamente outras partes do sistema.