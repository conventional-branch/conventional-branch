---
draft: false
aliases: ["/pl/"]
layout: single
seoTitle: "Konwencja nazewnictwa gałęzi Git — Conventional Branch"
seoDescription: "Specyfikacja nazw gałęzi Git: prefiksy feature/, bugfix/, hotfix/, release/ i chore/, formalna gramatyka oraz sposób jej egzekwowania w GitHub i GitLab."
---

# Conventional Branch 1.2.0

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

**Prefiksy celu** — opisują intencję pracy:
- **`feature/`** (lub **`feat/`**): Dla nowych funkcji (np. `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (lub **`fix/`**): Dla poprawek błędów (np. `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`**: Dla pilnych poprawek (np. `hotfix/security-patch`)
- **`release/`**: Dla gałęzi przygotowujących wydanie (np. `release/v1.2.0`)
- **`chore/`**: Dla zadań niezwiązanych z kodem, takich jak zależności, aktualizacje dokumentacji (np. `chore/update-dependencies`)

**Prefiksy źródła agenta AI** — identyfikują gałęzie generowane przez agentów kodujących AI:
{{< agents >}}

Ta lista jest zamknięta: agent bez własnego prefiksu używa `ai/`.

Gałęzie główne (`main`, `master`, `develop`) nie używają prefiksu.

---

### Podstawowe zasady

1. **Używaj małych liter, cyfr, myślników i kropek**: Zawsze używaj małych liter (`a-z`), cyfr (`0-9`) i myślników (`-`) do oddzielania słów. Unikaj znaków specjalnych, podkreśleń lub spacji. Kropki (`.`) są dozwolone w każdym opisie, zwykle w numerach wersji (np. `release/v1.2.0`, `chore/upgrade-node-v20.11`). Jedynym wyjątkiem od małych liter jest klucz zgłoszenia na początku opisu (zob. zasada 4).
2. **Bez następujących po sobie, wiodących lub końcowych myślników lub kropek**: Upewnij się, że myślniki i kropki nie pojawiają się kolejno po sobie (np. `feature/new--login`, `release/v1.-2.0`), ani na początku czy końcu opisu (np. `feature/-new-login`, `release/v1.2.0.`).
3. **Zachowaj jasność i zwięzłość**: Nazwa gałęzi powinna być opisowa, ale zwięzła, jasno wskazująca cel pracy.
4. **Dołącz numery biletów**: Jeśli to możliwe, dołącz numer biletu z narzędzia zarządzania projektami, aby ułatwić śledzenie. Na przykład, dla biletu `issue-123`, nazwa gałęzi mogłaby być `feature/issue-123-new-login`. Klucz zgłoszenia na początku opisu może zachować wielkie litery z narzędzia do śledzenia zgłoszeń, np. `feature/PROJ-123-new-login`; reszta opisu pozostaje pisana małymi literami.


### Formalna gramatyka

Poniższa gramatyka ABNF (Augmented Backus-Naur Form) formalnie definiuje prawidłowe nazwy gałęzi:

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
                / "ai" / "copilot" / "cursor"
                / "claude" / "codex"
description     = (ticket-key / desc-segment) *("-" desc-segment)
ticket-key      = UPPER *(UPPER / DIGIT) "-" 1*DIGIT
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A   ; małe litery a-z
UPPER           = %x41-5A   ; wielkie litery A-Z, tylko w kluczu zgłoszenia
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
| `chore/upgrade-node-v20.11` | ✅ | Kropki poza gałęzią wydania |
| `chore/update-dependencies` | ✅ | Zadanie niezwiązane z kodem |
| `feature/issue-123-new-login` | ✅ | Funkcja z numerem biletu |
| `feature/PROJ-123-new-login` | ✅ | Klucz zgłoszenia wielkimi literami na początku |
| `release/PROJ-1234` | ✅ | Opis składający się tylko z klucza zgłoszenia |
| `Feature/Add-Login` | ❌ | Wielkie litery są niedozwolone |
| `feature/new-login-PROJ-123` | ❌ | Klucz zgłoszenia musi otwierać opis |
| `feature/Proj-123-new-login` | ❌ | Klucz zgłoszenia musi być pisany wielkimi literami |
| `feature/new--login` | ❌ | Kolejne myślniki są niedozwolone |
| `feature/-new-login` | ❌ | Opis nie może zaczynać się myślnikiem |
| `feature/new-login-` | ❌ | Opis nie może kończyć się myślnikiem |
| `release/v1.-2.0` | ❌ | Myślnik obok kropki jest niedozwolony |
| `fix/header bug` | ❌ | Spacje są niedozwolone |
| `fix/header_bug` | ❌ | Podkreślenia są niedozwolone |
| `ai/refactor-auth-flow` | ✅ | Generyczny prefiks agenta AI |
| `copilot/add-login-page` | ✅ | GitHub Copilot |
| `cursor/fix-header-bug` | ✅ | Cursor |
| `claude/security-patch` | ✅ | Claude Code od Anthropic |
| `codex/optimize-query` | ✅ | OpenAI Codex |
| `unknown/some-task` | ❌ | Nieznany typ prefiksu |

## Wnioski

- **Jasna komunikacja**: Sama nazwa gałęzi zapewnia jasne zrozumienie jej celu i zmiany kodu.
- **Przyjazna dla automatyzacji**: Łatwo integruje się z procesami automatyzacji (np. różne przepływy pracy dla `feature`, `release`, itp.).
- **Skalowalność**: Dobrze sprawdza się w dużych zespołach, gdzie wielu programistów pracuje jednocześnie nad różnymi zadaniami.

Podsumowując, conventional branch został zaprojektowany w celu poprawy organizacji projektu, komunikacji i automatyzacji w przepływach pracy Git.

## Narzędzia

{{< tooling compact >}}

## FAQ

### Jak Conventional Branch ma się do Conventional Commits?

Conventional Branch jest zainspirowany przez [Conventional Commits](https://www.conventionalcommits.org) i podąża za podobną filozofią: wprowadzenie struktury czytelnej dla ludzi i maszyn do metadanych Git. Podczas gdy Conventional Commits standaryzuje wiadomości commitów, Conventional Branch standaryzuje nazwy gałęzi. Obie specyfikacje naturalnie się uzupełniają.

### Czy Conventional Branch wymyśliło te prefiksy?

Nie. Prefiksy takie jak `feature/`, `hotfix/` i `release/` spopularyzowało około 2010 roku narzędzie [git-flow](https://github.com/nvie/gitflow); są też domyślne w narzędziach takich jak [model gałęzi Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-a-projects-branching-model/). Conventional Branch opiera się na tej praktyce, zamiast ją zastępować. Dodaje precyzyjną definicję, którą mogą współdzielić ludzie i narzędzia: stały zestaw typów, formalną gramatykę, wyrażenie regularne do walidacji opublikowane w [`spec.json`](/spec.json) oraz przypadki zgodności, dzięki czemu każdy walidator akceptuje dokładnie te same nazwy.

### Dlaczego typy gałęzi nie są tak szczegółowe jak w Conventional Commits (np. `build`, `ci`, `docs`, `style`, `refactor`)?

Gałęzie różnią się od commitów — są tymczasowe i używane głównie do momentu scalenia. Wprowadzenie zbyt wielu typów dla gałęzi byłoby niepotrzebne i utrudniłoby ich zarządzanie oraz zapamiętywanie.

### Czy mogę zdefiniować własne typy gałęzi poza wymienionymi?

Tak, jako rozszerzenie na poziomie zespołu. Typy w gramatyce to te, które akceptuje każde zgodne narzędzie, dlatego gałąź taka jak `unknown/some-task` jest nieprawidłowa według samej specyfikacji. Zespół, który potrzebuje dodatkowych typów (np. `experiment/`), powinien jawnie dodać je do swojego walidatora (na przykład w `allow_branch_types` w [commit-check](/enforce/#commit-check)) i opisać je w dokumentacji, aby członkowie zespołu i zautomatyzowane narzędzia działali zgodnie. Na przykład repozytorium samej specyfikacji dodaje w swojej [konfiguracji commit-check](https://github.com/conventional-branch/conventional-branch/blob/main/commit-check.toml) typ `dependabot/` dla gałęzi tworzonych przez Dependabot.

### Dlaczego nazwy gałęzi muszą być pisane małymi literami?

Z dwóch powodów. Po pierwsze, Git zwykle przechowuje referencje gałęzi jako pliki w `.git/refs/heads/`, a domyślne systemy plików macOS i Windows nie rozróżniają wielkości liter: `Feature/login` i `feature/login` wskazują tam tę samą ścieżkę, a w Linuksie są dwiema różnymi gałęziami. Repozytorium, które dopuszcza obie formy, może więc zachowywać się różnie w zależności od klonu. Po drugie, jedna pisownia jest łatwiejsza do wpisania, wyszukania i dopasowania: narzędzie uruchamiane dla `release/*` nie musi uwzględniać także `Release/*`.

Od wersji v1.2.0 obowiązuje jeden wyjątek: klucz zgłoszenia na początku opisu, taki jak `PROJ-123`, może zachować wielkie litery, które wyświetlają narzędzia takie jak Jira. Zapisuj każdy klucz dokładnie tak, jak pokazuje go narzędzie, aby `PROJ-123` i `proj-123` nigdy nie nazywały gałęzi w tym samym repozytorium.

### Jakie są główne różnice między v1.2.0 a v1.1.0?

Wersja v1.2.0 pozwala, by opis zaczynał się od klucza zgłoszenia pisanego wielkimi literami, np. `feature/PROJ-123-new-login`, czego v1.1.0 nie akceptowała. Zamyka też listę prefiksów źródła agenta AI: nie będą dodawane kolejne prefiksy dostawców, a agent spoza tej piątki używa `ai/`. Każda nazwa gałęzi poprawna w v1.1.0 pozostaje poprawna — brak zmian łamiących zgodność.

### Jakie są główne różnice między v1.1.0 a v1.0.0?

v1.1.0 dodaje **Prefiksy źródła agenta AI** jako główną nową funkcję (dlaczego je wprowadzono, wyjaśnia następne pytanie w FAQ). Oferuje również witrynę z wersjonowaniem z przełącznikiem wersji, umożliwiającym użytkownikom przeglądanie specyfikacji v1.0.0 i v1.1.0. Wszystkie istniejące nazwy gałęzi v1.0.0 pozostają w pełni ważne — bez zmian łamiących zgodność.

### Dlaczego dodać prefiksy źródła agenta AI?

Agenci kodujący AI (GitHub Copilot, Cursor, Claude Code, OpenAI Codex itp.) są coraz częściej używani do generowania kodu i tworzenia pull requestów. Każdy agent używa własnego prefiksu gałęzi (np. `copilot/`, `cursor/`). Poprzez standaryzację tych prefiksów w specyfikacji Conventional Branch, umożliwiamy:
1. **Szybką identyfikację** — recenzenci i narzędzia mogą natychmiast rozpoznać PRy generowane przez AI
2. **Walidację narzędziową** — narzędzia takie jak commit-check mogą walidować gałęzie agentów AI względem specyfikacji
3. **Stała lista** — pięć prefiksów jest ustalonych od v1.2.0, a każdy inny agent używa `ai/`, więc gramatyka nie zmienia się przy każdym nowym narzędziu

Generyczny prefiks `ai/` jest dostępny dla każdego agenta AI bez dedykowanego prefiksu lub dla zespołów, które preferują neutralnego dostawcę. To kluczowa nowa funkcja wydana w **v1.1.0** — pełne podsumowanie zmian między wersjami znajduje się w powyższym pytaniu FAQ.

### Jak radzić sobie z długo żyjącymi gałęziami, takimi jak `develop` lub `staging`?

Długo żyjące gałęzie integracyjne lub środowiskowe (np. `develop`, `staging`, `production`) są w praktyce często traktowane jak gałęzie główne i nie wymagają prefiksu, o ile w danym projekcie zostanie to jasno ustalone. Formalna gramatyka ABNF definiuje jednak gałąź główną (`trunk-branch`) jedynie jako `main`, `master` lub `develop`, a dodatkowe nazwy (takie jak `staging` czy `production`) są opcjonalnymi konwencjami specyficznymi dla projektu, które należy odpowiednio udokumentować i skonfigurować w narzędziach.

### Jakich narzędzi można użyć, aby automatycznie sprawdzić, czy członek zespołu nie spełnia tej specyfikacji?

Możesz użyć [commit-check](https://github.com/commit-check/commit-check) do sprawdzania specyfikacji gałęzi lub [commit-check-action](https://github.com/commit-check/commit-check-action), jeśli twój kod jest hostowany na GitHub.
