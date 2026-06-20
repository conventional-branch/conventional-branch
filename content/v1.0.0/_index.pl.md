---
draft: false
layout: single
version: v1.0.0
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


### Formalna gramatyka

Poniższa gramatyka ABNF (Augmented Backus-Naur Form) formalnie definiuje prawidłowe nazwy gałęzi:

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
description     = desc-segment *("-" desc-segment)
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A   ; małe litery a-z
DIGIT           = %x30-39   ; cyfry 0-9
```

> Uwaga: Kolejne myślniki lub kropki oraz myślniki lub kropki na początku lub końcu opisu nie są dozwolone.

### Przykłady

| Nazwa gałęzi | Prawidłowa | Uwagi |
|---|---|---|
| `main` | ✅ | Gałąź główna |
| `master` | ✅ | Gałąź główna |
| `develop` | ✅ | Gałąź główna |
| `feature/add-login-page` | ✅ | Nowa funkcja |
| `feat/add-login-page` | ✅ | Krótki alias dla feature |
| `bugfix/fix-header-bug` | ✅ | Naprawa błędu |
| `fix/header-bug` | ✅ | Krótki alias dla bugfix |
| `hotfix/security-patch` | ✅ | Pilna naprawa |
| `release/v1.2.0` | ✅ | Wydanie z numerem wersji |
| `chore/update-dependencies` | ✅ | Zadanie niezwiązane z kodem |
| `feature/issue-123-new-login` | ✅ | Funkcja z numerem biletu |
| `Feature/Add-Login` | ❌ | Wielkie litery są niedozwolone |
| `feature/new--login` | ❌ | Kolejne myślniki są niedozwolone |
| `feature/-new-login` | ❌ | Opis nie może zaczynać się myślnikiem |
| `feature/new-login-` | ❌ | Opis nie może kończyć się myślnikiem |
| `release/v1.-2.0` | ❌ | Myślnik obok kropki jest niedozwolony |
| `fix/header bug` | ❌ | Spacje są niedozwolone |
| `fix/header_bug` | ❌ | Podkreślenia są niedozwolone |
| `unknown/some-task` | ❌ | Nieznany typ prefiksu |

## Wnioski

- **Jasna komunikacja**: Sama nazwa gałęzi zapewnia jasne zrozumienie jej celu i zmiany kodu.
- **Przyjazna dla automatyzacji**: Łatwo integruje się z procesami automatyzacji (np. różne przepływy pracy dla `feature`, `release`, itp.).
- **Skalowalność**: Dobrze sprawdza się w dużych zespołach, gdzie wielu programistów pracuje jednocześnie nad różnymi zadaniami.

Podsumowując, conventional branch został zaprojektowany w celu poprawy organizacji projektu, komunikacji i automatyzacji w przepływach pracy Git.

## Narzędzia

{{< tooling compact >}}

## FAQ

### Dlaczego typy gałęzi nie są tak szczegółowe jak w Conventional Commits (np. `build`, `ci`, `docs`, `style`, `refactor`)?

Gałęzie różnią się od commitów — są tymczasowe i używane głównie do momentu scalenia. Wprowadzenie zbyt wielu typów dla gałęzi byłoby niepotrzebne i utrudniłoby ich zarządzanie oraz zapamiętywanie.

### Jakich narzędzi można użyć, aby automatycznie sprawdzić, czy członek zespołu nie spełnia tej specyfikacji?

Możesz użyć [commit-check](https://github.com/commit-check/commit-check) do sprawdzania specyfikacji gałęzi lub [commit-check-action](https://github.com/commit-check/commit-check-action), jeśli twój kod jest hostowany na GitHub.

### Czy mogę zdefiniować własne typy gałęzi poza wymienionymi?

Tak. Specyfikacja definiuje zalecany zestaw typów, ale zespoły mogą definiować dodatkowe niestandardowe typy dla swojego przepływu pracy. Ważne jest jednak, aby jasno dokumentować niestandardowe typy, tak aby wszyscy członkowie zespołu i zautomatyzowane narzędzia były ich świadome.

### Jak Conventional Branch ma się do Conventional Commits?

Conventional Branch jest zainspirowany przez [Conventional Commits](https://www.conventionalcommits.org) i podąża za podobną filozofią: wprowadzenie struktury czytelnej dla ludzi i maszyn do metadanych Git. Podczas gdy Conventional Commits standaryzuje wiadomości commitów, Conventional Branch standaryzuje nazwy gałęzi. Obie specyfikacje naturalnie się uzupełniają.

### Jak radzić sobie z długo żyjącymi gałęziami, takimi jak `develop` lub `staging`?

Długo żyjące gałęzie integracyjne lub środowiskowe (np. `develop`, `staging`, `production`) są w praktyce często traktowane jak gałęzie główne i nie wymagają prefiksu, o ile w danym projekcie zostanie to jasno ustalone. Formalna gramatyka ABNF definiuje jednak gałąź główną (`trunk-branch`) jedynie jako `main`, `master` lub `develop`, a dodatkowe nazwy (takie jak `staging` czy `production`) są opcjonalnymi konwencjami specyficznymi dla projektu, które należy odpowiednio udokumentować i skonfigurować w narzędziach.
