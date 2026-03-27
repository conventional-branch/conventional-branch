---
draft: false
aliases: ["/es/"]
layout: single
---

# Conventional Branch 1.0.0

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

- **`main`**: La rama principal de desarrollo (p. ej., `main`, `master` o `develop`)
- **`feature/`** (o **`feat/`**): Para nuevas funcionalidades (p. ej., `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (o **`fix/`**): Para correcciones de errores (p. ej., `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`**: Para correcciones urgentes (p. ej., `hotfix/security-patch`)
- **`release/`**: Para ramas que preparan un lanzamiento (p. ej., `release/v1.2.0`)
- **`chore/`**: Para tareas no relacionadas con código, como actualizaciones de dependencias o documentación (p. ej., `chore/update-dependencies`)

---

### Reglas básicas

1. **Usar alfanuméricos en minúsculas, guiones y puntos**: Utilice siempre letras minúsculas (`a-z`), números (`0-9`) y guiones (`-`) para separar palabras. Evite caracteres especiales, guiones bajos o espacios. Para las ramas de release, los puntos (`.`) se pueden usar en la descripción para representar números de versión (p. ej., `release/v1.2.0`).
2. **Sin guiones o puntos consecutivos, iniciales o finales**: Asegúrese de que los guiones y los puntos no aparezcan de forma consecutiva (p. ej., `feature/new--login`, `release/v1.-2.0`), ni al inicio o al final de la descripción (p. ej., `feature/-new-login`, `release/v1.2.0.`).
3. **Ser claro y conciso**: El nombre de la rama debe ser descriptivo pero conciso, indicando claramente el propósito del trabajo.
4. **Incluir números de ticket**: Si corresponde, incluya el número de ticket de su herramienta de gestión de proyectos para facilitar el seguimiento. Por ejemplo, para un ticket `issue-123`, el nombre de la rama podría ser `feature/issue-123-new-login`.

## Conclusión

- **Comunicación clara**: El nombre de la rama por sí solo proporciona una comprensión clara de su propósito y del cambio de código.
- **Compatible con la automatización**: Se integra fácilmente en procesos automatizados (p. ej., diferentes flujos de trabajo para `feature`, `release`, etc.).
- **Escalabilidad**: Funciona bien en equipos grandes donde muchos desarrolladores trabajan en diferentes tareas simultáneamente.

En resumen, conventional branch está diseñado para mejorar la organización del proyecto, la comunicación y la automatización en los flujos de trabajo con Git.

## Preguntas frecuentes

### ¿Por qué los tipos de ramas no son tan detallados como los Conventional Commits (p. ej., `build`, `ci`, `docs`, `style`, `refactor`)?

Las ramas son diferentes de los commits: son temporales y se usan principalmente hasta que se fusionan. Introducir demasiados tipos para las ramas sería innecesario y dificultaría su gestión y memorización.

### ¿Qué herramientas se pueden usar para identificar automáticamente si un miembro del equipo no cumple con esta especificación?

Puede usar [commit-check](https://github.com/commit-check/commit-check) para verificar la especificación de ramas o [commit-check-action](https://github.com/commit-check/commit-check-action) si su código está alojado en GitHub.
