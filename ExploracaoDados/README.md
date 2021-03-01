**Sobre o Dataset**
- Escolhemos o AWS Honeypot Attack Data, um dataset que registra tentativas de ataques interceptados por honeypots. Possui 451,581 linhas de dados coletados entre 21:53 do dia 3 de março até 05:55 de 8 de setembro.

- As colunas são:

  - Data
  - Host
  - Source
  - Protocol
  - Type
  - Source Port
  - Dest Port
  - Source IP
  - Country Acronym
  - Country Name
  - City
  - City Abbreviation
  - Postal Code
  - Longitude
  - Latitude


**Tipos de Dados**
- O Dataset escolhido tem números de colunas iguais de atributos numéricos e textuais sendo 7 para cada. Por fim, possui uma única coluna no formato de datas.

**Objetivo**
- Analizar dados sobre ataques realizados e apresentar, de maneira gráfica, suas tendências, como locais mais atacados, horas em que mais ataques são realizados, países mais atigindos e outras especifidades. Por fim, pode-se pensar sobre usar o dataset para criar um algoritmo prediditivo de ameaças cibernéticas (com base nos atributos disponíveis).

**Rotulação do Dataset**
- Os rótulos são baseados no host do honeypot que recebe o ataque. Portanto, cada entrada corresponde a um ataque nos seguintes hosts:
  - groucho-oregon
  - groucho-us-east
  - groucho-singapore
  - groucho-tokyo
  - groucho-sa
  - zeppo-norcal
  - groucho-eu
  - groucho-norcal
  - groucho-sidney

**Dados a Retirar**
- Seria interessante retirar a coluna **Type**, visto que esta não é valorada para a maior parte dos registros do dataset. 
- As colunas que guardam o nome das cidades e países de maneira abreviada (**Locale Abbreviation, Country Acronym**) dificilmente serão utilizadas para alguma análise, já que temos os dados na íntegra. 
- **Postal Code** (cep), **Latitude** e **Longitude** também poderiam ser descartados, visto que não estamos interessados na localização em que ataques ocorreram de forma tão detalhada.

