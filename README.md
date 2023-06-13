# Título do Projeto
Manguefy
# Descrição do Projeto

Este é um projeto criado com o intuito de oferecer para o grande público mais conhecimento e a disseminação do movimento Manguebeat que surgiu na cidade do Recife, em 1992. O projeto foi desenvolvido em Python e utiliza a biblioteca Google Maps para criar rotas e visualizar no mapa com o uso do pacote folium. Neste código o usuário faz o cadastro, ou não, com acesso às telas para permitir a geolocalização dele e assim começar a escolher a rota para o passeio. Ainda escolhe que tipo de meio de transporte ele quer, e se vai escolher alguma rota pré-definida ou escolher uma rota personalizada.

# Requisitos

- Python 3.11.4
- Chave API válida do Google Maps

**Pacotes python:**
- googlemaps
- folium
- polyline
- python-dotenv
- time
- os

# Instalação

## Python

1. Certifique-se de ter o Python 3.11.4 instalado em seu sistema. Você pode baixar o Python em [python.org](https://www.python.org/downloads/).

## pip

1. A biblioteca 'pip' é um gerenciador de pacotes do Python que permite instalar bibliotecas e pacotes de terceiros de forma fácil e rápida. A maioria das distribuições do Python já inclui o 'pip' por padrão. No entanto, se você estiver usando uma versão mais antiga do Python que não inclui o 'pip', ou se você o removeu acidentalmente, você pode seguir as etapas abaixo para instalá-lo:

2. Verifique a versão do Python instalada em seu sistema digitando o seguinte comando no terminal ou prompt de comando:
```sh
python --version
````
  Certifique-se de que a versão exibida seja 2.7.9 ou superior para Python 2, ou 3.4 ou superior para Python 3.
2. Acesse o site oficial do Python Package Index (PyPI) em [pypi.org/project/pip](https://pypi.org/project/pip/) e clique no botão "Files" para baixar o arquivo de instalação do 'pip'. Selecione o arquivo apropriado para sua versão do Python e seu sistema operacional (por exemplo, 'get-pip.py' para Windows).

3. Salve o arquivo 'get-pip.py' em um local conveniente em seu computador.

4. Abra o terminal ou prompt de comando e navegue até o diretório onde você salvou o arquivo 'get-pip.py'.

5. Execute o seguinte comando para instalar o ‘pip':
```sh
python get-pip.py
```
6. O 'pip' será instalado e estará pronto para uso. Após a instalação do 'pip', você poderá usá-lo para instalar bibliotecas e pacotes Python adicionais executando o comando 'pip install' seguido do nome da biblioteca que você deseja instalar. Por exemplo:
```sh
pip install nome_da_biblioteca
```
Certifique-se de substituir "nome_da_biblioteca" pelo nome real da biblioteca que você deseja instalar.

Exemplo biblioteca googlemaps:
```sh
pip install googlemaps
````

Certifique-se de ter uma conexão com a internet durante a instalação, pois o comando 'pip' buscará e instalará as bibliotecas a partir do repositório Python Package Index (PyPI).

Se você encontrar algum problema durante a instalação, verifique se o Python está corretamente configurado em seu sistema e se você tem privilégios de administrador para instalar pacotes.

## Chave de API válida do Google Maps

1. Renomeie o arquivo “.env.example” para “.env”
2. Configure sua chave de API do Google Maps no arquivo “.env”. Você pode obter uma chave seguindo as instruções na [documentação oficial do Google Maps](https://developers.google.com/maps/gmp-get-started).
Forma correta do arquivo ".env":
![imagem_env](https://i.ibb.co/9ZV5WwB/code.png)

# Utilização

Para iniciar a aplicação você deve digitar a seguinte linha em seu console na pasta principal da aplicação:
```sh
python main.py
```

Ao iniciar irá aparecer a logo do Manguefy e em seguida outra tela explicando sobre o mesmo, onde você deverá apertar a tecla ENTER para prosseguir.

Após clicar ENTER você deverá ver o seguinte menu onde você deverá escolher a opção a qual melhor serve o seu caso no momento:
```sh
------ Tela Menu Principal  -------

1. Cadastrar-se

2. Continuar sem cadastro

3. Entrar

4. Sair

-----------------------------------
Escolha uma opção: 
```

Quando você escolher uma opção o aplicativo mostrará outro menu subsequente sobre o que você escolheu e você deve seguir as instruções do próprio aplicativo para prosseguir com a utilização.

Nossa aplicação é bem descritiva em suas telas, portanto é só ler com atenção que você conseguirá utilizar ela sem nenhum problema!