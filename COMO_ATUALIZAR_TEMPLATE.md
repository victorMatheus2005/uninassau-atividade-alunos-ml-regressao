# 🔄 Como Atualizar o Template Após Alunos Aceitarem a Tarefa

## ⚠️ Importante Entender

### Como Funciona o GitHub Classroom

Quando um aluno clica no link de convite e aceita a tarefa:
1. GitHub Classroom cria uma **cópia independente** do template naquele momento
2. O repositório do aluno **NÃO** está conectado ao seu template
3. Atualizações que você fizer no template **NÃO** vão automaticamente para repositórios já criados

---

## 📊 Cenários de Atualização

### Cenário 1: Aluno AINDA NÃO Aceitou a Tarefa ✅

**Situação:** Aluno ainda não clicou no link de convite

**Resultado:**
- ✅ Quando aceitar, receberá a versão MAIS RECENTE do template
- ✅ Suas atualizações estarão incluídas automaticamente

**Ação necessária:** Nenhuma! Basta atualizar o template normalmente.

---

### Cenário 2: Aluno JÁ Aceitou a Tarefa ⚠️

**Situação:** Aluno já tem seu repositório criado

**Resultado:**
- ❌ Repositório do aluno **NÃO** recebe atualizações automaticamente
- ❌ Aluno tem uma cópia "congelada" do template do momento que aceitou

**Ação necessária:** Usar a função **"Sync assignments"** do GitHub Classroom

---

## 🔄 Como Sincronizar Atualizações

### Passo 1: Atualizar o Template

Faça as alterações no repositório template:

```bash
cd /home/durval/Documentos/PROJETOS/ml-projeto-final/template-repo

# Fazer alterações nos arquivos
# Por exemplo, atualizar README.md, adicionar novos arquivos, etc.

# Commit
git add .
git commit -m "docs: Atualiza instruções da Semana 2"

# Push
git push origin main
```

### Passo 2: Sincronizar via GitHub Classroom

1. **Acesse o GitHub Classroom:**
   - https://classroom.github.com/

2. **Entre na Sala de Aula:**
   - Selecione sua Sala de Aula (ex: "Introdução à Machine Learning - 2025.1")

3. **Entre na Assignment:**
   - Clique em **"Machine Learning - Modelos de Regressão"**

4. **Sincronize:**
   - Procure o botão **"Sync assignments"** ou **"Sincronizar"**
   - Clique nele
   - Confirme a ação

5. **O Que Acontece:**
   - GitHub Classroom tenta fazer push dos seus commits para a `main` de **todos** os repositórios dos alunos
   - Se não houver conflitos, a atualização é feita automaticamente
   - Se houver conflitos, você verá quais repositórios falharam

---

## ⚠️ Problemas com Sincronização

### Por Que Pode Falhar?

A sincronização **só funciona bem** se:
- ✅ Alunos trabalharam em **branches** (ex: `semana/1-analise-exploratoria`)
- ✅ A branch `main` dos alunos está **intacta** (sem commits diretos)

A sincronização **vai falhar** se:
- ❌ Alunos fizeram commits **direto na `main`**
- ❌ Alunos modificaram os mesmos arquivos que você atualizou
- ❌ Há conflitos de merge

### Como Evitar Conflitos

**Instrua os alunos a:**

1. **SEMPRE trabalhar em branches:**
   ```bash
   git checkout -b semana/1-analise-exploratoria
   # Trabalhar na branch
   git add .
   git commit -m "Adiciona análise de correlação"
   git push origin semana/1-analise-exploratoria
   ```

2. **NÃO fazer commits direto na `main`:**
   ```bash
   # ❌ ERRADO
   git checkout main
   git add .
   git commit -m "..."

   # ✅ CORRETO
   git checkout -b semana/1-minha-tarefa
   git add .
   git commit -m "..."
   ```

3. **Fazer Pull da `main` regularmente:**
   ```bash
   # Antes de começar nova semana
   git checkout main
   git pull origin main  # Pega atualizações do professor
   git checkout -b semana/2-preprocessamento
   ```

---

## 📋 Boas Práticas para Atualizações

### 1. Timing das Atualizações

**✅ BOM MOMENTO:**
- Antes de muitos alunos aceitarem a tarefa
- Entre semanas (quando alunos não estão trabalhando ativamente)
- Fim de semana antes da próxima etapa

**❌ MAU MOMENTO:**
- Meio da semana quando alunos estão trabalhando
- Véspera de entrega
- Quando muitos alunos já commitaram na `main`

### 2. Tipo de Atualizações

**Fáceis de Sincronizar:**
- ✅ Adicionar novos arquivos (ex: instruções da próxima semana)
- ✅ Criar novas pastas
- ✅ Adicionar exemplos de código novos

**Difíceis de Sincronizar:**
- ⚠️ Modificar arquivos que alunos já editaram (ex: README.md)
- ⚠️ Deletar arquivos
- ⚠️ Renomear pastas

### 3. Comunicação com Alunos

Sempre que fizer uma sincronização:

**📧 Envie um aviso:**
```
Assunto: Atualização do Repositório Template

Olá pessoal!

Acabei de atualizar o repositório template com:
- Instruções da Semana 2
- Exemplos adicionais de código
- Correções no README.md

Para receber as atualizações:

1. Certifique-se de ter commitado todo seu trabalho
2. Execute:
   git checkout main
   git pull origin main

Se tiver problemas, me procurem!

Prof. Durval
```

---

## 🔧 Alternativas à Sincronização

Se a sincronização automática não funcionar, você tem outras opções:

### Opção 1: Issues Individuais

Crie uma Issue em cada repositório dos alunos:

1. Acesse repositório do grupo
2. Crie uma **Issue** explicando a atualização
3. Forneça instruções manuais:
   ```bash
   # Baixar arquivo atualizado
   curl -O https://raw.githubusercontent.com/professor-durval-ml/uninassau-atividade-alunos-ml-regressao/main/docs/INSTRUCOES_SEMANA2.md
   ```

### Opção 2: Pull Request Manual

1. Fork do repositório do aluno
2. Adicione os arquivos atualizados
3. Abra um Pull Request
4. Aluno faz merge

### Opção 3: Comunicação Simples

Para atualizações pequenas:
- 📧 Envie por e-mail
- 📎 Anexe os arquivos
- 📋 Alunos adicionam manualmente

---

## 📊 Exemplo Prático

### Situação Real:

**Você quer adicionar as instruções da Semana 2**

**Passo a Passo:**

1. **Criar o arquivo no template:**
   ```bash
   cd template-repo

   # Criar arquivo
   cat > docs/INSTRUCOES_SEMANA2.md << 'EOF'
   # Semana 2: Pré-processamento e Baseline

   ## Objetivos
   - Tratar valores faltantes
   - Feature engineering
   - Treinar modelo baseline
   EOF

   # Commit
   git add docs/INSTRUCOES_SEMANA2.md
   git commit -m "docs: Adiciona instruções da Semana 2"
   git push origin main
   ```

2. **Sincronizar no GitHub Classroom:**
   - Classroom → Assignment → "Sync assignments"
   - ✅ Sucesso! Arquivo adicionado em todos os repositórios

3. **Avisar os alunos:**
   ```bash
   📧 E-mail: "Instruções da Semana 2 disponíveis!
   Façam 'git pull origin main' para baixar."
   ```

4. **Alunos recebem:**
   ```bash
   git checkout main
   git pull origin main
   # Downloading docs/INSTRUCOES_SEMANA2.md
   ```

---

## ⚠️ Casos de Emergência

### Se a Sincronização Falhar Completamente

**Opção A: Criar Nova Assignment**
- Crie nova assignment com template atualizado
- Alunos migram trabalho para novo repositório
- **Desvantagem:** Perde histórico de commits

**Opção B: Instrução Manual**
- Forneça instruções passo a passo
- Alunos baixam arquivos individualmente
- **Desvantagem:** Trabalhoso

**Opção C: Aceitar Divergência**
- Grupos mais adiantados não recebem atualização
- Fornece atualização para novos grupos
- **Desvantagem:** Turma desalinhada

---

## ✅ Checklist para Atualizar Template

Antes de fazer qualquer atualização:

- [ ] Avalie se a atualização é realmente necessária
- [ ] Verifique se é bom momento (timing)
- [ ] Faça commit e push no template
- [ ] Use "Sync assignments" no GitHub Classroom
- [ ] Verifique se sincronização foi bem-sucedida
- [ ] Envie comunicado aos alunos
- [ ] Monitore Issues de alunos com problemas
- [ ] Ajude individualmente quem teve conflitos

---

## 🎯 Recomendação Final

**Melhor estratégia:**

1. **Configure o template COMPLETO antes de distribuir o link**
   - Inclua tudo que os alunos precisarão nas 4 semanas
   - Mesmo que eles não vejam tudo de uma vez (eles não lerão tudo no início)
   - Evita necessidade de sincronizações futuras

2. **Atualizações progressivas via comunicação:**
   - Semana 1: "Leiam a seção X do README.md"
   - Semana 2: "Agora consultem docs/INSTRUCOES_SEMANA2.md"
   - Semana 3: "Material em docs/SEMANA3/"

3. **Sincronizações apenas para correções críticas:**
   - Erros graves no código
   - Informações incorretas
   - Problemas de segurança

Dessa forma, você **minimiza sincronizações** e **maximiza a autonomia** dos alunos!

---

**Última atualização:** Outubro 2027
