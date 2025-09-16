---
draft: false
aliases: ["/pl/"]
layout: single
---

# Conventional Branch 1.0.0

## Podsumowanie

Conventional Branch odnosi się do uporządkowanej i ustandaryzowanej konwencji nazewnictwa gałęzi Git, której celem jest uczynienie gałęzi bardziej czytelnymi i wykonalnymi. Zaproponowaliśmy kilka prefiksów gałęzi, które możesz chcieć używać, ale możesz także określić własną konwencję nazewnictwa. Spójna konwencja nazewnictwa ułatwia identyfikację gałęzi według typu.

### Kluczowe punkty

1. **Nazwy gałęzi zorientowane na cel**: Każda nazwa gałęzi jasno wskazuje jej cel, ułatwiając wszystkim programistom zrozumienie, do czego służy gałąź.
2. **Integracja z CI/CD**: Używając spójnych nazw gałęzi, można pomóc zautomatyzowanym systemom (takim jak potoki Continuous Integration/Continuous Deployment) w wyzwalaniu określonych działań na podstawie typu gałęzi (np. automatyczne wdrożenie z gałęzi wydania).
3. **Współpraca zespołowa**: Zachęca do współpracy w zespołach poprzez wyjaśnienie celu gałęzi, zmniejszenie nieporozumień i ułatwienie członkom zespołu przełączania się między zadaniami bez zamieszania.

## Specyfikacja

### Prefiksy nazw gałęzi

Specyfikacja gałęzi obsługuje następujące prefiksy i powinna być zorganizowana jako:

---

```
<typ>/<opis>
```

- **`main`**: Główna gałąź deweloperska (np. `main`, `master`, lub `develop`)
- **`feature/`** (lub **`feat/`**): Dla nowych funkcji (np. `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (lub **`fix/`**): Dla poprawek błędów (np. `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`**: Dla pilnych poprawek (np. `hotfix/security-patch`)
- **`release/`**: Dla gałęzi przygotowujących wydanie (np. `release/v1.2.0`)
- **`chore/`**: Dla zadań niezwiązanych z kodem, takich jak zależności, aktualizacje dokumentacji (np. `chore/update-dependencies`)

---

### Podstawowe zasady

1. **Używaj małych liter, cyfr, myślników i kropek**: Zawsze używaj małych liter (`a-z`), cyfr (`0-9`) i myślników (`-`) do oddzielania słów. Unikaj znaków specjalnych, podkreśleń lub spacji. W przypadku gałęzi wydania kropki (`.`) mogą być używane w opisie do reprezentowania numerów wersji (np. `release/v1.2.0`).
2. **Bez następujących po sobie, wiodących lub końcowych myślników lub kropek**: Upewnij się, że myślniki i kropki nie pojawiają się kolejno po sobie (np. `feature/new--login`, `release/v1.-2.0`), ani na początku czy końcu opisu (np. `feature/-new-login`, `release/v1.2.0.`).
3. **Zachowaj jasność i zwięzłość**: Nazwa gałęzi powinna być opisowa, ale zwięzła, jasno wskazująca cel pracy.
4. **Dołącz numery biletów**: Jeśli to możliwe, dołącz numer biletu z narzędzia zarządzania projektami, aby ułatwić śledzenie. Na przykład, dla biletu `issue-123`, nazwa gałęzi mogłaby być `feature/issue-123-new-login`.

## Wnioski

- **Jasna komunikacja**: Sama nazwa gałęzi zapewnia jasne zrozumienie jej celu i zmiany kodu.
- **Przyjazna dla automatyzacji**: Łatwo integruje się z procesami automatyzacji (np. różne przepływy pracy dla `feature`, `release`, itp.).
- **Skalowalność**: Dobrze sprawdza się w dużych zespołach, gdzie wielu programistów pracuje jednocześnie nad różnymi zadaniami.

Podsumowując, conventional branch został zaprojektowany w celu poprawy organizacji projektu, komunikacji i automatyzacji w przepływach pracy Git.

## FAQ

### Dlaczego typy gałęzi nie są tak szczegółowe jak w Conventional Commits (np. `build`, `ci`, `docs`, `style`, `refactor`)?

Gałęzie różnią się od commitów — są tymczasowe i używane głównie do momentu scalenia. Wprowadzenie zbyt wielu typów dla gałęzi byłoby niepotrzebne i utrudniłoby ich zarządzanie oraz zapamiętywanie.

### Jakich narzędzi można użyć, aby automatycznie sprawdzić, czy członek zespołu nie spełnia tej specyfikacji?

Możesz użyć [commit-check](https://github.com/commit-check/commit-check) do sprawdzania specyfikacji gałęzi lub [commit-check-action](https://github.com/commit-check/commit-check-action), jeśli twój kod jest hostowany na GitHub.