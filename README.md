# PCS3623-locadora-de-jogos
Aplicação desenvolvida para a disciplina PCS3623 - Banco de Dados da Poli-USP para o gerenciamento de banco de dados SQL de uma loja de aluguel de jogos de tabuleiro.

## Configuração do servidor
Criar um arquivo `config.json` na pasta `board_game_store` com o conteúdo:
```json
{
    "secret-key": "some long secret key",
    "database": {
        "host": "PostgreSQL host",
        "database": "PostgreSQL database",
        "user": "PostgreSQL user",
        "password": "PostgreSQL password"
    }
}
```
