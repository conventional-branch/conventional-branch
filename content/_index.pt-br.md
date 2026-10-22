---
draft: false
aliases: ["/pt-br/"]
layout: single
seoTitle: "Convenção de nomes de branches Git — Conventional Branch"
seoDescription: "Uma especificação para nomes de branches Git: os prefixos feature/, bugfix/, hotfix/, release/ e chore/, uma gramática formal e como aplicá-la no GitHub e no GitLab."
---

# Conventional Branch 1.1.0

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

**Prefixos de propósito** — descrevem a intenção do trabalho:
- **`feature/`** (or **`feat/`**): para novas funcionalidades (ex.: `feature/add-login-page`, `feat/add-login-page`);
- **`bugfix/`** (or **`fix/`**): para correções de bugs (ex.: `bugfix/fix-header-bug`, `fix/header-bug`);
- **`hotfix/`**: para correções urgentes (ex.: `hotfix/correcao-seguranca`);
- **`release/`**: para branches de release (ex.: `release/v1.2.0`); e
- **`chore/`**: para tarefas não relacionadas ao código, como atualização de dependências ou documentação (ex.: `chore/atualizar-dependencias`).

**Prefixos de fonte de agente de IA** — identificam branches gerados por agentes de codificação de IA:
{{< agents >}}

Esta lista está fechada: um agente sem prefixo próprio usa `ai/`.

Branches tronco (`main`, `master`, `develop`) não usam prefixo.

---

### Regras básicas

1. **Use letras minúsculas, números, hífens e pontos**: sempre use letras minúsculas (`a-z`), números (`0-9`) e hífens (`-`) para separar palavras. Evite caracteres especiais, underlines ou espaços. Pontos (`.`) são permitidos em qualquer descrição, normalmente para números de versão (ex.: `release/v1.2.0`, `chore/upgrade-node-v20.11`).
2. **Sem hífens ou pontos consecutivos, iniciais ou finais**: certifique-se de que hífens e pontos não apareçam consecutivamente (ex.: `feature/novo--login`, `release/v1.-2.0`), nem no início ou fim da descrição (ex.: `feature/-novo-login`, `release/v1.2.0.`).
3. **Seja claro e conciso**: o nome do branch deve ser descritivo, mas conciso, indicando claramente o propósito do trabalho.
4. **Inclua o número do ticket**: se aplicável, inclua o número do ticket da sua ferramenta de gestão de projetos para facilitar o rastreamento. Por exemplo, para o ticket `issue-123`, o nome do branch pode ser `feature/issue-123-novo-login`.


### Gramática formal

A gramática ABNF (Augmented Backus-Naur Form) a seguir define formalmente nomes de branches válidos:

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
                / "ai" / "copilot" / "cursor"
                / "claude" / "codex"
description     = desc-segment *("-" desc-segment)
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A   ; letras minúsculas a-z
DIGIT           = %x30-39   ; dígitos 0-9
```

> Nota: Hífens ou pontos consecutivos e hífens ou pontos no início ou no final da descrição não são permitidos.

### Exemplos

| Nome do branch | Válido | Notas |
|---|---|---|
| `main` | ✅ | Branch principal |
| `master` | ✅ | Branch principal |
| `develop` | ✅ | Branch principal |
| `feature/add-login-page` | ✅ | Nova funcionalidade |
| `feat/add-login-page` | ✅ | Alias curto para feature |
| `bugfix/fix-header-bug` | ✅ | Correção de bug |
| `fix/header-bug` | ✅ | Alias curto para bugfix |
| `hotfix/security-patch` | ✅ | Correção urgente |
| `release/v1.2.0` | ✅ | Release com número de versão |
| `chore/upgrade-node-v20.11` | ✅ | Pontos fora de um branch de release |
| `chore/update-dependencies` | ✅ | Tarefa não relacionada ao código |
| `feature/issue-123-new-login` | ✅ | Funcionalidade com número de ticket |
| `Feature/Add-Login` | ❌ | Maiúsculas não permitidas |
| `feature/new--login` | ❌ | Hífens consecutivos não permitidos |
| `feature/-new-login` | ❌ | Descrição não pode começar com hífen |
| `feature/new-login-` | ❌ | Descrição não pode terminar com hífen |
| `release/v1.-2.0` | ❌ | Hífen adjacente a ponto não permitido |
| `fix/header bug` | ❌ | Espaços não permitidos |
| `fix/header_bug` | ❌ | Sublinhados (`_`) não permitidos |
| `ai/refactor-auth-flow` | ✅ | Prefixo genérico de agente de IA |
| `copilot/add-login-page` | ✅ | GitHub Copilot |
| `cursor/fix-header-bug` | ✅ | Cursor |
| `claude/security-patch` | ✅ | Claude Code da Anthropic |
| `codex/optimize-query` | ✅ | OpenAI Codex |
| `unknown/some-task` | ❌ | Tipo de prefixo desconhecido |

## Conclusão

- **Comunicação clara**: o nome do branch por si só já fornece um entendimento claro do propósito da alteração de código.
- **Amigável para automação**: facilmente integrável a processos automatizados, possibilitando, por exemplo, a configuração de diferentes workflows para `feature`, `release` etc.
- **Escalabilidade**: funciona bem em equipes grandes, onde muitos desenvolvedores trabalham em tarefas diferentes simultaneamente.

Em resumo, o Conventional Branch foi projetado para melhorar a organização do projeto, a comunicação e a automação nos fluxos de trabalho com Git.

## Ferramentas

{{< tooling compact >}}

## Perguntas frequentes

### O que é um nome de branch?

Um nome de branch é o rótulo que o Git dá a uma linha de desenvolvimento, como `main` ou `feature/add-login-page`; o Git o guarda como uma ref em `refs/heads/`. O Git aceita uma grande variedade de nomes, então, sozinho, um nome de branch não diz nada confiável sobre o trabalho feito nele. O Conventional Branch dá a ele uma estrutura, `<tipo>/<descrição>`: um tipo que diz para que serve o trabalho, seguido de uma descrição curta, em letras minúsculas, com as palavras separadas por hífens. Por exemplo:

- `feature/add-login-page`
- `bugfix/fix-header-bug`
- `release/v1.2.0`

Branches tronco (`main`, `master`, `develop`) não usam prefixo.

### Como devo nomear um branch de feature?

Comece com `feature/`, ou com o alias curto `feat/`, e descreva a funcionalidade depois da barra. Se o trabalho tiver um ticket na sua ferramenta de gestão de projetos, inclua o número dele. Por exemplo:

- `feature/add-login-page`
- `feat/add-login-page`
- `feature/issue-123-new-login`

### O que é um branch de chore?

Um branch `chore/` é para tarefas não relacionadas ao código, como atualizar dependências ou documentação. Os tipos de branch são, de propósito, menos numerosos que os tipos do Conventional Commits (veja abaixo), então esse tipo de manutenção fica em `chore/`. Por exemplo:

- `chore/update-dependencies`
- `chore/upgrade-node-v20.11`
- `chore/update-generated-files`

Alguns bots de dependências, como o Renovate, também podem ser configurados para usar esse prefixo; veja [Bots e automação](/enforce/#name-them-to-fit).

### Como devo nomear um branch de release?

Use `release/` seguido do que o branch prepara, normalmente o número da versão. Pontos são permitidos, mas não no início ou no fim da descrição, nem ao lado de um hífen:

- `release/v1.2.0` — válido
- `release/v1.2.0.` — inválido: ponto no final
- `release/v1.-2.0` — inválido: hífen ao lado de um ponto

Um prefixo consistente também permite que um pipeline atue sobre `release/*`, por exemplo para fazer a implantação automática a partir de branches de release.

### Como devo nomear um branch de hotfix?

Use `hotfix/` para uma correção urgente e `bugfix/` (ou `fix/`) para uma que não seja. Descreva o que está sendo corrigido e inclua o número do ticket, se houver. Por exemplo:

- `hotfix/security-patch`
- `hotfix/issue-123-security-patch`
- `bugfix/fix-header-bug`, para uma correção que não é urgente

### Como o Conventional Branch se relaciona com o Conventional Commits?

O Conventional Branch foi inspirado pelo [Conventional Commits](https://www.conventionalcommits.org) e segue uma filosofia semelhante: trazer estrutura legível por humanos e máquinas para os metadados do Git. Enquanto o Conventional Commits padroniza mensagens de commit, o Conventional Branch padroniza nomes de branches. As duas especificações se complementam naturalmente.

### O Conventional Branch inventou esses prefixos?

Não. Prefixos como `feature/`, `hotfix/` e `release/` foram popularizados por volta de 2010 pela ferramenta [git-flow](https://github.com/nvie/gitflow) e são o padrão em ferramentas como o [modelo de branches do Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-a-projects-branching-model/). O Conventional Branch se apoia nessa prática em vez de substituí-la. O que ele acrescenta é uma definição precisa que pessoas e ferramentas podem compartilhar: um conjunto fixo de tipos, uma gramática formal, uma regex de validação publicada em [`spec.json`](/spec.json) e casos de conformidade, para que todo validador aceite exatamente os mesmos nomes.

### Por que os tipos de branch não são tão detalhados quanto os Conventional Commits (por exemplo, `build`, `ci`, `docs`, `style`, `refactor`)?

Branches são diferentes de commits – são temporários e usados principalmente até serem mesclados. Introduzir muitos tipos de branch seria desnecessário e tornaria mais difícil gerenciá-los e lembrá-los.

### Posso definir meus próprios tipos de branch além dos listados?

Sim, como uma extensão da equipe. Os tipos da gramática são os que toda ferramenta conforme aceita, então um branch como `unknown/some-task` é inválido segundo a própria especificação. Uma equipe que precise de mais tipos (por exemplo, `experiment/`) deve declará-los explicitamente no seu validador (por exemplo, em `allow_branch_types` do [commit-check](/enforce/#commit-check)) e documentá-los, para que os membros da equipe e as ferramentas automatizadas fiquem alinhados. O próprio repositório da especificação, por exemplo, adiciona `dependabot/` à sua [configuração do commit-check](https://github.com/conventional-branch/conventional-branch/blob/main/commit-check.toml) para os branches abertos pelo Dependabot.

### Por que os nomes de branch devem ser em minúsculas?

Por dois motivos. Primeiro, o Git costuma guardar as referências de branch como arquivos em `.git/refs/heads/`, e os sistemas de arquivos padrão do macOS e do Windows não diferenciam maiúsculas de minúsculas: `Feature/login` e `feature/login` apontam ali para o mesmo caminho, enquanto no Linux são dois branches diferentes. Por isso, um repositório que aceita as duas formas pode se comportar de maneira diferente em cada clone. Segundo, uma única grafia é mais fácil de digitar, buscar e filtrar: uma ferramenta acionada por `release/*` não precisa prever também `Release/*`.

### Quais são as principais diferenças entre v1.1.0 e v1.0.0?

v1.1.0 adiciona **Prefixos de fonte de agente de IA** como a principal nova funcionalidade (veja a próxima pergunta frequente para saber por que foram introduzidos). Também inclui um site versionado com um seletor de versão para que os usuários possam navegar pelas especificações v1.0.0 e v1.1.0. Todos os nomes de branch v1.0.0 existentes permanecem totalmente válidos — sem alterações que quebrem a compatibilidade.

### Por que adicionar prefixos de fonte de agente de IA?

Agentes de codificação de IA (GitHub Copilot, Cursor, Claude Code, OpenAI Codex, etc.) são cada vez mais usados para gerar código e criar pull requests. Cada agente usa seu próprio prefixo de branch (ex.: `copilot/`, `cursor/`). Ao padronizar esses prefixos na especificação Conventional Branch, possibilitamos:
1. **Identificação rápida** — revisores e ferramentas podem reconhecer imediatamente PRs gerados por IA
2. **Validação por ferramentas** — ferramentas como commit-check podem validar branches de agentes de IA contra a especificação
3. **Uma lista estável** — os cinco prefixos são fixos e qualquer outro agente usa `ai/`, então a gramática não muda a cada nova ferramenta

O prefixo genérico `ai/` está disponível para qualquer agente de IA sem um prefixo dedicado, ou para equipes que preferem um identificador neutro em relação ao fornecedor. Esta é a principal novidade lançada na **v1.1.0** — para um resumo completo das mudanças entre versões, veja a pergunta frequente acima.

### Como devo lidar com branches de longa duração como `develop` ou `staging`?

Na gramática formal da especificação, apenas `main`, `master` e `develop` são considerados `trunk-branch`. Outros branches de integração ou de ambiente de longa duração (por exemplo, `staging`, `production`) podem ser adotados por cada projeto como extensões específicas da convenção, também sem prefixo, desde que sejam documentados e usados de forma consistente em todo o projeto.

### Quais ferramentas podem ser usadas para identificar automaticamente se um membro da equipe não segue esta especificação?

Você pode usar o [commit-check](https://github.com/commit-check/commit-check) para verificar a especificação de branch ou o [commit-check-action](https://github.com/commit-check/commit-check-action) se seu código estiver hospedado no GitHub.
