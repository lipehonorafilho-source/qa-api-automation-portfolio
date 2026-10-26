# Projeto 1 — Testes de API com Postman | API Testing with Postman

**PT-BR:** Projeto de portfólio para demonstrar testes manuais de API REST com Postman.  
**EN:** Portfolio project demonstrating manual REST API testing with Postman.

## Objetivo | Goal
- Validar códigos HTTP, estrutura JSON, tipos de dados e regras básicas de resposta.
- Validate HTTP status codes, JSON structure, data types, and basic response rules.

## API utilizada | API used
Este projeto usa a API pública de demonstração **JSONPlaceholder** (`https://jsonplaceholder.typicode.com`). Ela simula recursos REST para fins de estudo; não é um sistema de produção e não persiste todos os tipos de escrita como uma API real.

This project uses the public demo API **JSONPlaceholder** for learning. It simulates REST resources; it is not a production system and does not persist all write operations like a real API.

## Escopo de testes | Test scope
1. `GET /posts/1` — retorno de um post existente.
2. `GET /posts/999999` — retorno de recurso inexistente.
3. `GET /posts?userId=1` — filtro por usuário.
4. `POST /posts` — envio de um novo post simulado.
5. `GET /comments?postId=1` — comentários associados ao post.

## Como executar | How to run
1. Instale o Postman: https://www.postman.com/downloads/
2. Baixe ou clone este repositório.
3. No Postman, clique em **Import** e selecione `postman/qa-api-basics.postman_collection.json`.
4. Abra a coleção e execute os requests individualmente ou use **Run collection**.
5. É necessário acesso à internet para chamar a API.

## Critérios de aceitação | Acceptance criteria
- `GET /posts/1`: status `200`, JSON com `userId`, `id`, `title`, `body`; `id` deve ser `1`.
- `GET /posts/999999`: status `404` ou resposta vazia equivalente documentada pela API. A asserção da coleção espera `404`; se o serviço mudar, registre a diferença.
- `GET /posts?userId=1`: status `200`, resposta em array e todos os itens com `userId = 1`.
- `POST /posts`: status `201`, resposta contém o título enviado.
- `GET /comments?postId=1`: status `200`, array e cada item com `postId = 1`.

## Evidências sugeridas | Suggested evidence
Salve capturas de tela dos resultados do Postman em `evidence/`:
- execução da coleção com testes aprovados;
- resposta `GET /posts/1`;
- exemplo de falha intencional (por exemplo, altere temporariamente uma asserção e registre como teste negativo de ferramenta, depois reverta).

**Importante:** não inclua tokens, senhas ou dados pessoais em screenshots. Os resultados dependem da disponibilidade e do comportamento atual da API.

## Limitações | Limitations
- API pública de demonstração; sem SLA.
- Não são realizados testes de carga, segurança invasiva ou testes em dados reais.
- A API pode mudar; documente diferenças observadas em vez de forçar um resultado.

## Competências demonstradas | Skills demonstrated
REST, HTTP methods, status codes, JSON, assertions, test documentation, Postman collections.

## Estrutura | Structure
```text
01-api-postman/
├── README.md
├── postman/
│   └── qa-api-basics.postman_collection.json
└── evidence/
    └── .gitkeep
```
