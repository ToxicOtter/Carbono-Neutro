
# Carbono Zero

Um site que tem como intuito calcular a quantidade de toneladas de carbono emitidas por uma pessoa ou empresa anualmente. Como diferencial, apresenta o cálculo de área de um arquivo com extensão KML, indicando se no terreno selecionado será possível compensar o carbono emitido.  
Optou-se pelo uso do Python, com o pacote Flask, como backend pela flexibilidade que a linguagem possui. Desse modo, é possível calcular todas as variáveis necessárias e hospedar o site simultaneamente.  
Durante o desenvolvimento encontrou-se dificuldades em lidar com o Flask e todas as suas peculiaridades, além de apresentar os resultados dos cálculos visualmente.


## Instalação

#### Para executar o código localmente, faz-se necessário a Instalação do Python, criação de um *virtual enviromment*, e Instalação de algumas bibliotecas.  
#### Recomendamos o uso do Visual Studio Code como *IDE*, pois foi usado no desenvolvimento. 

Python
```
Instale a versão 3.10 em https://www.python.org/downloads/
```

Criação do *virtual enviromment*
```py
    #MacOs/Linux
    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv

    #Windows
    > mkdir myproject
    > cd myproject
    > py -3 -m venv venv
```

Ativação do *virtual enviromment*
```py
    #MacOs/Linux
    $ . venv/bin/activate

    #Windows
    > venv\Scripts\activate
```

#### Com o *virtual-env* funcionando, instale os pacotes necessários:

Flask
```py
    pip install Flask
```
Geopandas
```py
pip install geopandas
```
Shapely
```py
pip install shapely
```
Fiona
```py
pip install Fiona
```
Pyproj
```py
pip install pyproj
```

#### Observação: Encontramos dificuldades de instalar alguns dos pacotes por meio do pip. Caso o problema apareça, recomendamos baixar os pacotes por meio desse link:
```py
https://www.lfd.uci.edu/~gohlke/pythonlibs/
```
## Como usar
Com todos os requisitos instalados, basta executar o comando abaixo com o *virtual-env* aberto e abrir no navegador o caminho descrito.

```py
    flask --app server run
```
## Autores

- [@ToxicOtter](https://github.com/ToxicOtter)
- [@IsaacKralik](https://github.com/IsaacKralik)
- [@João](https://www.linkedin.com/in/joão-cardoso-769a531b9/)