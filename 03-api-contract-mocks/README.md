# Projeto 3 — Validação de contrato de API e mocks | API Contract & Mock Testing

**PT-BR:** Projeto de testes unitários para validar o contrato de uma API e simular respostas externas com mocks.  
**EN:** Unit-testing project that validates an API contract and simulates external responses using mocks.

## Por que este projeto? | Why this project?
Nem todo teste precisa depender de uma API online. Mocks permitem testar como o código reage a respostas válidas, erros HTTP e falhas de conexão de maneira repetível.
Not every test should depend on an online API. Mocks help test how code responds to valid responses, HTTP errors, and connection failures reliably.

## Pré-requisitos | Prerequisites
- Python 3.10+
- pip

## Instalação e execução | Setup and run
```bash
python -m venv .venv
```

Ative o ambiente virtual conforme seu sistema operacional e depois:
```bash
python -m pip install -r requirements.txt
pytest -v
```

**Este projeto não precisa de internet para rodar os testes.**  
**This project does not require internet access to run its tests.**

## O que é testado? | What is tested?
- Normalização de uma resposta de usuário.
- Validação de campos obrigatórios.
- Conversão de resposta HTTP em erro de domínio.
- Simulação de resposta bem-sucedida com `unittest.mock`.
- Simulação de timeout e falha de conexão.

## Estrutura | Structure
```text
03-api-contract-mocks/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/
│   └── api_client.py
├── tests/
│   └── test_api_client.py
└── .gitignore
```

## Competências demonstradas | Skills demonstrated
Python, pytest, unittest.mock, test isolation, exception handling, contract validation, deterministic tests.
