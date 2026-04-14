# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Login
- Busca de restaurantes com filtro
- Salvamento de locais como favoritos
- Corpatilhamento de experiencias
- Receber recomendações personalizadas

---

## 2. Níveis de Teste

### Funcionalidade: Login
- Unitário: validar senha e campos obrigatórios
- Integração: verificar comunicação com banco
- Sistema: usuário faz login completo
- Aceitação: usuário entra no sistema sem erro

### Funcionalidade: Busca de restaurantes com filtro
- Unitário: verificar se os filtros estão funcionando
- Integração: verifiar se a requisição esta indo opara o endpoint certo
- Sistema: usuário seleciona a barra de busca, e seleiona os filtros desejados
- Aceitação: o sistema retorna os restaurantes que possuem aquela caracteristica 

### Funcionalidade: Salvamento de locais como favoritos
- Unitário: validar adição e exlusão de items da lista de favoritos
- Integração: verificar se os locais favoritos são salvos no banco
- Sistema: usuario seleciona o local, e adiciona como favorito
- Aceitação: o local continua na lista de favoritos, mesmo ao atualizar o app

### Funcionalidade: Corpatilhamento de experiencias
- Unitário: validar os campos da avaliação
- Integração: verificar se a avaliação é salva no banco com o restaurante certo
- Sistema: usuário seleciona o local desejado, e o avalia
- Aceitação: A avalição continua, mesmo ao atualizar o app

### Funcionalidade: Receber recomendações personalizadas
- Unitário: validar a lógica de recomendação com base nos favoritos e no histórico de buscas
- Integração: verificar se o sistema consulta o histórico do usuário para gerar as recomendações
- Sistema: usuário acessa a tela inicial do app e vê a lista de restaurantes recomendados
- Aceitação: o usuario recebe recomendações com base nos seus favoritos, ao inves de receber reccomendações aleatórias
---

## 3. Prioridades e Riscos

Alta prioridade:
- Login → sem login o usuário não usa o sistema
- Busca de restaurantes com filtro → sem a busca com filtro, o usuario precisaria saber o nome do local previamente, o que possivelmente o impediria de achar certos estabelecimentos  

Justificativa:
Falhas nessas áreas impedem o uso da plataforma.
Falhas nessas áreas agravam muito a experiencia do usuário

Baixa prioridade: 
- Favoritos → não impede uso
- Receber recomendações personalizadas → O usuário ainda pode achar seus restaurantes favoritos, mas tera mais trabalho
- Compartilhamento de experiências → não impede o uso básico, mas reduz o engajamento e a confiança dos usuários

Justificativa:
Falhas nessas áreas não impedem o uso da plataforma.

---

## 4. Pirâmide de Testes

- Maior foco: Testes unitários
- Médio foco: Testes de integração
- Menor foco: Testes de sistema e aceitação

Justificativa:
Os testes unitários são mais baratos, além de serem mais rápidos, o que acelera a detecção de erros. Já os testes de integração custam um pouco a mais, mas ajuda a validar se o app funciona em conjunto front-end + back-end. Os testes de sistema e aceitação são mais caros e demorados, seriam usados para validar os fluxos principais do app.

---

## 5. Testes em Produção

- Uso de feature flags e também monotorar erros
- Aplicar em busca de restaurantes e recomendações

Justificativa:
Testar em produção exige cuidado para não impactar todos os usuários. Feature flags permitem liberar funcionalidades gradualmente e reverter rápido se alguma coisa falhar. Monitoramento de erros ajuaria a identificar problemas em tempo real.
