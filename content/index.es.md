---
draft: false
aliases: ["/es/"]
layout: single
seoTitle: "Convención de nombres de ramas Git — Conventional Branch"
seoDescription: "Una especificación para nombrar ramas de Git: prefijos feature/, bugfix/, hotfix/, release/ y chore/, una gramática formal y cómo aplicarla en GitHub y GitLab."
---

# Conventional Branch 1.1.0

## Resumen

Conventional Branch hace referencia a una convención de nomenclatura estructurada y estandarizada para ramas de Git, cuyo objetivo es hacer que las ramas sean más legibles y accionables. Hemos sugerido algunos prefijos de rama que quizás desee utilizar, pero también puede especificar su propia convención de nomenclatura. Una convención de nomenclatura coherente facilita la identificación de las ramas por tipo.

### Puntos clave

1. **Nombres de ramas orientados al propósito**: Cada nombre de rama indica claramente su propósito, lo que facilita a todos los desarrolladores entender para qué sirve la rama.
2. **Integración con CI/CD**: Al usar nombres de ramas coherentes, se puede ayudar a los sistemas automatizados (como los pipelines de integración continua/despliegue continuo) a activar acciones específicas según el tipo de rama (por ejemplo, despliegue automático desde ramas de release).
3. **Colaboración en equipo**: Fomenta la colaboración dentro de los equipos al hacer explícito el propósito de la rama, reduciendo malentendidos y facilitando el cambio entre tareas sin confusión.

## Especificación

### Prefijos de nomenclatura de ramas

La especificación de ramas admite los siguientes prefijos y debe estructurarse de la siguiente manera:

---

```
<tipo>/<descripción>
```

**Prefijos de propósito** — describen la intención del trabajo:
- **`feature/`** (o **`feat/`**): Para nuevas funcionalidades (p. ej., `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (o **`fix/`**): Para correcciones de errores (p. ej., `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`**: Para correcciones urgentes (p. ej., `hotfix/security-patch`)
- **`release/`**: Para ramas que preparan un lanzamiento (p. ej., `release/v1.2.0`)
- **`chore/`**: Para tareas no relacionadas con código, como actualizaciones de dependencias o documentación (p. ej., `chore/update-dependencies`)

**Prefijos de fuente de agente de IA** — identifican ramas generadas por agentes de codificación de IA:
{{< agents >}}

Las ramas troncales (`main`, `master`, `develop`) no usan prefijo.

---

### Reglas básicas

1. **Usar alfanuméricos en minúsculas, guiones y puntos**: Utilice siempre letras minúsculas (`a-z`), números (`0-9`) y guiones (`-`) para separar palabras. Evite caracteres especiales, guiones bajos o espacios. Los puntos (`.`) se permiten en cualquier descripción, normalmente para números de versión (p. ej., `release/v1.2.0`, `chore/upgrade-node-v20.11`).
2. **Sin guiones o puntos consecutivos, iniciales o finales**: Asegúrese de que los guiones y los puntos no aparezcan de forma consecutiva (p. ej., `feature/new--login`, `release/v1.-2.0`), ni al inicio o al final de la descripción (p. ej., `feature/-new-login`, `release/v1.2.0.`).
3. **Ser claro y conciso**: El nombre de la rama debe ser descriptivo pero conciso, indicando claramente el propósito del trabajo.
4. **Incluir números de ticket**: Si corresponde, incluya el número de ticket de su herramienta de gestión de proyectos para facilitar el seguimiento. Por ejemplo, para un ticket `issue-123`, el nombre de la rama podría ser `feature/issue-123-new-login`.


### Gramática formal

La siguiente gramática ABNF (Augmented Backus-Naur Form) define formalmente los nombres de ramas válidos:

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

> Nota: No se permiten guiones o puntos consecutivos, ni guiones o puntos al inicio o al final de la descripción.

### Ejemplos

| Nombre de rama | Válido | Notas |
|---|---|---|
| `main` | ✅ | Rama principal |
| `master` | ✅ | Rama principal |
| `develop` | ✅ | Rama principal |
| `feature/add-login-page` | ✅ | Nueva funcionalidad |
| `feat/add-login-page` | ✅ | Alias corto para feature |
| `bugfix/fix-header-bug` | ✅ | Corrección de error |
| `fix/header-bug` | ✅ | Alias corto para bugfix |
| `hotfix/security-patch` | ✅ | Corrección urgente |
| `release/v1.2.0` | ✅ | Release con número de versión |
| `chore/upgrade-node-v20.11` | ✅ | Puntos fuera de una rama de release |
| `chore/update-dependencies` | ✅ | Tarea no relacionada con código |
| `feature/issue-123-new-login` | ✅ | Funcionalidad con número de ticket |
| `Feature/Add-Login` | ❌ | Mayúsculas no permitidas |
| `feature/new--login` | ❌ | Guiones consecutivos no permitidos |
| `feature/-new-login` | ❌ | La descripción no puede comenzar con guion |
| `feature/new-login-` | ❌ | La descripción no puede terminar con guion |
| `release/v1.-2.0` | ❌ | Guion adyacente a punto no permitido |
| `fix/header bug` | ❌ | Espacios no permitidos |
| `fix/header_bug` | ❌ | Guiones bajos no permitidos |
| `ai/refactor-auth-flow` | ✅ | Prefijo genérico de agente de IA |
| `copilot/add-login-page` | ✅ | GitHub Copilot |
| `cursor/fix-header-bug` | ✅ | Cursor |
| `claude/security-patch` | ✅ | Claude Code de Anthropic |
| `codex/optimize-query` | ✅ | OpenAI Codex |
| `unknown/some-task` | ❌ | Tipo de prefijo desconocido |

## Conclusión

- **Comunicación clara**: El nombre de la rama por sí solo proporciona una comprensión clara de su propósito y del cambio de código.
- **Compatible con la automatización**: Se integra fácilmente en procesos automatizados (p. ej., diferentes flujos de trabajo para `feature`, `release`, etc.).
- **Escalabilidad**: Funciona bien en equipos grandes donde muchos desarrolladores trabajan en diferentes tareas simultáneamente.

En resumen, conventional branch está diseñado para mejorar la organización del proyecto, la comunicación y la automatización en los flujos de trabajo con Git.

## Herramientas

{{< tooling compact >}}

## Preguntas frecuentes

### ¿Qué es un nombre de rama?

Un nombre de rama es la etiqueta que Git da a una línea de desarrollo, como `main` o `feature/add-login-page`; Git lo guarda como una referencia (ref) en `refs/heads/`. Git acepta una gran variedad de nombres, así que un nombre de rama, por sí solo, no dice nada fiable sobre el trabajo que contiene. Conventional Branch le da una estructura, `<tipo>/<descripción>`: un tipo que indica para qué es el trabajo, seguido de una descripción breve, en minúsculas, con las palabras separadas por guiones. Por ejemplo:

- `feature/add-login-page`
- `bugfix/fix-header-bug`
- `release/v1.2.0`

Las ramas troncales (`main`, `master`, `develop`) no llevan prefijo.

### ¿Cómo debo nombrar una rama de feature?

Empiécela con `feature/`, o con el alias corto `feat/`, y describa la funcionalidad después de la barra. Si el trabajo tiene un ticket en su herramienta de gestión de proyectos, incluya su número. Por ejemplo:

- `feature/add-login-page`
- `feat/add-login-page`
- `feature/issue-123-new-login`

### ¿Qué es una rama de chore?

Una rama `chore/` es para tareas no relacionadas con código, como actualizar dependencias o documentación. Los tipos de rama son, a propósito, menos que los tipos de Conventional Commits (véase más abajo), así que este tipo de mantenimiento va en `chore/`. Por ejemplo:

- `chore/update-dependencies`
- `chore/upgrade-node-v20.11`
- `chore/update-generated-files`

Algunos bots de dependencias, como Renovate, también pueden configurarse para usar este prefijo; consulte [Bots y automatización](/enforce/#name-them-to-fit).

### ¿Cómo debo nombrar una rama de release?

Use `release/` seguido de lo que prepara la rama, normalmente el número de versión. Se permiten puntos, pero no al inicio ni al final de la descripción, ni junto a un guion:

- `release/v1.2.0` — válido
- `release/v1.2.0.` — inválido: punto al final
- `release/v1.-2.0` — inválido: guion junto a un punto

Un prefijo coherente también permite que un pipeline actúe sobre `release/*`, por ejemplo para desplegar automáticamente desde las ramas de release.

### ¿Cómo debo nombrar una rama de hotfix?

Use `hotfix/` para una corrección urgente y `bugfix/` (o `fix/`) para una que no lo sea. Describa lo que se corrige e incluya el número de ticket, si lo hay. Por ejemplo:

- `hotfix/security-patch`
- `hotfix/issue-123-security-patch`
- `bugfix/fix-header-bug`, para una corrección que no es urgente

### ¿Cómo se relaciona Conventional Branch con Conventional Commits?

Conventional Branch está inspirado en [Conventional Commits](https://www.conventionalcommits.org) y sigue una filosofía similar: aportar estructura legible por humanos y máquinas a los metadatos de Git. Mientras que Conventional Commits estandariza los mensajes de commit, Conventional Branch estandariza los nombres de ramas. Ambas especificaciones se complementan de forma natural.

### ¿Conventional Branch inventó estos prefijos?

No. Prefijos como `feature/`, `hotfix/` y `release/` se popularizaron hacia 2010 con la herramienta [git-flow](https://github.com/nvie/gitflow) y son los valores predeterminados de herramientas como el [modelo de ramas de Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-a-projects-branching-model/). Conventional Branch se basa en esa práctica en lugar de sustituirla. Lo que aporta es una definición precisa que personas y herramientas pueden compartir: un conjunto fijo de tipos, una gramática formal, una regex de validación publicada en [`spec.json`](/spec.json) y casos de conformidad, para que todos los validadores acepten exactamente los mismos nombres.

### ¿Por qué los tipos de ramas no son tan detallados como los Conventional Commits (p. ej., `build`, `ci`, `docs`, `style`, `refactor`)?

Las ramas son diferentes de los commits: son temporales y se usan principalmente hasta que se fusionan. Introducir demasiados tipos para las ramas sería innecesario y dificultaría su gestión y memorización.

### ¿Puedo definir mis propios tipos de ramas más allá de los listados?

Sí, como una extensión del equipo. Los tipos de la gramática son los que acepta cualquier herramienta conforme, así que una rama como `unknown/some-task` es inválida según la propia especificación. Un equipo que necesite más tipos (por ejemplo, `experiment/`) debe declararlos explícitamente en su validador (por ejemplo, en `allow_branch_types` de [commit-check](/enforce/#commit-check)) y documentarlos, para que los miembros del equipo y las herramientas automatizadas estén de acuerdo. El propio repositorio de la especificación, por ejemplo, añade `dependabot/` a su [configuración de commit-check](https://github.com/conventional-branch/conventional-branch/blob/main/commit-check.toml) para las ramas que abre Dependabot.

### ¿Por qué los nombres de rama deben ir en minúsculas?

Por dos razones. Primero, Git suele guardar las referencias de las ramas como archivos en `.git/refs/heads/`, y los sistemas de archivos predeterminados de macOS y Windows no distinguen mayúsculas de minúsculas: `Feature/login` y `feature/login` apuntan allí a la misma ruta, mientras que en Linux son dos ramas distintas. Por eso, un repositorio que permita ambas puede comportarse de forma distinta según el clon. Segundo, una sola grafía es más fácil de escribir, buscar y filtrar: una herramienta que se activa con `release/*` no tiene que prever también `Release/*`.

### ¿Cuáles son las principales diferencias entre v1.1.0 y v1.0.0?

v1.1.0 añade **Prefijos de fuente de agente de IA** como la nueva característica principal (consulte la siguiente entrada de preguntas frecuentes para saber por qué se introdujeron). También incluye un sitio web versionado con un conmutador de versiones para que los usuarios puedan navegar tanto por la especificación v1.0.0 como por la v1.1.0. Todos los nombres de ramas v1.0.0 existentes siguen siendo totalmente válidos — sin cambios que rompan la compatibilidad.

### ¿Por qué añadir prefijos de fuente de agente de IA?

Los agentes de codificación de IA (GitHub Copilot, Cursor, Claude Code, OpenAI Codex, etc.) se utilizan cada vez más para generar código y crear pull requests. Cada agente usa su propio prefijo de rama (p. ej., `copilot/`, `cursor/`). Al estandarizar estos prefijos en la especificación Conventional Branch, permitimos:
1. **Identificación rápida** — los revisores y las herramientas pueden reconocer inmediatamente los PRs generados por IA
2. **Validación de herramientas** — herramientas como commit-check pueden validar las ramas de agentes de IA según la especificación
3. **Un estándar de registro** — los nuevos agentes de IA pueden adoptar un prefijo documentado en lugar de inventar patrones ad-hoc

El prefijo genérico `ai/` está disponible para cualquier agente de IA que no tenga un prefijo dedicado, o para equipos que prefieran un identificador neutro respecto al proveedor. Esta es la nueva característica clave lanzada en **v1.1.0** — para un resumen completo de los cambios entre versiones, consulte la entrada de preguntas frecuentes anterior.

### ¿Cómo debo manejar ramas de larga duración como `develop` o `staging`?

Dentro de la gramática anterior, las ramas de tronco válidas son únicamente las definidas allí (por ejemplo, `main`/`master`/`develop`) y no requieren prefijo. Algunos equipos además utilizan ramas de integración o de entorno de larga duración (como `staging` o `production`); estas son una convención opcional de cada equipo y pueden no estar cubiertas por la gramática básica ni ser reconocidas por todas las herramientas, por lo que deben documentarse y configurarse explícitamente si se desea que las validen.

### ¿Qué herramientas se pueden usar para identificar automáticamente si un miembro del equipo no cumple con esta especificación?

Puede usar [commit-check](https://github.com/commit-check/commit-check) para verificar la especificación de ramas o [commit-check-action](https://github.com/commit-check/commit-check-action) si su código está alojado en GitHub.
