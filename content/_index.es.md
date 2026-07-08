---
draft: false
aliases: ["/es/"]
layout: single
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

1. **Usar alfanuméricos en minúsculas, guiones y puntos**: Utilice siempre letras minúsculas (`a-z`), números (`0-9`) y guiones (`-`) para separar palabras. Evite caracteres especiales, guiones bajos o espacios. Para las ramas de release, los puntos (`.`) se pueden usar en la descripción para representar números de versión (p. ej., `release/v1.2.0`).
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

### ¿Cómo se relaciona Conventional Branch con Conventional Commits?

Conventional Branch está inspirado en [Conventional Commits](https://www.conventionalcommits.org) y sigue una filosofía similar: aportar estructura legible por humanos y máquinas a los metadatos de Git. Mientras que Conventional Commits estandariza los mensajes de commit, Conventional Branch estandariza los nombres de ramas. Ambas especificaciones se complementan de forma natural.

### ¿Por qué los tipos de ramas no son tan detallados como los Conventional Commits (p. ej., `build`, `ci`, `docs`, `style`, `refactor`)?

Las ramas son diferentes de los commits: son temporales y se usan principalmente hasta que se fusionan. Introducir demasiados tipos para las ramas sería innecesario y dificultaría su gestión y memorización.

### ¿Puedo definir mis propios tipos de ramas más allá de los listados?

Sí. La especificación define un conjunto recomendado de tipos, pero los equipos pueden definir tipos personalizados adicionales para su flujo de trabajo. Sin embargo, es importante documentar claramente los tipos personalizados para que todos los miembros del equipo y las herramientas automatizadas estén al tanto de ellos.

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
