# Projeto 2 — Testes automatizados de API com Python e Pytest | API Automation

**PT-BR:** Testes automatizados de API REST usando Python, `requests` e `pytest`.  
**EN:** REST API automated tests using Python, `requests`, and `pytest`.

## Objetivo | Goal
Praticar automação de testes HTTP, validação de status codes, estrutura de dados e filtros de API.
Practice HTTP test automation, status-code checks, response schema basics, and API filtering.

## Pré-requisitos | Prerequisites
- Python 3.10 ou superior / Python 3.10+
- pip
- Internet access / acesso à internet

## Instalação | Setup
No terminal, entre nesta pasta e execute:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

**Windows PowerShell**
```powershell
.venv\\Scripts\\Activate.ps1
```

**Windows CMD**
```bat
.venv\\Scripts\\activate.bat
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Instale as dependências:
```bash
python -m pip install -r requirements.txt
```

## Executar testes | Run tests
```bash
pytest -v
```

Para gerar um relatório JUnit XML:
```bash
pytest -v --junitxml=reports/junit.xml
```
A pasta `reports/` já existe. O arquivo do relatório é gerado localmente e pode ser commitado se fizer sentido para a demonstração, mas normalmente é melhor não versionar relatórios temporários.

## Cenários cobertos | Covered scenarios
- Buscar post existente e validar campos.
- Buscar coleção de posts e validar tipo da resposta.
- Filtrar posts por `userId`.
- Consultar recurso inexistente.
- Tratar timeout e falhas de conexão de forma explícita no cliente de teste.

## Boas práticas | Good practices
- Os testes usam `timeout` para evitar espera infinita.
- Falhas de rede são relatadas como falha do teste, não confundidas com defeito funcional da API.
- A API é pública e pode ficar indisponível ou alterar comportamento.
- Não são feitos testes de carga nem chamadas destrutivas.

## Estrutura | Structure
```text
02-api-python-pytest/
├── README.md
├── requirements.txt
├── pytest.ini
├── tests/
│   └── test_posts_api.py
├── reports/
│   └── .gitkeep
└── .gitignore
```

## Competências demonstradas | Skills demonstrated
Python, pytest, requests, assertions, parametrization, API validation, test reporting.
