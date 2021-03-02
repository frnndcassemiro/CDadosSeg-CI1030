Trabalhos realizados para a matéria de CI1030-CiênciaDeDados referentes ao ERE2-2021 (UFPR) <br>
Professor: André Grégio<br>
Alunos:<br> 
Fernanda Cassemiro Pereira GRR20163078<br>
Gabriel Segatti GRR20189990<br>
Victor Rocha de Abreu GRR20171623<br>
<br>
**Sobre o Dataset**
- Escolhemos o AWS Honeypot Attack Data, um dataset que registra tentativas de ataques interceptados por honeypots. Possui 451,581 linhas de dados coletados entre 21:53 do dia 3 de março até 05:55 de 8 de setembro.

- As colunas são:

  - Date
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


**Distribuição do Dataset**
- As 15 colunas do Dataset são distribuídas da maneira a seguir:
  - **Country Acronym**: os 6 termos mais frequentes estão abaixo, enquanto todos os demais 172 possíveis valores ocorrem 10.000 vezes ou menos, dentre as 451.000 linhas.
    - CN: 191394.
    - US: 90005.
    - JP: 17204.
    - IR: 13042.
    - TW: 12150.
   
  - **Country**: da mesma forma que _Country Acronym_.
  
  - **Type**:
  
    ![type](https://user-images.githubusercontent.com/71611489/109517995-9d695900-7a88-11eb-89cc-0f5addd8422e.png)
  
  - **Source Port**: as portas utilizadas variam de valores próximos a 0 até 65535 (eixo X), já que diferentes protocolos são utilizados. O eixo Y corresponde ao número de vezes que cada porta foi utilizada.
    ![spt](https://user-images.githubusercontent.com/71611489/109510515-ddc4d900-7a80-11eb-8884-a33892182a01.png)
  
  - **Dest Port**: Mesmo racíocínio de _Source Port_:
    ![dpt](https://user-images.githubusercontent.com/71611489/109511006-65aae300-7a81-11eb-98f7-d92f878d2a6c.png)
    
  - **Date**: segue a distribuição de dados por mês.
    ![date](https://user-images.githubusercontent.com/71611489/109512204-9d665a80-7a82-11eb-9283-6ea56344b468.png)
    
  - **Host**: a distribuição se dá pelo número de vezes que o Host de cada Honeypot foi acessado:
 
    ![host](https://user-images.githubusercontent.com/71611489/109512486-e7e7d700-7a82-11eb-90bf-2294b4a4308c.png)
  
  - **Latitude**: convertendo os valores para inteiros, temos:
    ![latitude](https://user-images.githubusercontent.com/71611489/109512857-4745e700-7a83-11eb-9576-943bbca7ce80.png)
    
  - **Longitude**: convertendo os valores para inteiros, temos:
    ![Longitude](https://user-images.githubusercontent.com/71611489/109513151-912ecd00-7a83-11eb-93d5-64d655318a8c.png)

  - **City**: existem 1181 valores distintos de cidades e estados, sendo suas ocorrências:
    - Null: 109469
    - California: 37266
    - Jiangsu Sheng: 34114
    - Beijing Shi: 33564
    - Liaoning: 21346
    Todos os demais 1175 locais ocorrem 13500 vezes ou menos.

  - **City Abbreviation**: existem 614 valores distintos para esse campo, sendo numéricos ou textuais:
    - Null: 119842
    - CA: 37278
    - 11: 36062
    - 32: 34121
    - 21: 21423
    Todos demais 609 valores ocorrem 13700 vezes ou menos.
    
  - **Postal Code**: convertendo os CEPs para inteiros, temos a seguinte distribuição:
    ![cep](https://user-images.githubusercontent.com/71611489/109517232-cb01d280-7a87-11eb-879c-37d0534a4608.png)
    
  - **Protocol**: são usados 3 protocolos dentre todos os registros, aqui estão as frequências com que se distribuem:
    ![protocol](https://user-images.githubusercontent.com/71611489/109515544-f84d8100-7a85-11eb-99e6-c923fc5c8322.png)
    
  - **Source IP**: existem 69586 valores diferentes de IP registrados. A foto abaixo representa os mais utilizados, todos os demais não incluídos occorem 700 vezes ou menos:
    ![ip](https://user-images.githubusercontent.com/71611489/109516433-f3d59800-7a86-11eb-95cc-37eb265eecb0.png)
     

**Dados a Retirar/Manter**
- Seria interessante retirar a coluna **Type**, visto que esta não é valorada para a maior parte dos registros do dataset. 
- As colunas que guardam o nome das cidades e países de maneira abreviada (**Locale Abbreviation, Country Acronym**) dificilmente serão utilizadas para alguma análise, já que temos os dados na íntegra. 
- **Postal Code** (cep), **Latitude** e **Longitude** também poderiam ser descartados, visto que não estamos interessados na localização em que ataques ocorreram de forma tão detalhada.
- **City Abbreviation** possui valores em texto ou em número, tal falta de consistencia provavelmente causará impecilhos que justificam sua retirada do dataset, visto que o mesmo dado já é explicitado no campo **City**.
- **Date** será quebrada em duas colunas, onde uma terá o formato dd/mm/aaaa e a outra a hora e minuto, ao invés de um único campo multivalorado contendo ambas informaçoes.

