# Dataset: Desempenho Acadêmico de Estudantes

## 📊 Visão Geral

Este dataset contém informações sobre **2.510 estudantes universitários** e tem como objetivo prever o **desempenho acadêmico final** (nota de 0-100) com base em diversos fatores.

**Problema:** Regressão (prever valor contínuo)
**Variável Alvo:** `final_grade` (nota final do estudante)

---

## 📋 Descrição das Variáveis

### Identificação
- **`student_id`**: ID único do estudante (texto)
  - Exemplo: STD01416, STD01345
  - **Não usar como feature para o modelo**

### Variáveis Demográficas
- **`age`**: Idade do estudante (numérico)
  - Faixa: 18-25 anos

- **`gender`**: Gênero (categórico)
  - Valores: M (Masculino), F (Feminino)

- **`parental_education`**: Nível educacional dos pais (categórico ordinal)
  - Valores: high_school, bachelor, master, doctorate
  - Ordem: high_school < bachelor < master < doctorate

### Variáveis Acadêmicas
- **`study_hours_week`**: Horas de estudo por semana (numérico)
  - Faixa aproximada: 0-20 horas

- **`attendance_rate`**: Taxa de frequência às aulas (numérico)
  - Faixa: 0-100%
  - Valores altos indicam maior presença

- **`previous_scores`**: Notas médias de períodos anteriores (numérico)
  - Faixa: 0-100 pontos
  - Forte preditor do desempenho futuro

- **`tutoring`**: Recebe aulas de reforço/tutoria (categórico)
  - Valores: Yes, No

- **`extracurricular`**: Participa de atividades extracurriculares (categórico)
  - Valores: Yes, No
  - Exemplos: esportes, clubes, projetos

### Variáveis de Infraestrutura e Condições
- **`internet_quality`**: Qualidade da conexão de internet (categórico ordinal)
  - Valores: Poor, Good, Excellent
  - Ordem: Poor < Good < Excellent
  - Importante para ensino online/híbrido

- **`family_income`**: Faixa de renda familiar (categórico ordinal)
  - Valores: Low, Medium, High
  - Ordem: Low < Medium < High

### Variáveis de Saúde e Bem-estar
- **`sleep_hours`**: Horas médias de sono por dia (numérico)
  - Faixa aproximada: 4-10 horas
  - Impacto na performance cognitiva

- **`health_status`**: Estado geral de saúde (categórico ordinal)
  - Valores: Poor, Good, Excellent
  - Ordem: Poor < Good < Excellent

### Variável Alvo (Target)
- **`final_grade`**: Nota final do estudante (numérico - VARIÁVEL ALVO)
  - Faixa: 0-100 pontos
  - **Esta é a variável que você deve prever!**

---

## ⚠️ Problemas de Qualidade dos Dados

Este dataset foi criado com **problemas intencionais** para simular dados do mundo real. Você precisará identificar e tratar:

### 1. Valores Faltantes (Missing Values)
- **Aproximadamente 8% dos dados** possuem valores faltantes
- Distribuídos em várias colunas
- Representados como `NaN`, células vazias ou espaços em branco
- **Exemplo:**
  ```
  study_hours_week    NaN
  internet_quality
  family_income       NaN
  ```

### 2. Outliers
- **~40-50 registros** com valores extremos mas plausíveis
- Podem ser legítimos (ex: aluno excepcional) ou erros
- **Exemplo:**
  - Estudante com 20h de estudo/semana
  - Nota anterior de 100

### 3. Valores Impossíveis
- **~10-20 registros** com valores que violam limites lógicos
- **Exemplos:**
  - `attendance_rate > 100%`
  - `sleep_hours > 24` ou `< 0`
  - `final_grade > 100` ou `< 0`

### 4. Problemas de Formatação
- **~70 registros** com inconsistências de texto
- **Exemplos:**
  ```
  tutoring: "  No " (espaços extras)
  tutoring: "no" (lowercase em vez de "No")
  tutoring: "Yes " (espaço no final)
  ```

### 5. Inconsistências Lógicas
- **~10-15 registros** com padrões contraditórios
- **Exemplo:**
  - `study_hours_week = 0.5` + `attendance_rate = 10%` mas `final_grade = 98`

---

## 🎯 Contexto e Aplicação Prática

### Problema de Negócio
Uma universidade deseja:
1. **Identificar estudantes em risco** de baixo desempenho antes das provas finais
2. **Implementar intervenções preventivas** (tutoria, aconselhamento)
3. **Otimizar alocação de recursos** (focar em quem mais precisa)

### Perguntas que o Modelo Deve Responder
- Quais fatores mais influenciam o desempenho final?
- É possível prever a nota final com 2 meses de antecedência?
- Estudantes de baixa renda têm desempenho significativamente diferente?
- Tutoria realmente melhora as notas?

---

## 📈 Estatísticas Descritivas (Resumo)

| Variável | Tipo | Missing | Valores Únicos | Faixa/Categorias |
|----------|------|---------|----------------|------------------|
| student_id | Texto | 0% | 2,510 | Único para cada aluno |
| age | Numérico | ~2% | 8 | 18-25 |
| gender | Categórico | ~1% | 2 | M, F |
| parental_education | Categórico | ~3% | 4 | high_school, bachelor, master, doctorate |
| study_hours_week | Numérico | ~5% | - | 0-20 |
| attendance_rate | Numérico | ~4% | - | 0-100 |
| previous_scores | Numérico | ~3% | - | 0-100 |
| tutoring | Categórico | ~2% | 2 | Yes, No |
| extracurricular | Categórico | ~1% | 2 | Yes, No |
| internet_quality | Categórico | ~6% | 3 | Poor, Good, Excellent |
| family_income | Categórico | ~7% | 3 | Low, Medium, High |
| sleep_hours | Numérico | ~2% | - | 4-10 |
| health_status | Categórico | ~3% | 3 | Poor, Good, Excellent |
| **final_grade** | **Numérico** | **0%** | - | **0-100** |

---

## 🔍 Exemplos de Registros

### Registro Completo (sem problemas)
```csv
STD01416,22,M,bachelor,5.66,69.55,Yes,6.49,49.41,No,Good,Medium,Good,85.39
```

### Registro com Valores Faltantes
```csv
STD01345,19,M,bachelor,13.3,58.82,Yes,8.12,50.29,No,,Medium,Good,98.43
```
(Missing: `internet_quality`)

### Registro com Formatação Incorreta
```csv
STD00660,18,M,bachelor,,49.88,Yes,7.43,52.41,  No ,Good,,Good,87.97
```
(Missing: `study_hours_week`, `family_income`; Formatação: `"  No "` com espaços)

---

## 📚 Tarefas Sugeridas para EDA (Semana 1)

### 1. Carregamento e Inspeção Inicial
- Carregar o dataset com pandas
- Verificar shape (linhas, colunas)
- Ver primeiras/últimas linhas
- Checar tipos de dados

### 2. Análise de Valores Faltantes
- Quantificar missing values por coluna
- Visualizar padrão de missingness
- Identificar se são MCAR, MAR ou MNAR

### 3. Análise da Variável Alvo
- Distribuição de `final_grade`
- Estatísticas descritivas (média, mediana, std)
- Verificar normalidade
- Identificar outliers

### 4. Análise Univariada
- Distribuição de cada feature numérica
- Frequência de cada categoria nas features categóricas
- Identificar assimetria (skewness)

### 5. Análise Bivariada
- Correlação entre features numéricas e `final_grade`
- Boxplots: features categóricas vs `final_grade`
- Identificar multicolinearidade

### 6. Identificação de Problemas
- Listar todos os problemas de qualidade encontrados
- Documentar valores impossíveis
- Registrar inconsistências

---

## ⚙️ Como Carregar o Dataset

```python
import pandas as pd
import numpy as np

# Carregar dataset
df = pd.read_csv('data/raw/students_performance.csv')

# Exibir informações básicas
print(f"Shape: {df.shape}")
print(f"\nPrimeiras linhas:")
print(df.head())

print(f"\nInformações sobre colunas:")
df.info()

print(f"\nEstatísticas descritivas:")
print(df.describe())

print(f"\nValores faltantes:")
print(df.isnull().sum())
```

---

## 🚨 IMPORTANTE

1. **NÃO modifique este arquivo** (`students_performance.csv`)
2. **NÃO faça commit de versões alteradas** deste dataset em `data/raw/`
3. **Salve dados processados em** `data/processed/`
4. **Documente todas as transformações** que você fizer

---

**Última atualização:** Outubro 2027
