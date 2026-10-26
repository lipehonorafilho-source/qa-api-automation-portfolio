# Como publicar este portfólio no GitHub | Publish this portfolio

## Opção A — pelo site do GitHub (mais simples)
1. Acesse https://github.com e entre na sua conta.
2. Clique no botão `+` e escolha **New repository**.
3. Nome sugerido: `qa-api-automation-portfolio`.
4. Escolha **Public** para que recrutadores possam visualizar.
5. Como os arquivos já estão incluídos neste pacote, deixe desmarcada a opção de criar README automaticamente.
6. Crie o repositório.
7. Na página do repositório, escolha **Add file → Upload files**.
8. Descompacte este pacote no computador e arraste os arquivos e pastas para a página. Se a interface não aceitar uma pasta, entre nela e envie os arquivos, ou use a opção Git abaixo.
9. Escreva a mensagem `Add initial QA portfolio projects` e clique em **Commit changes**.
10. Abra o repositório e confira se o README e as três pastas aparecem.

> Dica: envie o conteúdo da pasta `portfolio_qa_github`, não o arquivo ZIP dentro do repositório.

## Opção B — usando Git no VS Code
1. Instale o Git: https://git-scm.com/downloads
2. Extraia o ZIP para uma pasta local.
3. Abra essa pasta no VS Code.
4. Abra **Terminal → New Terminal**.
5. Execute os comandos abaixo. Substitua `SEU-USUARIO` pelo seu nome de usuário real do GitHub.

```bash
git init
git add .
git commit -m "Add initial QA portfolio projects"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/qa-api-automation-portfolio.git
git push -u origin main
```

Se o Git solicitar identificação e ela ainda não estiver configurada:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"
```
Use um e-mail que você queira associar aos commits. Para autenticar no GitHub, siga o fluxo de login solicitado pelo Git Credential Manager; não coloque senha ou token dentro dos comandos.

## Antes de publicar
- Rode os testes localmente e atualize os READMEs se observar diferenças.
- Não publique `.venv`, senhas, tokens, chaves ou dados pessoais.
- Troque os exemplos por evidências capturadas por você; não apresente screenshots fictícias como execução real.
- Mantenha o repositório público se quiser facilitar a avaliação por recrutadores.
- Escreva no perfil do GitHub que são projetos de estudo/portfólio.

## Comandos rápidos de validação
Projeto 2:
```bash
python -m pip install -r requirements.txt
pytest -v
```
Projeto 3:
```bash
python -m pip install -r requirements.txt
pytest -v
```
