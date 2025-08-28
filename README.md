# laboratorio-01-repositorios-populares
Alunos: Luiz Felipe Campos de Morais e Marcus Vinícius Carvalho de Oliveira

## Introdução e hipóteses informais sobre as RQs
Neste trabalho, buscamos no universo dos repositórios de código aberto mais populares do GitHub para desvendar os padrões e as características que definem o sucesso no cenário atual de desenvolvimento de software.


- **RQ01:** Sistemas populares são maduros/antigos?  
  **Métrica:** idade do repositório (calculado a partir da data de sua criação)  
  **Hipótese:** Repositórios populares tendem a ser mais antigos, pois a confiança e a base de usuários levam tempo para se consolidar.  

- **RQ02:** Sistemas populares recebem muita contribuição externa?  
  ***Métrica:** total de pull requests aceitas  
  **Hipótese:** A popularidade atrai uma comunidade engajada, resultando em um alto volume de contribuições externas (pull requests).  

- **RQ03:** Sistemas populares lançam releases com frequência?  
  **Métrica:** total de releases  
  **Hipótese:** Projetos populares lançam novas versões com frequência para demonstrar desenvolvimento ativo e entregar valor aos usuários.  

- **RQ04:** Sistemas populares são atualizados com frequência?  
  **Métrica:** tempo até a última atualização (calculado a partir da data de última
  atualização)  
  **Hipótese:** Para se manterem relevantes e seguros, os repositórios populares devem ser atualizados constantemente.  
  
- **RQ05:** Sistemas populares são escritos nas linguagens mais populares?  
  **Métrica:** linguagem primária de cada um desses repositórios  
  **Hipótese:** Os repositórios mais populares são majoritariamente desenvolvidos nas linguagens de programação mais usadas no mercado.  

- **RQ06:** Sistemas populares possuem um alto percentual de issues fechadas?  
  **Métrica:** razão entre número de issues fechadas pelo total de issues  
  **Hipótese:** Projetos populares são bem gerenciados, o que se reflete em uma alta porcentagem de issues fechadas.  


## Metodologia
 O arquivo repositorios_github.csv contém informações sobre os 1.000 repositórios com mais estrelas, incluindo data de criação, número de pull requests, total de releases, linguagem primária e contagem de issues abertas e fechadas.

Cálculo da Idade (RQ01): A idade de cada repositório foi calculada subtraindo a data de criação (Created At)  da data de referência deste relatório (agosto de 2025). O resultado foi convertido para anos.  
Contribuição Externa (RQ02): A métrica de contribuição foi analisada diretamente a partir da coluna Total Pull Requests.  
Frequência de Releases (RQ03): A frequência de lançamentos foi avaliada usando os dados da coluna Total Releases.  
Popularidade das Linguagens (RQ05): A linguagem primária de cada repositório foi extraída da coluna Language. Foi realizada uma contagem para identificar as linguagens mais frequentes na amostra. Repositórios sem uma linguagem principal definida foram categorizados como "Não especificado".  
Percentual de Issues Fechadas (RQ06): Para cada repositório, o total de issues foi calculado somando as Open Issues e Closed Issues. A razão de 
issues fechadas foi então calculada pela fórmula da razão entre número de issues fechadas pelo total de issues
Casos sem nenhuma issue (denominador zero) foram desconsiderados do cálculo da mediana.
