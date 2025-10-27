"""
Notebook Starter - Semana 1: Análise Exploratória de Dados (EDA)

INSTRUÇÕES:
1. Copie este código para um novo Jupyter Notebook (01_EDA.ipynb)
2. Execute célula por célula, entendendo cada passo
3. Expanda as análises com suas próprias visualizações e insights
4. Documente suas descobertas em células markdown

ATENÇÃO: Este é apenas um PONTO DE PARTIDA. Você deve ir além!
"""

# ==============================================================================
# 1. IMPORTAÇÃO DE BIBLIOTECAS
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configurações de visualização
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Ignorar warnings
import warnings
warnings.filterwarnings('ignore')

print("✅ Bibliotecas importadas com sucesso!")

# ==============================================================================
# 2. CARREGAMENTO DOS DADOS
# ==============================================================================

# Carregar dataset
df = pd.read_csv('../data/raw/students_performance.csv')

print("\n" + "="*50)
print("DATASET CARREGADO")
print("="*50)
print(f"Shape: {df.shape}")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

# ==============================================================================
# 3. INSPEÇÃO INICIAL
# ==============================================================================

print("\n" + "="*50)
print("PRIMEIRAS LINHAS DO DATASET")
print("="*50)
print(df.head())

print("\n" + "="*50)
print("INFORMAÇÕES SOBRE AS COLUNAS")
print("="*50)
df.info()

print("\n" + "="*50)
print("ESTATÍSTICAS DESCRITIVAS")
print("="*50)
print(df.describe())

# ==============================================================================
# 4. ANÁLISE DE VALORES FALTANTES
# ==============================================================================

print("\n" + "="*50)
print("VALORES FALTANTES")
print("="*50)

missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing': missing,
    'Percentage': missing_pct
}).sort_values('Percentage', ascending=False)

print(missing_df[missing_df['Missing'] > 0])

# Visualização de valores faltantes
plt.figure(figsize=(12, 6))
missing_pct_sorted = missing_pct[missing_pct > 0].sort_values(ascending=False)
plt.barh(missing_pct_sorted.index, missing_pct_sorted.values)
plt.xlabel('Porcentagem de Valores Faltantes (%)', fontsize=12)
plt.title('Valores Faltantes por Feature', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ==============================================================================
# 5. ANÁLISE DA VARIÁVEL ALVO (final_grade)
# ==============================================================================

print("\n" + "="*50)
print("ANÁLISE DA VARIÁVEL ALVO: final_grade")
print("="*50)

print(f"Média: {df['final_grade'].mean():.2f}")
print(f"Mediana: {df['final_grade'].median():.2f}")
print(f"Desvio Padrão: {df['final_grade'].std():.2f}")
print(f"Mínimo: {df['final_grade'].min():.2f}")
print(f"Máximo: {df['final_grade'].max():.2f}")

# Distribuição de final_grade
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histograma
axes[0].hist(df['final_grade'], bins=30, edgecolor='black', alpha=0.7)
axes[0].axvline(df['final_grade'].mean(), color='red', linestyle='--',
                label=f'Média: {df["final_grade"].mean():.2f}')
axes[0].axvline(df['final_grade'].median(), color='green', linestyle='--',
                label=f'Mediana: {df["final_grade"].median():.2f}')
axes[0].set_xlabel('Nota Final', fontsize=12)
axes[0].set_ylabel('Frequência', fontsize=12)
axes[0].set_title('Distribuição das Notas Finais', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Boxplot
axes[1].boxplot(df['final_grade'], vert=True)
axes[1].set_ylabel('Nota Final', fontsize=12)
axes[1].set_title('Boxplot de Notas Finais', fontsize=14, fontweight='bold')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# ==============================================================================
# 6. ANÁLISE DE CORRELAÇÕES
# ==============================================================================

print("\n" + "="*50)
print("ANÁLISE DE CORRELAÇÕES")
print("="*50)

# Selecionar apenas colunas numéricas
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Calcular correlação com final_grade
correlations = df[numeric_cols].corr()['final_grade'].sort_values(ascending=False)
print("\nCorrelação com final_grade:")
print(correlations)

# Matriz de correlação
plt.figure(figsize=(12, 10))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=1)
plt.title('Matriz de Correlação - Features Numéricas', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ==============================================================================
# 7. ANÁLISE UNIVARIADA - VARIÁVEIS NUMÉRICAS
# ==============================================================================

print("\n" + "="*50)
print("ANÁLISE UNIVARIADA - VARIÁVEIS NUMÉRICAS")
print("="*50)

# Remover student_id e final_grade
numeric_features = [col for col in numeric_cols if col not in ['student_id', 'final_grade']]

# Criar subplots para distribuições
n_cols = 3
n_rows = (len(numeric_features) + n_cols - 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))
axes = axes.flatten()

for idx, col in enumerate(numeric_features):
    if df[col].notna().sum() > 0:  # Se houver dados não-nulos
        axes[idx].hist(df[col].dropna(), bins=30, edgecolor='black', alpha=0.7)
        axes[idx].set_xlabel(col, fontsize=10)
        axes[idx].set_ylabel('Frequência', fontsize=10)
        axes[idx].set_title(f'Distribuição: {col}', fontsize=11, fontweight='bold')
        axes[idx].grid(alpha=0.3)

# Remover subplots extras
for idx in range(len(numeric_features), len(axes)):
    fig.delaxes(axes[idx])

plt.tight_layout()
plt.show()

# ==============================================================================
# 8. ANÁLISE UNIVARIADA - VARIÁVEIS CATEGÓRICAS
# ==============================================================================

print("\n" + "="*50)
print("ANÁLISE UNIVARIADA - VARIÁVEIS CATEGÓRICAS")
print("="*50)

# Identificar colunas categóricas
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
if 'student_id' in categorical_cols:
    categorical_cols.remove('student_id')

# Contagem de valores para cada categórica
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())
    print(f"Valores únicos: {df[col].nunique()}")

# Visualizações
n_cols_cat = 2
n_rows_cat = (len(categorical_cols) + n_cols_cat - 1) // n_cols_cat

fig, axes = plt.subplots(n_rows_cat, n_cols_cat, figsize=(14, n_rows_cat * 4))
axes = axes.flatten() if len(categorical_cols) > 1 else [axes]

for idx, col in enumerate(categorical_cols):
    value_counts = df[col].value_counts()
    axes[idx].barh(value_counts.index, value_counts.values)
    axes[idx].set_xlabel('Frequência', fontsize=10)
    axes[idx].set_title(f'Distribuição: {col}', fontsize=11, fontweight='bold')
    axes[idx].grid(alpha=0.3)

# Remover subplots extras
for idx in range(len(categorical_cols), len(axes)):
    fig.delaxes(axes[idx])

plt.tight_layout()
plt.show()

# ==============================================================================
# 9. ANÁLISE BIVARIADA - CATEGÓRICAS vs FINAL_GRADE
# ==============================================================================

print("\n" + "="*50)
print("ANÁLISE BIVARIADA - CATEGÓRICAS vs FINAL_GRADE")
print("="*50)

# Boxplots de categóricas vs final_grade
n_cols_bi = 2
n_rows_bi = (len(categorical_cols) + n_cols_bi - 1) // n_cols_bi

fig, axes = plt.subplots(n_rows_bi, n_cols_bi, figsize=(14, n_rows_bi * 5))
axes = axes.flatten() if len(categorical_cols) > 1 else [axes]

for idx, col in enumerate(categorical_cols):
    df.boxplot(column='final_grade', by=col, ax=axes[idx])
    axes[idx].set_xlabel(col, fontsize=10)
    axes[idx].set_ylabel('Nota Final', fontsize=10)
    axes[idx].set_title(f'Nota Final por {col}', fontsize=11, fontweight='bold')
    axes[idx].get_figure().suptitle('')  # Remover título automático

# Remover subplots extras
for idx in range(len(categorical_cols), len(axes)):
    fig.delaxes(axes[idx])

plt.tight_layout()
plt.show()

# ==============================================================================
# 10. IDENTIFICAÇÃO DE OUTLIERS
# ==============================================================================

print("\n" + "="*50)
print("IDENTIFICAÇÃO DE OUTLIERS (Método IQR)")
print("="*50)

def detect_outliers_iqr(data, column):
    """Detecta outliers usando o método IQR"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

# Detectar outliers em cada variável numérica
for col in numeric_features:
    if df[col].notna().sum() > 0:
        outliers, lower, upper = detect_outliers_iqr(df, col)
        print(f"\n{col}:")
        print(f"  Lower Bound: {lower:.2f}")
        print(f"  Upper Bound: {upper:.2f}")
        print(f"  Número de Outliers: {len(outliers)}")
        if len(outliers) > 0:
            print(f"  Valores: {sorted(outliers[col].unique())}")

# ==============================================================================
# 11. CONCLUSÕES PRELIMINARES
# ==============================================================================

print("\n" + "="*50)
print("RESUMO DA ANÁLISE EXPLORATÓRIA")
print("="*50)

print(f"""
DATASET:
- Total de registros: {df.shape[0]}
- Total de features: {df.shape[1]}
- Features numéricas: {len(numeric_cols)}
- Features categóricas: {len(categorical_cols)}

VARIÁVEL ALVO (final_grade):
- Média: {df['final_grade'].mean():.2f}
- Desvio Padrão: {df['final_grade'].std():.2f}
- Faixa: {df['final_grade'].min():.2f} - {df['final_grade'].max():.2f}

VALORES FALTANTES:
- Total de valores faltantes: {df.isnull().sum().sum()}
- Porcentagem: {(df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100:.2f}%

PRÓXIMOS PASSOS (Semana 2 - Pré-processamento):
1. Tratar valores faltantes
2. Tratar outliers
3. Encoding de variáveis categóricas
4. Feature Engineering
5. Normalização/Padronização
""")

print("\n✅ Análise Exploratória Concluída!")
print("📝 Lembre-se de documentar suas descobertas em células markdown!")
