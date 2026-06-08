## Como executar o projeto localmente

Primeiro, clone o repositório:

```bash
git clone https://github.com/GustavoMairinck/Atividades-CI-CD-LEDS-Academy
cd Atividades-CI-CD-LEDS-Academy
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

No Linux/macOS:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois disso, o projeto já estará pronto para ser executado localmente.

## Como rodar os testes

Para executar os testes unitários localmente, utilize o comando:

```bash
python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=70
```

Esse comando procura automaticamente os arquivos de teste dentro da pasta `tests/` e executa os testes definidos no projeto.

Exemplo de resultado esperado:

```text
collected 2 items

test_arquivoum.py::test_somar PASSED
test_arquivoum.py::test_eh_par PASSED

2 passed
```

## Como funciona o pipeline de CI

O workflow de integração contínua configurado fica no arquivo:

```text
.github/workflows/ci.yml
```

Esse pipeline é executado automaticamente nos eventos de `push` e `pull_request` para a branch `main`.

As etapas do pipeline são:

1. Clonar o repositório usando `actions/checkout@v4`;
2. Configurar o Python 3.12 usando `actions/setup-python@v5`;
3. Instalar as dependências do projeto a partir do arquivo `requirements.txt`;
4. Executar os testes unitários com o comando: `pytest --cov=src --cov-report=term-missing --cov-fail-under=70`


## Como interpretar os resultados da aba Actions

Na aba **Actions** do GitHub, é possível acompanhar a execução automática do workflow de testes.

Quando a execução aparece com status verde, significa que o pipeline foi executado com sucesso. Isso indica que as dependências foram instaladas corretamente, os testes passaram e a cobertura mínima exigida foi atingida.

Quando a execução aparece com status vermelho, significa que ocorreu algum erro durante o processo. Esse erro pode estar relacionado à instalação das dependências, falha em algum teste ou cobertura abaixo do mínimo definido.

## Cobertura atingida pelo projeto

A cobertura mínima exigida pelo workflow é de **70%**.

Neste projeto, a cobertura atingida foi de **100%**, pois todas as funções criadas na pasta `src/` foram testadas com sucesso.
