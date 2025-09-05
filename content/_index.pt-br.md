---
draft: false
aliases: ["/pt-br/"]
layout: single
---

# Conventional Branch 1.0.0

## Resumo

Conventional Branch é uma convenção estruturada e padronizada para nomeação de branches no Git, que visa tornar os nomes dos branches mais legíveis e acionáveis. Sugerimos alguns prefixos de branch que você pode usar, mas também é possível especificar sua própria convenção de nomes. Uma convenção consistente facilita a identificação dos branches pelo tipo.

### Pontos-chave

1. **Nomes de branches orientados ao propósito**: cada nome de branch indica claramente seu propósito, facilitando para todos os desenvolvedores entenderem para que serve o branch.
2. **Integração com CI/CD**: ao usar nomes de branch consistentes, é possível auxiliar sistemas automatizados (como pipelines de integração contínua/entrega contínua) a disparar ações específicas com base no tipo de branch (como implantação automática a partir de branches de release).
3. **Colaboração em equipe**: incentiva a colaboração dentro das equipes ao tornar explícito o propósito do branch, reduzindo mal-entendidos e facilitando a troca de tarefas entre membros sem confusão.

## Especificação

### Prefixos de nomeação de branch

A especificação de branch suporta os seguintes prefixos e deve ser estruturada da seguinte forma:

---

```
<tipo>/<descrição>
```

- **`main`**: o branch principal de desenvolvimento (ex.: `main`, `master` ou `develop`);
- **`feature/`** (or **`feat/`**): para novas funcionalidades (ex.: `feature/add-login-page`, `feat/add-login-page`);
- **`bugfix/`** (or **`fix/`**): para correções de bugs (ex.: `bugfix/fix-header-bug`, `fix/header-bug`);
- **`hotfix/`**: para correções urgentes (ex.: `hotfix/correcao-seguranca`);
- **`release/`**: para branches de release (ex.: `release/v1.2.0`); e
- **`chore/`**: para tarefas não relacionadas ao código, como atualização de dependências ou documentação (ex.: `chore/atualizar-dependencias`).

---

### Regras básicas

1. **Use letras minúsculas, números, hífens e pontos**: sempre use letras minúsculas (`a-z`), números (`0-9`) e hífens (`-`) para separar palavras. Evite caracteres especiais, underlines ou espaços. Para branches de release, pontos (`.`) podem ser usados na descrição para representar versões (ex.: `release/v1.2.0`).
2. **Sem hífens ou pontos consecutivos, iniciais ou finais**: certifique-se de que hífens e pontos não apareçam consecutivamente (ex.: `feature/novo--login`, `release/v1.-2.0`), nem no início ou fim da descrição (ex.: `feature/-novo-login`, `release/v1.2.0.`).
3. **Seja claro e conciso**: o nome do branch deve ser descritivo, mas conciso, indicando claramente o propósito do trabalho.
4. **Inclua o número do ticket**: se aplicável, inclua o número do ticket da sua ferramenta de gestão de projetos para facilitar o rastreamento. Por exemplo, para o ticket `issue-123`, o nome do branch pode ser `feature/issue-123-novo-login`.

## Conclusão

- **Comunicação clara**: o nome do branch por si só já fornece um entendimento claro do propósito da alteração de código.
- **Amigável para automação**: facilmente integrável a processos automatizados, possibilitando, por exemplo, a configuração de diferentes workflows para `feature`, `release` etc.
- **Escalabilidade**: funciona bem em equipes grandes, onde muitos desenvolvedores trabalham em tarefas diferentes simultaneamente.

Em resumo, o Conventional Branch foi projetado para melhorar a organização do projeto, a comunicação e a automação nos fluxos de trabalho com Git.

## Perguntas frequentes

### Quais ferramentas podem ser usadas para identificar automaticamente se um membro da equipe não segue esta especificação?

Você pode usar o [commit-check](https://github.com/commit-check/commit-check) para verificar a especificação de branch ou o [commit-check-action](https://github.com/commit-check/commit-check-action) se seu código estiver hospedado no GitHub.
