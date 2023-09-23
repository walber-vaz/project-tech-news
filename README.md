# Projeto Traduzo

Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para a eletiva de Python do curso da Trybe.

## Requisitos

1 - MODEL - Instanciando idiomas

- [x] Crie uma classe `LanguageModel` que recebe init da class um dicionario `{"name": "afrikaans", "acronym": "af"}` e atribui a um atributo de instancia `self.language` o valor do dicionario passado como parametro.

2 - MODEL - Conversão atributo self.data para Dicionário

- [x] Crie um método `to_dict` que retorna um dicionario com os atributos da instancia.

3 - MODEL - Listagem de Idiomas como Dicionários

- [x] Crie um método de classe `list_dicts` que retorna uma lista de dicionarios com todos os idiomas cadastrados.

4 - CONTROLLER & VIEW - Endpoint Tradutor, renderizando variáveis do Backend - GET

- [x] Crie um método `index` que renderiza o template `index.html` com os seguintes parâmetros:
  - `languages`: Todos os idiomas disponíveis, que devem ser obtidos utilizando o método `LanguageModel.find()`;
  - `text_to_translate`: O texto que será traduzido ou a string "O que deseja traduzir";
  - `translate_from`: O idioma de origem da tradução;
  - `translate_to`: O idioma de destino da tradução;
  - `translated`: O texto já traduzido ou a string "Tradução".

5 - CONTROLLER - Tradução de Texto - POST

- [x] Crie um método `translate` que recebe uma solicitação POST e retorna o template `index.html` com os seguintes parâmetros:
  - `languages`: Todos os idiomas disponíveis, que devem ser obtidos utilizando o método `LanguageModel.find()`;
  - `text_to_translate`: O texto que será traduzido ou a string "O que deseja traduzir";
  - `translate_from`: O idioma de origem da tradução;
  - `translate_to`: O idioma de destino da tradução;
  - `translated`: O texto já traduzido ou a string "Tradução".

6 - CONTROLLER - Tradução Reversa - POST

- [x] Se você acessou a aplicação, deve ter visto no FrontEnd um botão para inverter a linguagem. Vamos implementar sua funcionalidade agora.

7 - TESTE - Histórico de Traduções

- [x] Crie o teste no arquivo tests/models/history/test_history_model.py

8 - Endpoint de Listagem de Histórico de Traduções - API GET

- [x] Crie um novo arquivo para a controller do endpoint, use as controllers já implementadas como referência.

9 - TESTE - Exclusão de Histórico de Traduções - DELETE

## Autor

- [Walber Vaz](https://www.linkedin.com/in/walber-vaz/)
