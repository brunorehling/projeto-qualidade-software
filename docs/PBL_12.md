# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Bruno Beiró Rehling
---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | LocalEats_ci_laboratorio|
| Link do repositório | https://github.com/brunorehling/LocalEats_ci_laboratorio |

### Estrutura de Diretórios

```text
LocalEats_ci_laboratorio/
├── tests/
│   ├── test_delivery.py
│   ├── test_delivery_bdd.py
│   ├── test_apply_discount.py
│   ├── test_apply_discount_bdd.py
│   ├── conftest.py
│   ├── features/
│   │   ├── calc_delivery.feature
│   │   └── calc_discount.feature
│   └── steps/
│       ├── test_delivery_steps.py
│       └── test_discount_steps.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── delivery.py
├── apply_discount.py
├── pytest.ini
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar cálculo do valor de entrega do pedido |
| Objetivo da funcionalidade | Calcular automaticamente a soma dos itens do pedido mais o valor da entrega conforme o destino |
| Link da Issue | https://github.com/brunorehling/LocalEats_ci_laboratorio/issues/1
---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar o cálculo correto do valor total do pedido com o valor da entrega junto |
| Link para o arquivo do teste | https://github.com/brunorehling/LocalEats_ci_laboratorio/blob/main/tests/test_delivery.py

## código relevante para o PBL 12
```python
from delivery import calculate_delivery

def test_calculate_delivery():
    assert calculate_delivery([10.0, 20.0, 30.0], 15.0) == 67.5
```

## código final após concluir os items da apostila disponobilizada na aula 17
```python
import pytest
from delivery import calculate_delivery


def test_calculate_delivery():
    assert calculate_delivery([10.0, 20.0, 30.0], 15.0) == 67.5


def test_calculate_delivery_lista_vazia():
    assert calculate_delivery([], 10) == 0


@pytest.mark.xfail(reason="Bug conhecido: aceita valores negativos silenciosamente (ver Issue #X)")
def test_calculate_delivery_valores_negativos():
    resultado = calculate_delivery([-10, 20, 30], 15)
    assert resultado == 47.5


@pytest.mark.xfail(raises=TypeError,
                   reason="Bug conhecido: nao valida tipo dos itens (ver Issue #X)")
def test_calculate_delivery_com_string():
    calculate_delivery(['abc', 20, 30], 15)

```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o workflow | https://github.com/brunorehling/LocalEats_ci_laboratorio/blob/main/.github/workflows/quality.yml |
| Link da execução | https://github.com/brunorehling/LocalEats_ci_laboratorio/actions |

```yaml
name: Quality Check
 
on:
  push:
  pull_request:
 
jobs:
  tests:
    runs-on: ubuntu-latest
 
    steps:
      - uses: actions/checkout@v4
 
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
 
      - name: Instalar dependencias
        run: |
          pip install pytest
          pip install pytest-bdd
 
      - name: Executar testes
        run: pytest

      - name: Instalar dependencias (com extras)
        run: |
          pip install pytest pytest-bdd flake8 pytest-cov
 
      - name: Verificar estilo do codigo
        run: flake8 . --max-line-length=100 --exclude=.venv,.git
 
      - name: Executar testes com cobertura
        run: pytest --cov=. --cov-fail-under=80
        # Falha se a cobertura for menor que 80%
```

---

## 5. Indicadores de Qualidade
 
| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 2 |
| Quantidade de testes aprovados | 2 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |
 
---
 
## 6. Registro de Defeito
 
| Item | Descrição |
|--------|--------|
| Título do defeito | Pipeline falha por ausência de evento definido em `on` |
| Severidade | Alta |
| Link da Issue | https://github.com/brunorehling/LocalEats_ci_laboratorio/issues/5|
 
O defeito ocorreu quando o Pull Request da branch feature/calculate_delivery foi mergeado na main, sobrescrevendo o arquivo quality.yml com uma versão que não continha a seção on (gatilhos push e pull_request). O problema foi identificado automaticamente pela falha do workflow na aba Actions do GitHub, com a mensagem "No event triggers defined in on". Após restaurar os gatilhos no quality.yml, o pipeline voltou a ser executado corretamente e os testes passaram normalmente.