# 📝 To Do Notes

> Sistema simples, moderno e eficiente para organizar sua rotina diária com listas de tarefas e notas em texto — acesse de onde você estiver.

![Tela inicial da página](img/home.png)

🌐 **Aplicação em Produção:** [https://to-do-notes.onrender.com/](https://to-do-notes.onrender.com/)

---

## 💡 Sobre o Projeto

O **To Do Notes** nasceu como um projeto pessoal para centralizar anotações rápidas e gerenciamento de tarefas do dia a dia. Recentemente modernizado, conta com:
- **Tema Claro e Escuro (Dark Mode)** nativo via Bootstrap 5.3 com persistência automática no navegador.
- **Gerenciamento de dependências ultra-rápido** utilizando o [Astral uv](https://github.com/astral-sh/uv) e `pyproject.toml`.
- **Pipeline de CI/CD** no GitHub Actions com checagem de integridade, validação de migrações e suite de testes unitários automatizados.
- **Hospedagem em nuvem** com deploy automatizado via Render e banco de dados PostgreSQL via Supabase.

---

## ✨ Principais Funcionalidades

- 🌓 **Alternador de Tema (Light / Dark / Auto)**: Permite escolher entre tema claro, escuro ou acompanhar automaticamente a preferência do seu sistema operacional, sem cintilação ao recarregar a página.
- 📋 **Gerenciador de Tarefas**: Crie tarefas com prazos definidos por um calendário interativo ou deixe o prazo em aberto (opcional). Conclua, edite ou exclua tarefas com facilidade.
- 📄 **Bloco de Notas**: Escreva ideias, listas de estudos e textos longos com formatação limpa de parágrafos e contagem de caracteres.
- 🔒 **Contas Individuais Seguras**: Cada usuário possui seu próprio espaço isolado de tarefas e notas, com fluxo de cadastro, login e recuperação de senha por email.

---

## 🧭 Fluxo de Uso e Guias Passo a Passo (How-Tos)

### 1. Como Criar uma Conta (Cadastro)
1. Na barra de navegação superior, clique no botão **Entrar** ou acesse a página inicial e selecione qualquer funcionalidade.
2. Na tela de login, clique no link **"Não tem uma conta? Cadastre-se"** (ou acesse diretamente `/signup`).
3. Preencha os campos:
   - **Nome de usuário**: Seu identificador único no sistema.
   - **Email**: Endereço de email válido (utilizado caso precise redefinir sua senha).
   - **Senha** e **Confirme a Senha**: Defina uma senha segura com no mínimo 8 caracteres (evite senhas comuns ou puramente numéricas).
4. Clique em **Cadastrar**.
   > **Dica de UX:** Se alguma regra de validação não for atendida (como uma senha muito curta), o sistema exibirá os apontamentos em um único banner consolidado e **manterá seu nome de usuário e email preenchidos**, para que você precise apenas redigitar a senha.
5. Após o cadastro com sucesso, você será redirecionado para a tela de login.

---

### 2. Como Criar e Gerenciar Tarefas
1. Faça login na sua conta e clique em **Tarefas** no menu superior (ou no botão **"Minhas Tarefas"** na página inicial).
2. Para adicionar uma nova tarefa, clique no botão **"Adicionar Tarefa"**.
3. Preencha os dados:
   - **Título**: O nome ou descrição da atividade a ser realizada.
   - **Prazo (Opcional)**: Clique no campo para abrir o **seletor interativo em calendário** e escolher a data limite. Se a tarefa não tiver prazo fixo, pode deixar este campo em branco.
4. Clique em **Salvar**.
5. **Gerenciando na Tabela de Tarefas**:
   - **Concluir**: Clique no botão azul **Concluir** para marcar a tarefa como finalizada com a data de hoje. O botão será desativado automaticamente para tarefas concluídas.
   - **Editar**: Clique no botão cinza **Editar** para alterar o título ou a data de entrega.
   - **Excluir**: Clique no botão vermelho **Excluir** e confirme para remover a tarefa definitivamente.
   - *Ordenação inteligente*: Suas tarefas com prazo mais próximo aparecem primeiro; tarefas sem prazo fixo ficam organizadas ao final da lista pela data de criação.

---

### 3. Como Criar e Organizar Notas
1. No menu superior, clique em **Notas** (ou no botão **"Minhas Notas"** na página inicial).
2. Para criar uma nova anotação, clique em **"Nova Nota"**.
3. Preencha:
   - **Título**: Um identificador para o assunto da nota.
   - **Conteúdo**: O texto da sua nota (suporta até 10.000 caracteres e múltiplas quebras de linha).
4. Clique em **Salvar**.
5. **Visualizando e Gerenciando Notas**:
   - Na listagem de notas em formato de cards, você verá um resumo com os primeiros caracteres e a data de criação.
   - Clique em **"Ver Detalhes"** para abrir a visualização completa, formatada com indentação de parágrafos e tipografia legível.
   - Pelos cards ou pela tela de detalhes, você também pode **Editar** ou **Excluir** a nota quando desejar.

---

### 4. Como Alternar o Tema Visual
- No canto direito da barra de navegação, clique no ícone circular de tema:
  - ☀️ **Claro**: Fundo claro e alto contraste para ambientes iluminados.
  - 🌙 **Escuro**: Tons escuros confortáveis para leitura noturna e economia de bateria.
  - 🌓 **Automático**: Sincroniza a interface em tempo real com as preferências do seu dispositivo.
- Sua escolha fica salva no navegador (`localStorage`) para que você não precise escolher novamente a cada página acessada.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Ferramenta / Biblioteca | Descrição |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.12+ | Linguagem principal do ecossistema backend |
| **Framework Web** | Django 5.2 | Arquitetura robusta MVC com ORM, autenticação e views genéricas |
| **Frontend & Estilo** | Bootstrap 5.3 + Bootstrap Icons | Interface responsiva com suporte nativo a `data-bs-theme` |
| **Formulários** | Django Crispy Forms & Crispy Bootstrap 5 | Renderização semântica e acessível de formulários |
| **Gerenciador de Pacotes** | Astral `uv` | Gerenciamento ultrarrápido com `pyproject.toml` e `uv.lock` |
| **Banco de Dados** | SQLite (Dev) / PostgreSQL (Prod) | Configurado via `dj-database-url` e Supabase |
| **Arquivos Estáticos** | WhiteNoise | Compressão e distribuição eficiente de arquivos estáticos em produção |
| **Servidor WSGI** | Gunicorn | Servidor HTTP de produção para aplicações Python |
| **CI / CD** | GitHub Actions | Pipeline automatizada de testes, validação de migrações e deploy |
| **Hospedagem** | Render | Plataforma de cloud hosting com integração contínua |

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- **Python 3.12+** instalado.
- **[uv](https://docs.astral.sh/uv/)** instalado (recomendado) ou Python `venv` padrão.
  ```bash
  # Instalação do uv (Linux/macOS)
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MuriloBarros304/to-do-notes.git
   cd to-do-notes
   ```

2. **Crie o ambiente virtual e sincronize as dependências:**
   ```bash
   uv sync
   ```

3. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto com as chaves necessárias:
   ```env
   SECRET_KEY="sua-chave-secreta-de-desenvolvimento"
   DEBUG=True
   ALLOWED_HOSTS="127.0.0.1,localhost"
   DATABASE_URL="sqlite:///db.sqlite3"
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   uv run python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   uv run python manage.py runserver
   ```
   Acesse a aplicação no navegador em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

6. **Execute os testes automatizados:**
   ```bash
   uv run python manage.py test
   ```

---

## 🚢 Deploy no Render

O projeto está pronto para deploy no **Render** com `uv`:

- **Build Command**:
  ```bash
  ./build.sh
  ```
  *(ou `uv sync --locked && uv run python manage.py collectstatic --no-input && uv run python manage.py migrate`)*
- **Start Command**:
  ```bash
  uv run gunicorn setup.wsgi:application
  ```

---

## 👨‍💻 Autor

Desenvolvido por **Murilo Barros**  
- GitHub: [@MuriloBarros304](https://github.com/MuriloBarros304)  
- Repositório: [https://github.com/MuriloBarros304/to-do-notes](https://github.com/MuriloBarros304/to-do-notes)
