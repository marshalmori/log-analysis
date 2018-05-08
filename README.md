
# Análise de Logs
Essa aplicação em Python e SQL, faz a análise de logs e informações contidas em algumas tabelas de uma banco de dados Postgres.

## Instalação
Abaixo temos os passos necessários para conseguir rodar esta aplicação:


1. **Instalar o Postgresql** - de acordo com o seu sistema operacional, consulte [este link](https://www.postgresql.org/download/) e instale o Postgresql.
2. **Download do projeto** - basta fazer um clone, fork ou download desse projeto, direto para sua máquina.
3. **Download arquivo SQL** - baixe o arquivo [newsdata.sql](https://drive.google.com/file/d/1PQjt7EZUyWXg0JVEBpSqhXt42jXOsUW0/view?usp=sharing) e coloque na pasta principal.
4. **Configurar o acesso ao banco** - acesse o projeto principal, abra o arquivo `app.py`. Procure pelo código abaixo e edite os campos `<seu_usuario>` e `<sua_senha>`, respectivamente com usuário e senha configurados no Postgresql.

    * `Database.initialise(database="news",
                        user="<seu_usuario>"",
                        password="<sua_senha>",
                        host="localhost")`


5. **Criar o Bando de Dados** - o nome do banco de dados será **news**, para fazer isso, utilize o terminal, acesse a pasta onde se encontra o arquivo **newsdata.sql** e execute o comando abaixo:
    * `$ create news; psql -d news -f newsdata.sql`

    Feito isso será criado um banco de dados no Postgresql chamado news e constituído de 3 tabelas: `authors`, `articles` e `log`.

6. **Criar uma virtualenv** - fora da pasta do projeto crie uma virtualenv e instale o pacote `psycopg2` para o Python poder trabalhar com o Postgresql. Para fazer isso, acesso o terminal e faça os seguintes passos: (Obs.: Para esses passos, é necessário ter a virtualenv e o pip instalados)
    * `$ virtualenv venv`
    * `$ source venv/bin/activate`
    * `$ pip install psycopg2`

## Como rodar o programa
Acesse a pasta do projeto e execute o comando `$ python app.py`. Feito isso será apresentado no terminal as respostas as seguintes perguntas:

  1. **Quais são os três artigos mais populares de todos os tempos?**
  2. **Quem são os autores de artigos mais populares de todos os tempos?**
  3. **Em quais dias mais de 1% das requisições resultaram em erros?**

Além desses resultados apresentados no terminal, também será gerado um arquivo chamado `log_file.txt` com os mesmos resultados mostrados no teminal.

## Licença
O projeto Análise de Logs foi lançado com a licença [MIT
license](https://github.com/atom-community/markdown-preview-plus/blob/master/LICENSE.md).
