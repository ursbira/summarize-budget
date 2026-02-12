# summarize-budget

Project Name   : summarize-budget
Version        : 0.1
Start Date     : 08/02/2025
Project Git    : https://github.com/ursbira/summarize-budget
Author         : Ubiratan Rocha da Silva
Email          : urs.bira@gmail.com

### Descrição do projeto


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.14+](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/)
[![Tool: uv](https://img.shields.io/badge/Tool-uv-663399.svg)](https://github.com/astral-sh/uv)


**Description**
Ler arquivos excel com extensão .xlsx e capturar informações de células em linhas específicas,
                 gravando-as ao final em um novo arquivo .xlsx em formato de uma tabela e gera um arquivo de LOG
                 utilizando logging.

### Objetivo do Projeto

**Objective**

Conseguir ler o orçamento em arquivos excel .xlsx exportados à partir do DRG 2.0,onde cada
arquivo corresponde a um Centro de Custo, ler as linhas e culunas com as informações
orçamentárias e exportar para o arquivo excel final em um formato de tabela com as mesmas colunas
que existem na colunas [A] a [J] da guia [Dados] do DRG 2.0. Com este arquivo final deve ser
possível Copiar os dados desta Tabela criada e colar diretamente na guia [Dados] do DRG 2.0 e
passar a ter o Orçamento Anual de todos os departamentos cujos arquivos sejam lidos.

**What solves it?**

Passamos a Copiar e Colar os dados do orçamento anual dos centro de custo ao invés de digitar.

**How**

Ler as linhas e as colunas definidas, guardando seus valores em palavras chaves pré definidas,
podendo haver tratamento específico para dadas colunas e salvando-as em um dataframe pandas,
e ao final gravar um arquivo .xlsx.

### Controle de Versão e Boas Práticas

**Version Control**

`uv Versão: uv 0.9.26 (ee4f00362 2026-01-15)`

**Best practices**

Escrever o código utilizando as melhores práticas de programação, PEP8, jeito pythonico: legível, simples e conciso
Evitar utilizar parâmetros ou biblotecas obsoletos ou que vão entrar em obsolescência ou que já tenha consolidado
um jeito mais moderno, mais parecido com o python 3.14.

**Modular Code**

Vamos fazer o código python de forma modular, na pasta do projeto já tem uma pasta chamada `package` e nela tem que 
haver um `__init__.py` que deve inicializar o que for preciso e conter com os valores a serem exportados `__all__ = []`.
Nesta pasta deve haver um programa chamado `funcger.py` para funcões gerais do programa como ler o arquivo de configuração
e que vai ler os dicionários externos de uso geral e outros módulos como por exemplo um para as funções que vão tratar das linhas
um outro módulo para tratar dos dicionários internos e que vai conter todos os dicionários internos, um módulo somente para a GUI
e outros que se fizerem necessários.

### Estrutura do projeto

**Structure Start**

Estrutura inicial básica (não definitiva) sugerida

summarize-budget/
├── bases/              # Arquivos .xlsx de entrada
├── doc/                # prompt.md que definiu o problema e apresentou uma solução e leia-me.txt
├── logs/               # Arquivo de log configproject.log
├── output/             # Onde o arquivo final será gerado
├── package/
│   ├── __init__.py     # Inicialização e __all__
│   ├── constants.py    # Dicionários (Empresas, Centros de Custo, Contas)
│   ├── funcger.py      # Funções gerais (leitura de config, logs)
│   ├── parser.py       # Lógica de extração das linhas do Excel
│   └── messages.py     # Cadastro das mensagens de interação com o usuário e o log.
├── main.py             # Programa principal
├── pyproject.toml
├── README.md
├── uv.lock
└── .gitignore

### Editor, GUI e Build

**Soft Components**

`Liguagem Python 3.14 ou superior, Microsoft Windows 11 Pro, PowerShell: v7.5.4`

**Editor**

`VSCode, Versão: 1.109.0 (user setup) Data: 2026-02-04T02:01:38.288Z`

**GUI**

Nesta fase não teremos uma *GUI* (*Graphical User Interface*), mas todo o projeto já será estruturado para ao final desenharmos
uma janela com a biblioteca `'customtkinter'` na última versão que estiver disponível.

**Build**

Programa será, ao final, convertido para .exe com o pyinstaller, e na versão final irei colocar ícone e poderei colocar imagens.
linha que será utilizada para compilar
`uv run pyinstaller --onefile --name SummarizeB --log-level INFO --noconsole --add-data "favicon.ico;." --add-data "logo_1.png;." --add-data "logo_version.png;." main.py`
Onde os arquivos .ico e .png ainda serão definidos.

**Processador**
`11th Gen Intel(R) Core(TM) i7-11700F @ 2.50GHz (2.50 GHz)`

**RAM instalada**
`32,0 GB (utilizável: 31,8 GB)`

### Como as Funções Serão Estruturadas

**Structure Functions**

Todas as funções que forem criadas devem seguir o padrão de usar a docstring e definir as 
variáveis e o return. É usar Type Hinting e Docstrings rigorosas.
Segue um exemplo simplório:

```
def is_valid_file(file_path: Path, expected_extension: str) -> bool:

Verifica se o caminho é um arquivo válido, se existe e se possui
a extensão desejada.
Args:
    file_path: Objeto Path do arquivo.
    expected_extension: String com a extensão (ex: '.xlsx', '.csv').
```

Então neste caso a função is_valid_file sempre vai retornar um bool.
A Função tem um texto de documentação
Os argumentos estão com os tipos definidos e documentados

### Sobre os Centros de Custo nos arquivos de entrada

**Cost Centers**

Os Centros de Custos são os departamentos da empresa como foram denominados na Contabilidade.
Para cada Centro de Custo há uma guia no DRG 2.0 com um nome imutável, estes centros de custo
depois de preenchido pelo Consultor da Linkie Consultoria Empresarial e aprovado pela Diretoria
da empresa, cliente da Linkie, é exportado e salvo como uma planilha independente e com os
vínculos quebrados em relação à planilha DRG 2.0 de origem, o que congela o cenário aprovado
pela diretoria e validado pelo Consultor Linkie.

Normalmente é salvo um arquivo para cada um dos departamentos:
```
'Veículos Novos', 'Seminovos', 'Venda Direta',
'Consórcio', 'Licitação', 'Veículos Assinatura',
'Locação', 'Peças', 'Acessórios',
'Assistência Técnica', 'Funilaria e Pintura',
'Administração', 'Diretoria'.
```

Não ocorrem todos estes departamentos, obrigatoriamente, em todas as empresas e há casos especiais
como ao invés de ter o departamento 'Seminovos' existe os departamentos 'Seminovos Showroom' e
'Seminovos Repasse' que segmenta a venda dos veículos seminovos, e 'Venda Direta' pode estar
também segmentado em 'Venda Governo', 'VD Big' e 'VD Small', e se a empresa tiver um prédio separado
que serve de showroom para exposição e venda de veículos pode have uma departamento com um nome
específico de cada empresa que normalmente é o nome deste showroom filial como por exemplo:
'Venda Jorge Amado' onde Jorge Amado é o nome da rua onde o prédio fica.
Um outro caso comum é que o departamento 'Peças' refere-se à venda de Peças e Acessórios, não havendo
na maioria dos casos o departamento 'Acessórios' e é comum o nome do departamento ser chamado de
'Peças e Acessórios'.

Outra variação importante é que em uma empresa o nome do departamento está 'Peças' e na outra 'Pecas';
ou 'Seminovos' e 'Semi Novos' ou ainda 'Semi-Novos' ou 'Veículos Usados' ou 'Veiculos Usados';
e 'Assistência Técnica' pode ser 'Mecânica' ou 'Oficina' ou ainda 'Oficina Mecânica'.

Além de que estas variações podem estar totalmente com letras maiúsculas ou minúsculas.

Outra ocorrência é que um departamento pode estar desmembrado em dois centros de custo sem que seja para
segmentar as vendas, como por exemplo o departamento de 'Assistência Técnica' pode ter dois centros de
custo, um com o nome de 'Mecânica' e o outro 'Mecânica Adm', onde eles colocam no 'Mecânica' todos os 
lançamentos referentes aos produtivos, ou seja, quem realmente repara os veículos e no 'Mecânica Adm' os
demais funcionários como gestores, consultores técnicos, recepcionista, encarregado de garantia etc.

Em geral, o mais comum é ter os departamentos: 'Veículos Novos', 'Seminovos', 'Venda Direta', 'Peças',
'Assistência Técnica' e 'Administração'.

Importante salientar que, se por exemplo, a empresa não tem o departamento de 'Venda Direta', não significa
que ela não venda veículo por esta modalidade, ela apenas não tem interesse de acompanhar separadamente ou o
volume de vendas não tem a quantidade que justifique ter um departamento à parte, nestes casos as vendas por
esta modalidade de venda direta é efetuada e contabilizada dentro do departamento de 'Veículos Novos'.

Esta mesma situação ocorre com o departamento de 'Acessórios' que é incorporado pelo departamento de 'Peças';
pelo mesmo motivo 'Funilaria e Pintura' pode ficar dentro de 'Oficina Mecânica'.

**SUGESTÃO DE SOLUÇÃO**

Como resolvemos esta variedade de nomes: para cada empresa que o programa for ler tem
que ter um dicionário que contenha todos os departamentos que serão lidos, por exemplo
o nome 'Veículos Novos': 'VEICULOS NOVOS' onde a chave é o equivalente ao departamento
que está sendo processado e o valor é o nome definido pela contabilidade da empresa e
que será gravado no arquivo excel .xlsx final.
Este Dicionário deve ficar em um arquivo `configproject.json` como fizemos para o projeto
`omni_clean_report_urs` recentemente.

# Como são os arquivos de entrada

**Input Data**

Os dados nos arquivos excel com extensão `.xlsx` tem todos o mesmo padrão, mas a depender do departamento pode
conter mais ou menos linhas o que pode fazer por exemplo que a 'Despesa com Pessoal' que está em um departamento
em uma linha no outro estará em outra linha.

Existem algumas linhas que só existem nos departamentos que vendem veículos, como por exemplo: 'Comissão de Financiamento'.

Pode ocorrer que em uma mesma linha em um departamento refeira-se ao volume de vendas e esta mesma linha em outro
seja a quantidade de passagem na oficina.

Existem algumas informações auxiliares que constam nestes arquivos que apesar de não serem necessárias para serem gravadas
no arquivo final de saída, são importantes e devem ser coletadas, mesmo que nas primeiras versões não sejam utilizadas
poderão ser utilizadas no futuro para ao gerar um arquivo excel com extensão .xlsx possamos também gerar um arquivo .html
com um texto que descreva um resumo do que e como os valores foram orçados, o exemplo disso á célula no arquivo excel que
defini o 'projeção de crescimento' das vendas para o ano orçado, e podemos citar ainda, sem esgotar todas as possibilidades:
percentual de vendas de seminovos em relação a venda de novos, índice médio de acessórios, percentual de despesas com
pessoal em relação ao faturamento etc.

Apesar destas planilhas serem utilizadas para elaborar o orçamento do próximo ano, em algumas linhas as informações são
sobre o realizado no ano anterior, e mesmo que, nesta primeira versão não venhamos a definir quais linhas são estas para
que elas possam ser lidas elas serão incluídas em versões posteriores para também serem utilizadas na geração dos texto
`.html`, e possivelmente, também serão gravadas no arquivo excel com extensão `.xlsx`, mesmo que não sejam copiadas e coladas
na guia `[Dados]` do **DRG 2.0** elas poderão auxiliar a que por exemplo uma função leia o arquivo e gere um texto explicando
que: "... o faturamento total no ano anterior foi de R$ 13.456.789,01 que que o valor orçado é de XX.XXX.XXX,00
representando um crescimento de 8,95% o que permitirá em conjunto com uma margem de 7% obter uma margem de contribuição de
blá blá blá ...".

Todas as linhas tem informações dos dozes meses do ano numerados de 1 a 12.

Apesar dos arquivos terem as quantidades de linhas diferentes e nem todas as linhas serão lidas, todos tem as colunas
distribuídas da seguinte forma:

- `Coluna [A]` - Vazia, não precisa ler nada dela.
- `Coluna [B]` - Descrição da informação contida na linha.
- `Coluna [C]` - Coluna de Total para a maioria das linhas, mas em algumas são informações auxiliares como 'projeção de crescimento'.
- `Colunas [D:O]` - São os valores para cada um dos dozes meses do ano para cada linha- .

Importante salientar que em todos os arquivos a linha 1 sempre terá:
- `Célula [B1]` - Nome do departamento que deve ser lido e será usado no dicionário do qual já falamos no item 'Cost Centers'.
- `Célula [B2]` - Nome da empresa que deve ser lido e será usado no dicionário do qual já falamos no item 'Cost Centers'.
- `Célula [C3]` - Contém o ano para o qual o orçamento está sendo elaborado.
- `Célula [C17]` - Contém o ano Base cujos dados estão sendo utilizados para projetar o crescimento.
- `Células [D:O]` - Contém os números de 1 a 12 representando os meses do ano.

*SUGESTÃO DE SOLUÇÃO PARA TRATAR AS LINHAS*

**Teremos um dicionário:**

Para cada linha que formos definir que será lida teremos um nome para ela, exemplo: se a linha for o Faturamento teremos
o nome para ela 'Faturamento', se for a quantidade de veículos vendidos teremos o nome 'Volume de Vendas', se for a 
quantidade de veículos que passaram na oficina teremos 'Passagem na Oficina', se for o valor das despesas com funcionamento
teremos 'Despesa com Funcionamento' etc. Cada um destes termos estará descrito em uma dicionário e para cada um deles estará
associado o número da linha, tipo de dados que contém e um código de conta contábil, mais ou menos assim: '3.1.1.001.0001' para Receita de Veículos Novos etc.

Todas as contas que possam ser utilizadas já estarão anteriormente presentes em um dicionário chamada `standard_linkie_accounts`
que terá o código da conta em `code_account`, e a descrição em `description`, e valores string para:
`macro`, `micro`, `characteristic`, `category` e `class`

Podemos colocar alguns valores fictícios inicialmente, mas eu vou fornecer os valores corretos depois.

**Linhas Especiais**

Elas vão ficar com o código de conta contábil fixo '9999.9999.9999.001' a descrição vai ser o valor da coluna [B] descrito abaixo
acrescido de '(Valor ano anterior)'.

Um conjunto de linhas bem especiais são as descritas em `Realizadas no Ano Anterior`.

Este grupo de linhas não começam em todos os departamentos exatamente na mesma linha, mas elas têm o mesmo tipo de dados
somente a linha que descrevo abaixo como 'Receita xxx' que o nome muda conforme o departamento para 'Receita Veículos Novos'
'Receita sobre Cotas', 'Receita Mão de Obra', 'Receita Peças'

Elas têm os seguintes valores na coluna `[B]` onde a primeira linha é sempre 'REALIZADO NO ANO'
- Faturamento
- Receita xxx
- Descontos
- Devoluções
- Faturamento sem Encargos
- Custo Veículos Novos
- Margem Bruta
- Margem Bruta %
- Total Encargos
- Outras Receitas
- Result. Oper. Bruto (com O. Receitas)
- Total Despesa com Pessoal
- Total Despesa com Vendas
- Total Despesa com Ocupação
- Total Despesa com Funcionamento
- Total Geral Despesas
- Resultado Líquido Departamental
- Rateio de Despesa Administrativa
- Resultado Líquido Departamental

**Observação ERRATA**

Quando estava descrevendo os valores dos textos da coluna `[B]` para as linhas do 'REALIZADO NO ANO'
percebi que há alguns erros, como por exemplo em todos os departamentos a linha do 'Custo' está 
como 'Custo Veículos Novos' mesmo que o departamento não seja o de 'Veículos Novos' e a linha de
'Receita xxx' que deveria ter o 'xxx' substituído por algo que descreva o departamento, nem sempre
está correto, por exemplo no departamento de 'Veículos Seminovos' está como 'Receita Veículos Novos'.
Não vou corrigir isso por enquanto, mas vamos lembrar de considerar isso.
Assim que corrigir se tivermos colocado algo no código para tratar isso eu removo.

**SUGESTÃO DE SOLUÇÃO**

Diante da variedade de linhas para cada departamento devemos criar um dicionário com o nome de
todos os departamentos e para cada departamento chaves com o valor e o tipo de dado, exemplo:
```
'Veículos Novos': {
'Faturamento': [14, 'Valor em Reais com 2 casas decimais e separador de centavos a vírgula],
'Volume de Vendas': [12, 'Quantidade inteiro sem casas decimais']
}
```
Este dicionário pode ficar interno ao programa porque ele é imutável.

                 
# Procedimentos Específicos aplicados ao Projeto

**Data Processing**

Aqui eu vou descrever alguns procedimentos específicos para como os dados deverão ser tratados.

Mas temos que definir se as leituras dos dados dos departamentos nos arquivos serão efetuados por funções ou por classes, precisamos definir a melhor prática para esta situação.

**Columns Panda**

Aqui eu vou descrever se necessário as colunas no `dataframe Pandas` que poderão ter algum tratamento especial.

Nesta versão não necessitamos do `Pandas` todo o processo foi executado com o `openpyxl`.

Mas o `Pandas` será necessário nas versões posteriores porque além de gerar o arquivo de saída serão gerados diversos outros arquivos `.html` com análises comparativas.

**file output**

O arquivo de saída final com os dados coletados deve conter as seguintes colunas dispostas da coluna [A:J]:
```
['emp', 'mes', 'ano', 'origem', 'historico', 'centro_custo_bal', 'conta', 'des_conta', 'movimento', 'view]
```

* 'emp' = Código da Empresa que vai ser lido à partir de um dicionário e vai procurar pelo nome em Célula [B2]
* 'mes' = É o mês do ano de 1 a 12
* 'ano' = É o ano definido em Célula `[C3]`
* 'origem' = Valor fixo 'Orçamento'
* 'historico' = Vazio
* 'centro_custo_bal' = Lê o valor em Célula `[B1]` e localiza o correspondente no dicionário tratado em `Cost Centers`.
* 'conta' = pegar a conta como descrita em Input Data no item 'SUGESTÃO DE SOLUÇÃO PARA TRATAR AS LINHAS:'.
* 'des_conta' = Pegar a descrição do dicionário tratado em Input Data no item 'SUGESTÃO DE SOLUÇÃO PARA TRATAR AS LINHAS:'.
* 'movimento' = é o valor que foi lido no arquivo cada um para seu respectivo mês.
* 'view' = Valor fixo 'Atual'.
                 
## Other information about the project

Utiliza o conceito de `@dataclass` para dados das empresas e centros de custo.
Em outras versões estes dados podem estar em um banco de dados.
