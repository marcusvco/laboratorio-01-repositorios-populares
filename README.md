
## 📌 Introdução
Neste trabalho, exploramos os **1.000 repositórios mais populares do GitHub** para identificar **padrões e características que definem o sucesso** no cenário atual de desenvolvimento de software.

Respondemos as seguintes **Questões de Pesquisa (RQs)** acompanhadas de métricas e hipóteses:

---

## ❓ Questões de Pesquisa

| RQ | Pergunta | Métrica | Hipótese |
|----|----------|---------|----------|
| **RQ01** | Sistemas populares são maduros/antigos? | Idade do repositório (anos desde a criação) | Repositórios populares tendem a ser mais antigos, pois confiança e base de usuários levam tempo para se consolidar. |
| **RQ02** | Sistemas populares recebem muita contribuição externa? | Total de *pull requests* aceitas | A popularidade atrai uma comunidade engajada, resultando em alto volume de contribuições externas. |
| **RQ03** | Sistemas populares lançam *releases* com frequência? | Total de *releases* | Projetos populares lançam versões frequentes para demonstrar desenvolvimento ativo e entregar valor aos usuários. |
| **RQ04** | Sistemas populares são atualizados com frequência? | Tempo até a última atualização | Repositórios populares se mantêm relevantes e seguros com atualizações constantes. |
| **RQ05** | Sistemas populares são escritos nas linguagens mais populares? | Linguagem primária do repositório | Repositórios populares são majoritariamente desenvolvidos nas linguagens de maior uso no mercado. |
| **RQ06** | Sistemas populares possuem um alto percentual de *issues* fechadas? | Razão entre issues fechadas / total de issues | Projetos populares são bem gerenciados, refletindo em alta porcentagem de *issues* fechadas. |

---

## ⚙️ Metodologia

O arquivo **`repositorios_github.csv`** contém informações sobre os **1.000 repositórios com mais estrelas** no GitHub, incluindo:

- 📅 Data de criação  
- 🔀 Número de *pull requests*  
- 🚀 Total de *releases*  
- 💻 Linguagem primária  
- 🐞 Contagem de *issues* abertas e fechadas  

**Etapas de análise:**

1. **Cálculo da Idade (RQ01):**  
   - Idade = Data de referência (ago/2025) – Data de criação.  
   - Resultado convertido em anos.

2. **Contribuição Externa (RQ02):**  
   - Métrica: coluna **Total Pull Requests**.

3. **Frequência de Releases (RQ03):**  
   - Métrica: coluna **Total Releases**.

4. **Atualizações Recentes (RQ04):**  
   - Métrica: diferença entre a data de última atualização e a data de referência.

5. **Popularidade das Linguagens (RQ05):**  
   - Extração da coluna **Language**.  
   - Contagem das linguagens mais frequentes.  
   - Repositórios sem linguagem definida → **"Não especificado"**.

6. **Percentual de Issues Fechadas (RQ06):**  
   - Fórmula: razão entre número de issues fechadas pelo total de issues  
   - Casos com zero *issues* foram desconsiderados.  
   - Análise feita sobre a **mediana** dos valores.

---
