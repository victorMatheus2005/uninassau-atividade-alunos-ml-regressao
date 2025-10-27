# Projeto: Machine Learning - Modelos de Regressão

**Disciplina:** Introdução à Machine Learning - 2025.1
**Professor:** Professor Durval
**Organização:** uninassau-ml-classroom

Este repositório é o seu ponto de partida (template) para a atividade de Modelos de Regressão. Siga as orientações semanais e utilize o fluxo de trabalho Git detalhado abaixo.

---

## 🚀 Fluxo de Trabalho e Regras de Entrega

Para garantir a rastreabilidade e a avaliação correta do seu progresso, é **obrigatório** seguir o fluxo Git baseado em *branches* (ramos) e *commits* **a cada semana de entrega**.

### 1. Crie uma Branch Semanal

Para iniciar o trabalho de cada semana, crie uma nova *branch* a partir da `main` no seu repositório, usando o padrão: `semana/X-nome-da-tarefa`.

**Exemplo para a 1ª Semana:**
```bash
git checkout main
git pull origin main
git checkout -b semana/1-analise-exploratoria
```

### 2. Commits e Progresso

Faça *commits* pequenos e frequentes na sua *branch* de trabalho, documentando seu progresso.

**Boas práticas para mensagens de commit:**
```bash
# Adicionando uma nova funcionalidade
git commit -m "feat: Adiciona visualização de distribuição das features"

# Corrigindo um erro
git commit -m "fix: Corrige cálculo de valores faltantes"

# Atualizando documentação
git commit -m "docs: Atualiza análise de correlação no notebook"

# Refatorando código
git commit -m "refactor: Reorganiza funções de pré-processamento"
```

### 3. Entrega Semanal (Pull Request)

Ao final de cada semana (ou quando a etapa for concluída), você deve abrir um **Pull Request (PR)** da sua *branch* semanal para a `main`.

**Como criar um Pull Request:**
1. Faça push da sua branch:
   ```bash
   git push origin semana/1-analise-exploratoria
   ```

2. No GitHub, vá até o repositório e clique em **"Compare & pull request"**

3. Preencha o PR com:
   - **Título:** `ENTREGA SEMANA 1: Análise Exploratória de Dados`
   - **Descrição:**
     ```markdown
     ## O que foi feito
     - Análise de valores faltantes
     - Visualizações de distribuição
     - Análise de correlação

     ## Desafios encontrados
     - [Descreva dificuldades]

     ## Arquivos modificados/criados
     - notebooks/01_EDA.ipynb
     - data/processed/dataset_clean.csv
     ```

### 4. Integração (Merge)

O professor (ou o sistema de Autograding, se configurado) revisará seu PR. Somente após a aprovação, o PR será aceito (Merge).

**⚠️ IMPORTANTE:** Você só deve começar a próxima semana após o `merge` da anterior.

---

## 📋 Etapas do Projeto (Cronograma e Requisitos)

| Etapa | Semana | Prazo de Entrega (PR) | Diretrizes e Entregáveis | Pastas Envolvidas |
|:---:|:---:|:---:|:---|:---|
| **01** | **Semana 1** | [DD/MM/AAAA] | **Análise Exploratória (EDA):** Carregue o dataset (em `data/raw`), trate valores nulos, faça visualizações e descreva as principais características. **Entregável:** `notebooks/01_EDA.ipynb` | `data/raw/`, `notebooks/` |
| **02** | **Semana 2** | [DD/MM/AAAA] | **Pré-processamento e Baseline:** Crie e salve o dataset limpo (`data/processed/`), faça *feature engineering* e treine o modelo de Regressão Linear Simples (Baseline). **Entregável:** `notebooks/02_Preprocessamento_Baseline.ipynb` | `data/processed/`, `notebooks/`, `src/` |
| **03** | **Semana 3** | [DD/MM/AAAA] | **Modelos Avançados:** Implemente e compare outros modelos de Regressão (Ridge, Lasso, Random Forest, XGBoost). Documente a performance (RMSE, R², MAE). **Entregável:** `notebooks/03_Modelos_Avancados.ipynb` | `notebooks/` |
| **04** | **Semana 4** | [DD/MM/AAAA] | **Otimização e Conclusão:** Ajuste de hiperparâmetros (GridSearch/RandomSearch), escolha o melhor modelo e gere um relatório final. **Entregável:** `notebooks/04_Otimizacao_Final.ipynb` + `docs/RELATORIO_FINAL.md` | `notebooks/`, `docs/` |

---

## 📁 Estrutura do Projeto

```
.
├── data/
│   ├── raw/              # Dados brutos fornecidos (NÃO MODIFICAR)
│   │   └── [dataset].csv
│   └── processed/        # Dados limpos e processados (você cria)
│       └── dataset_clean.csv
├── notebooks/            # Notebooks Jupyter das análises semanais
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessamento_Baseline.ipynb
│   ├── 03_Modelos_Avancados.ipynb
│   └── 04_Otimizacao_Final.ipynb
├── src/                  # Scripts Python (opcional, para código reutilizável)
│   ├── preprocessing.py
│   ├── models.py
│   └── utils.py
├── docs/                 # Documentação adicional
│   └── RELATORIO_FINAL.md
├── .gitignore
├── requirements.txt      # Dependências Python
└── README.md            # Este arquivo
```

### Descrição das Pastas

- **`data/raw/`**: Contém o dataset fornecido pelo professor. **NÃO modifique estes arquivos!**
- **`data/processed/`**: Armazene aqui os dados limpos e pré-processados que você criar.
- **`notebooks/`**: Crie seus notebooks Jupyter aqui, seguindo a numeração das semanas.
- **`src/`**: (Opcional) Para organizar funções reutilizáveis em módulos Python.
- **`docs/`**: Documentação adicional, incluindo o relatório final.

---

## 💻 Como Iniciar (Setup do Ambiente)

### 1. Clone o Repositório

Após aceitar a tarefa no GitHub Classroom, clone seu repositório:

```bash
git clone https://github.com/uninassau-ml-classroom/[seu-repositorio].git
cd [nome-do-repositorio]
```

### 2. Configure o Ambiente Virtual

**Opção 1: usando venv (recomendado)**
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

**Opção 2: usando conda**
```bash
# Criar ambiente
conda create -n ml-projeto python=3.10

# Ativar ambiente
conda activate ml-projeto
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Verifique a Instalação

```bash
# Testar se as bibliotecas foram instaladas
python -c "import pandas, numpy, sklearn, seaborn, matplotlib; print('✅ Todas as bibliotecas instaladas!')"
```

### 5. Inicie a Primeira Semana

```bash
# Criar branch da Semana 1
git checkout -b semana/1-analise-exploratoria

# Iniciar Jupyter
jupyter notebook
```

Crie seu primeiro notebook (`notebooks/01_EDA.ipynb`) e comece a análise exploratória!

---

## 📊 Dataset Disponível

O dataset está localizado em `data/raw/` e contém dados para um problema de regressão.

**IMPORTANTE:** Consulte o arquivo `data/raw/README.md` (se disponível) para:
- Descrição das variáveis (features)
- Contexto do problema
- Dicionário de dados

---

## ✅ Checklist de Cada Semana

Antes de abrir seu Pull Request, verifique:

- [ ] Todos os notebooks executam do início ao fim (`Restart & Run All`)
- [ ] Código está comentado e organizado
- [ ] Commits foram feitos regularmente (não apenas 1 commit gigante)
- [ ] Mensagens de commit são descritivas
- [ ] Arquivos gerados estão nas pastas corretas
- [ ] `.gitignore` está impedindo arquivos desnecessários de serem commitados
- [ ] Pull Request tem título e descrição claros
- [ ] Você testou seu código antes de fazer push

---

## 🚫 O Que NÃO Fazer

❌ **NÃO faça commits diretamente na `main`** - Sempre use branches
❌ **NÃO modifique arquivos em `data/raw/`** - São os dados originais
❌ **NÃO faça commit de arquivos grandes** (modelos .pkl, venv/, etc.) - Use .gitignore
❌ **NÃO copie código de outros alunos** - Plágio será penalizado
❌ **NÃO deixe para última hora** - Commits regulares são parte da avaliação

---

## 📚 Recursos Úteis

### Documentação Oficial
- [Pandas](https://pandas.pydata.org/docs/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/stable/contents.html)
- [Seaborn](https://seaborn.pydata.org/)

### Tutoriais Recomendados
- [Git Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
- [Jupyter Notebook Tips](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

### Fluxo Git Resumido
```bash
# 1. Criar nova branch
git checkout -b semana/X-nome-tarefa

# 2. Trabalhar e fazer commits
git add .
git commit -m "feat: descrição do que foi feito"

# 3. Enviar para GitHub
git push origin semana/X-nome-tarefa

# 4. Abrir Pull Request no GitHub

# 5. Após merge aprovado, voltar para main
git checkout main
git pull origin main
```

---

## ❓ Suporte

Em caso de dúvidas:

1. **Sobre Git/GitHub:** Consulte a [documentação oficial do Git](https://git-scm.com/doc)
2. **Sobre o projeto:** Abra uma Issue neste repositório ou procure o professor
3. **Problemas técnicos:** Verifique se todas as dependências foram instaladas corretamente

**⚠️ ATENÇÃO:** Não faça commits diretamente na `main` sem abrir um Pull Request. Isso pode resultar em penalização na nota.

---

## 🏆 Critérios de Avaliação

Cada entrega semanal será avaliada considerando:

| Critério | Peso | Descrição |
|----------|:----:|-----------|
| **Código Funcional** | 30% | Código executa sem erros, está organizado e bem estruturado |
| **Análise Técnica** | 30% | Qualidade da análise, uso correto de técnicas de ML |
| **Documentação** | 20% | Código comentado, notebooks claros, README atualizado |
| **Fluxo Git** | 10% | Uso correto de branches, commits descritivos e regulares |
| **Visualizações** | 10% | Gráficos informativos e bem formatados |

### Pontuação Extra
- Implementações criativas (+0.5)
- Análises além do solicitado (+0.5)
- Código muito bem organizado (+0.3)

---

**Boa sorte no projeto! 🚀**

*Última atualização: Outubro 2027*
