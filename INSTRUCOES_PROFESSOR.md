# 📚 Instruções para o Professor - Template GitHub Classroom

## ✅ Template Criado com Sucesso!

Este documento explica como usar o template criado para configurar o GitHub Classroom.

---

## 📂 Estrutura Completa do Template

```
template-repo/
│
├── README.md                           # ⭐ Guia principal do projeto (alunos)
├── requirements.txt                    # Dependências Python
├── .gitignore                         # Arquivos a ignorar no Git
│
├── data/
│   ├── raw/                           # Dados originais (NÃO modificar)
│   │   ├── students_performance.csv   # Dataset fornecido
│   │   └── README.md                  # Descrição detalhada do dataset
│   └── processed/                     # Dados limpos (alunos criam)
│       └── .gitkeep
│
├── notebooks/                          # Notebooks Jupyter das análises
│   ├── README.md                      # Guia dos notebooks
│   ├── 00_EXEMPLO_STARTER.py          # Código exemplo (starter)
│   └── .gitkeep
│
├── src/                               # Scripts Python (opcional)
│   └── .gitkeep
│
└── docs/                              # Documentação adicional
    ├── BOAS_PRATICAS.md              # Guia de boas práticas
    ├── TEMPLATE_RELATORIO_FINAL.md   # Template para relatório
    └── .gitkeep
```

---

## 🚀 Próximos Passos (Ações Manuais)

### 1️⃣ Inicializar Repositório Git Local

```bash
cd /home/durval/Documentos/PROJETOS/ml-projeto-final/template-repo

# Inicializar Git
git init

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "chore: Inicializa template do projeto ML"
```

### 2️⃣ Criar Repositório no GitHub

**Opção A: Via Interface Web**
1. Acesse: https://github.com/new
2. Nome do repositório: `uninassau-atividade-alunos-ml-regressao`
3. Descrição: `Template para projeto de Machine Learning - Modelos de Regressão`
4. Visibilidade: **Public**
5. **NÃO marque:** Initialize with README (já temos)
6. Clique em **"Create repository"**

**Opção B: Via CLI (GitHub CLI)**
```bash
# Criar repositório público
gh repo create uninassau-atividade-alunos-ml-regressao --public --source=. --remote=origin

# Fazer push
git push -u origin main
```

### 3️⃣ Configurar como Template Repository

**Via Interface Web:**
1. Vá até o repositório: https://github.com/durvallins/uninassau-atividade-alunos-ml-regressao
2. Clique em **Settings** (Configurações)
3. Na seção **General**, marque:
   - ☑️ **Template repository**
4. Salvar alterações

**Resultado:** Agora o repositório pode ser usado como template no GitHub Classroom!

---

## 🎓 Configurar GitHub Classroom

### 1️⃣ Criar Organização (se não tiver)

1. Acesse: https://github.com/organizations/plan
2. Clique em **"Create an organization"**
3. Escolha: **"Create a free organization"**
4. Nome: `uninassau-ml-2025-1` (ou similar)
5. Siga os passos de configuração

### 2️⃣ Criar Classroom

1. Acesse: https://classroom.github.com/
2. Clique em **"New classroom"**
3. Selecione a organização criada
4. Nome do Classroom: `Introdução à Machine Learning - 2025.1`
5. Configure permissões conforme necessário

### 3️⃣ Criar Assignment (Atividade)

1. No Classroom, clique em **"New assignment"**
2. Configure:
   - **Assignment title:** `Projeto Final - Modelos de Regressão`
   - **Deadline:** [Data de entrega da Semana 4]
   - **Repository visibility:** Private
   - **Grant students admin access:** ✅ (permite criar branches)
   - **Template repository:** Selecione `durvallins/uninassau-atividade-alunos-ml-regressao`
   - **Supported editors:** Jupyter, Visual Studio Code
   - **Enable feedback pull requests:** ✅ (opcional, útil para revisão)

3. Clique em **"Create assignment"**

### 4️⃣ Distribuir Link aos Alunos

Após criar a assignment, você receberá um **link de convite**.

Exemplo: `https://classroom.github.com/a/xxxxxxxx`

**Compartilhe este link com os alunos!**

Quando o aluno clicar:
1. GitHub criará automaticamente uma cópia do template
2. Nome do repositório: `projeto-ml-regressao-[username]`
3. Aluno terá acesso completo ao seu repositório individual

---

## 📅 Cronograma Sugerido de Entregas

### Semana 1: Análise Exploratória (EDA)
- **Prazo:** [DD/MM/AAAA]
- **Branch:** `semana/1-analise-exploratoria`
- **Entregável:** `notebooks/01_EDA.ipynb`
- **Pull Request:** Abrir PR para `main` ao final

### Semana 2: Pré-processamento + Baseline
- **Prazo:** [DD/MM/AAAA]
- **Branch:** `semana/2-preprocessamento-baseline`
- **Entregáveis:**
  - `notebooks/02_Preprocessamento_Baseline.ipynb`
  - `data/processed/dataset_clean.csv`
- **Pull Request:** Abrir PR para `main` ao final

### Semana 3: Modelos Avançados
- **Prazo:** [DD/MM/AAAA]
- **Branch:** `semana/3-modelos-avancados`
- **Entregável:** `notebooks/03_Modelos_Avancados.ipynb`
- **Pull Request:** Abrir PR para `main` ao final

### Semana 4: Otimização + Relatório Final
- **Prazo:** [DD/MM/AAAA]
- **Branch:** `semana/4-otimizacao-final`
- **Entregáveis:**
  - `notebooks/04_Otimizacao_Final.ipynb`
  - `docs/RELATORIO_FINAL.md`
- **Pull Request:** Abrir PR para `main` ao final

---

## 🔍 Como Revisar Trabalhos dos Alunos

### Via GitHub (Manual)

1. Acesse o repositório do aluno
2. Vá em **Pull Requests**
3. Abra o PR da semana (ex: "ENTREGA SEMANA 1")
4. Revise:
   - **Files changed:** Ver código e notebooks
   - **Commits:** Verificar histórico de desenvolvimento
   - **Checks:** (se configurado) Autograding
5. Deixe comentários inline no código
6. Aprove ou solicite mudanças
7. Fazer **Merge** quando aprovar

### Via GitHub Classroom Dashboard

1. Acesse: https://classroom.github.com/
2. Selecione o Classroom
3. Clique na Assignment
4. Visualize lista de alunos e status:
   - ✅ Accepted (aluno aceitou)
   - 🔄 In Progress (commits feitos)
   - ⏸️ Not Started (sem commits)
5. Clique em cada repositório para revisar

---

## ⚙️ Configurações Opcionais Avançadas

### 1. Autograding (Avaliação Automática)

GitHub Classroom permite criar testes automáticos.

**Exemplo: Verificar se notebook executa sem erros**

```yaml
# .github/workflows/autograding.yml
name: Autograding

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install nbconvert pytest

      - name: Test Notebook Execution
        run: |
          jupyter nbconvert --to notebook --execute notebooks/01_EDA.ipynb
```

### 2. Branch Protection Rules

Proteger a `main` para que PRs sejam obrigatórios:

1. Settings → Branches → Add rule
2. Branch name pattern: `main`
3. Marcar:
   - ☑️ Require pull request before merging
   - ☑️ Require approvals (1)
4. Save changes

### 3. GitHub Pages (Opcional)

Hospedar notebooks renderizados:

1. Settings → Pages
2. Source: `main` branch, `/docs` folder
3. Alunos podem adicionar relatórios HTML em `docs/`

---

## 📊 Critérios de Avaliação (Rubrica)

Sugestão de rubrica por entrega:

| Critério | Peso | Descrição |
|----------|:----:|-----------|
| **Código Funcional** | 30% | Notebook executa sem erros (`Restart & Run All`) |
| **Análise Técnica** | 30% | Qualidade da análise, uso correto de técnicas |
| **Documentação** | 20% | Código comentado, markdown claro, interpretações |
| **Fluxo Git** | 10% | Commits descritivos, frequentes, uso correto de branches |
| **Visualizações** | 10% | Gráficos informativos, bem formatados, com labels |

**Total:** 100% (1.0 ponto por semana × 4 semanas = 4.0 pontos)

---

## 🆘 Troubleshooting

### Problema: Alunos não conseguem fazer push

**Solução:** Verificar permissões do repositório
- Settings → Collaborators → Verificar se aluno tem acesso

### Problema: Template não aparece na lista

**Solução:** Confirmar que marcou "Template repository" nas settings

### Problema: Autograding não funciona

**Solução:**
- Verificar sintaxe do arquivo `.github/workflows/autograding.yml`
- Checar logs em Actions tab

### Problema: Alunos estão commitando na `main` direto

**Solução:** Configurar Branch Protection Rules (veja seção anterior)

---

## 📞 Suporte

### Documentação Oficial
- [GitHub Classroom Docs](https://docs.github.com/en/education/manage-coursework-with-github-classroom)
- [GitHub Actions](https://docs.github.com/en/actions)

### Comunidade
- [GitHub Education Community](https://education.github.community/)
- [Discord - GitHub Education](https://discord.gg/github-education)

---

## ✅ Checklist Final

Antes de distribuir aos alunos:

- [ ] Template repository criado no GitHub
- [ ] Marcado como "Template repository" nas settings
- [ ] Todos os arquivos estão commitados
- [ ] README.md está completo e claro
- [ ] Dataset está em `data/raw/`
- [ ] `.gitignore` está configurado
- [ ] `requirements.txt` está atualizado
- [ ] GitHub Classroom configurado
- [ ] Assignment criada
- [ ] Link de convite gerado
- [ ] Prazo de entrega definido
- [ ] Rubrica de avaliação pronta
- [ ] (Opcional) Autograding configurado
- [ ] (Opcional) Branch protection configurado

---

## 🎉 Pronto para Uso!

Seu template está completo e pronto para ser usado com GitHub Classroom.

**Próxima ação:** Compartilhar o link de convite do GitHub Classroom com os alunos!

---

**Criado em:** Outubro 2027
**Última atualização:** Outubro 2027
