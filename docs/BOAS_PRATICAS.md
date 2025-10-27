# 📚 Boas Práticas para o Projeto de Machine Learning

Este documento contém orientações e melhores práticas para garantir que seu projeto seja bem-sucedido, organizado e profissional.

---

## 🎯 Organização Geral

### 1. Mantenha o Código Limpo e Organizado

✅ **BOM:**
```python
# Carregar dados e realizar análise exploratória inicial
df = pd.read_csv('data/raw/students_performance.csv')
print(f"Dataset shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}")
```

❌ **RUIM:**
```python
df=pd.read_csv('data/raw/students_performance.csv')
print(df.shape)
print(df.isnull().sum())
# código desorganizado, sem comentários
```

### 2. Use Comentários Descritivos

✅ **BOM:**
```python
# Identificar outliers usando método IQR (Interquartile Range)
# Valores abaixo de Q1 - 1.5*IQR ou acima de Q3 + 1.5*IQR são considerados outliers
Q1 = df['study_hours_week'].quantile(0.25)
Q3 = df['study_hours_week'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['study_hours_week'] < Q1 - 1.5*IQR) |
              (df['study_hours_week'] > Q3 + 1.5*IQR)]
```

❌ **RUIM:**
```python
# outliers
Q1 = df['study_hours_week'].quantile(0.25)
Q3 = df['study_hours_week'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['study_hours_week'] < Q1 - 1.5*IQR) | (df['study_hours_week'] > Q3 + 1.5*IQR)]
```

### 3. Divida o Código em Seções Lógicas

Use markdown headers nos notebooks Jupyter:

```markdown
# 1. Importação de Bibliotecas

# 2. Carregamento de Dados

# 3. Análise Exploratória
## 3.1 Valores Faltantes
## 3.2 Distribuição da Variável Alvo
## 3.3 Correlações

# 4. Conclusões
```

---

## 📊 Análise Exploratória de Dados (EDA)

### 1. Sempre Verifique os Dados Primeiro

```python
# Inspeção inicial obrigatória
df.head()
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
```

### 2. Visualizações Devem Ser Informativas

✅ **BOM:**
```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['final_grade'], kde=True, bins=30)
plt.title('Distribuição das Notas Finais', fontsize=14, fontweight='bold')
plt.xlabel('Nota Final', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.axvline(df['final_grade'].mean(), color='red', linestyle='--', label=f'Média: {df["final_grade"].mean():.2f}')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

❌ **RUIM:**
```python
df['final_grade'].hist()
plt.show()
```

### 3. Documente Suas Descobertas

Após cada visualização ou análise, adicione células markdown explicando:
- O que você está analisando
- O que você encontrou
- Por que isso é importante

**Exemplo:**
```markdown
### Análise de Correlação

A matriz de correlação mostra que:
- `previous_scores` tem a maior correlação com `final_grade` (r=0.75)
- `study_hours_week` tem correlação moderada (r=0.45)
- `sleep_hours` tem correlação fraca (r=0.12)

**Conclusão:** Notas anteriores são o melhor preditor, seguidas por horas de estudo.
```

---

## 🔧 Pré-processamento de Dados

### 1. Tratamento de Valores Faltantes

✅ **BOM:** Documente a estratégia escolhida
```python
# Estratégia de imputação:
# - Numéricas: mediana (mais robusta a outliers)
# - Categóricas: moda (valor mais frequente)

from sklearn.impute import SimpleImputer

# Imputar variáveis numéricas
num_imputer = SimpleImputer(strategy='median')
df[num_cols] = num_imputer.fit_transform(df[num_cols])

# Imputar variáveis categóricas
cat_imputer = SimpleImputer(strategy='most_frequent')
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

print(f"✅ Valores faltantes após imputação: {df.isnull().sum().sum()}")
```

❌ **RUIM:** Deletar linhas sem justificativa
```python
df = df.dropna()  # Perde muitos dados!
```

### 2. Encoding de Variáveis Categóricas

```python
# One-Hot Encoding para variáveis nominais (sem ordem)
df = pd.get_dummies(df, columns=['gender', 'tutoring', 'extracurricular'], drop_first=True)

# Label Encoding para variáveis ordinais (com ordem)
from sklearn.preprocessing import LabelEncoder

# Criar mapeamento manual para preservar ordem
education_map = {
    'high_school': 0,
    'bachelor': 1,
    'master': 2,
    'doctorate': 3
}
df['parental_education'] = df['parental_education'].map(education_map)
```

### 3. Feature Engineering

Crie features novas que possam melhorar o modelo:

```python
# Criar feature de "esforço total" (horas de estudo * frequência)
df['effort_score'] = df['study_hours_week'] * (df['attendance_rate'] / 100)

# Criar categoria de "alto desempenho anterior"
df['high_previous_performer'] = (df['previous_scores'] >= 80).astype(int)

# Criar interação entre variáveis
df['study_x_tutoring'] = df['study_hours_week'] * df['tutoring_Yes']
```

---

## 🤖 Modelagem

### 1. Sempre Divida os Dados Corretamente

```python
from sklearn.model_selection import train_test_split

# Separar features (X) e target (y)
X = df.drop('final_grade', axis=1)
y = df['final_grade']

# Divisão 60% treino, 20% validação, 20% teste
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

print(f"Treino: {X_train.shape[0]} amostras")
print(f"Validação: {X_val.shape[0]} amostras")
print(f"Teste: {X_test.shape[0]} amostras")
```

### 2. Normalize/Padronize Apenas Após o Split

❌ **RUIM:** Normalizar antes do split (data leakage!)
```python
X = scaler.fit_transform(X)  # ERRADO!
X_train, X_test = train_test_split(X, y)
```

✅ **BOM:** Fit no treino, transform em validação/teste
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)  # Apenas transform!
X_test_scaled = scaler.transform(X_test)  # Apenas transform!
```

### 3. Avalie Múltiplas Métricas

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def evaluate_model(y_true, y_pred, model_name="Model"):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    print(f"\n{'='*50}")
    print(f"{model_name} - Performance Metrics")
    print(f"{'='*50}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE:  {mae:.4f}")
    print(f"R²:   {r2:.4f}")
    print(f"{'='*50}")

    return {'rmse': rmse, 'mae': mae, 'r2': r2}

# Usar
results = evaluate_model(y_val, y_pred, "Linear Regression")
```

### 4. Compare Modelos de Forma Organizada

```python
import pandas as pd

# Dicionário para armazenar resultados
results_dict = {}

# Treinar e avaliar múltiplos modelos
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

models = {
    'Linear Regression': LinearRegression(),
    'Ridge': Ridge(),
    'Lasso': Lasso(),
    'Random Forest': RandomForestRegressor(random_state=42),
    'XGBoost': XGBRegressor(random_state=42)
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_val_scaled)
    results_dict[name] = evaluate_model(y_val, y_pred, name)

# Criar DataFrame de comparação
results_df = pd.DataFrame(results_dict).T
results_df = results_df.sort_values('rmse')
print("\n📊 Comparação de Modelos:")
print(results_df)
```

---

## 🔍 Validação e Interpretação

### 1. Análise de Resíduos

```python
import matplotlib.pyplot as plt

# Calcular resíduos
residuals = y_val - y_pred

# Plot de resíduos
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Resíduos vs Predições
axes[0].scatter(y_pred, residuals, alpha=0.5)
axes[0].axhline(0, color='red', linestyle='--')
axes[0].set_xlabel('Valores Preditos')
axes[0].set_ylabel('Resíduos')
axes[0].set_title('Resíduos vs Predições')
axes[0].grid(alpha=0.3)

# Distribuição dos resíduos
axes[1].hist(residuals, bins=30, edgecolor='black')
axes[1].set_xlabel('Resíduos')
axes[1].set_ylabel('Frequência')
axes[1].set_title('Distribuição dos Resíduos')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

### 2. Feature Importance

```python
# Para modelos baseados em árvores
feature_importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(feature_importance['feature'][:10], feature_importance['importance'][:10])
plt.xlabel('Importância')
plt.title('Top 10 Features Mais Importantes')
plt.gca().invert_yaxis()
plt.show()
```

---

## 📝 Git e Controle de Versão

### 1. Commits Frequentes e Descritivos

✅ **BOM:**
```bash
git commit -m "feat: Adiciona análise de correlação entre features numéricas"
git commit -m "fix: Corrige tratamento de valores faltantes em internet_quality"
git commit -m "docs: Atualiza documentação da função de pré-processamento"
```

❌ **RUIM:**
```bash
git commit -m "update"
git commit -m "fixes"
git commit -m "stuff"
```

### 2. Padrões de Mensagem de Commit

Use prefixos claros:
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `refactor:` - Refatoração de código
- `test:` - Adição/modificação de testes
- `style:` - Formatação, espaços, etc.

### 3. Estrutura de Branches

```bash
# Branch de trabalho semanal
semana/1-analise-exploratoria
semana/2-preprocessamento-baseline
semana/3-modelos-avancados
semana/4-otimizacao-final

# Nunca commitar diretamente na main!
```

---

## ⚠️ Erros Comuns a Evitar

### 1. Data Leakage
❌ Usar dados de teste durante o treinamento
❌ Normalizar antes de fazer train-test split
❌ Feature engineering usando informações do futuro

### 2. Overfitting
❌ Modelo muito complexo para poucos dados
❌ Não usar validação cruzada
❌ Otimizar hiperparâmetros no conjunto de teste

### 3. Underfitting
❌ Modelo muito simples para o problema
❌ Features irrelevantes ou mal processadas
❌ Não fazer feature engineering

### 4. Organização
❌ Notebooks gigantes sem estrutura
❌ Código sem comentários
❌ Arquivos com nomes genéricos (`teste.ipynb`, `final_final_v2.ipynb`)

---

## ✅ Checklist Final

Antes de abrir seu Pull Request, verifique:

- [ ] Notebook executa do início ao fim sem erros (`Restart & Run All`)
- [ ] Código está comentado adequadamente
- [ ] Visualizações têm títulos, labels e legendas
- [ ] Resultados estão interpretados (não apenas números)
- [ ] Commits foram feitos regularmente (não apenas 1 commit)
- [ ] Mensagens de commit são descritivas
- [ ] `.gitignore` está funcionando (nenhum arquivo grande commitado)
- [ ] README está atualizado (se necessário)
- [ ] Dados processados salvos em `data/processed/`
- [ ] Nenhum hardcoded path absoluto (use caminhos relativos)

---

**Última atualização:** Outubro 2027
