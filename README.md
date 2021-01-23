# PokeTrader (Backend)

Backend para o simulador de trocas de Pokémons. O sistema avalia possíveis trocas
entre treinadores, informando se a mesma é justa ou não, a partir do valor de
`base experience` de cada Pokémon existente na troca. Os dados de uma troca
podem ser armazenados no sistema, permitindo visualização posterior.

## Endpoints

* **POST** - /api/users/register - Cadastra um novo usuário.
* **POST** - /api/users/signin - Autentica um usuário já existente.
* **GET** - /api/pokemons/<:name> - Recupera os dados de um Pokémon a partir de seu nome.
* **GET** - /api/trades/fairness?trainer1=<:exp1>&trainer2=<:exp2> - Informa se uma determinada troca é justa ou não.
* **POST** - /api/trades - Registra os dados de uma troca no sistema.
* **GET** - /api/trades - Recupera as trocas salvas por um usuário.
* **GET** - /api/trades/<:id> - Exibe os detalhes de uma troca salva específica.

## Instalação

É necessário ter o Docker e docker-compose instalados.

Para executar o projeto, rodar o comando `docker-compose -f docker-compose-dev.yml up`.

Caso sejam realizadas alterações nas models do banco de dados, deve se rodar os comandos:

```
docker-compose -f docker-compose-dev.yml run base python manage.py db migrate

docker-compose -f docker-compose-dev.yml run base python manage.py db upgrade
```

Para executar os testes da aplicação, executar o comando `docker-compose -f docker-compose-dev.yml run base python manage.py test`.