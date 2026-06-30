# Contributing to CineMatch 🎬

First off — **thank you for taking the time to contribute!** 🙌
Every bug report, feature idea, documentation fix, or line of code makes this project better for everyone.

This document is the single source of truth for how to contribute. Please read it fully before opening an issue or submitting a pull request.

---

## 📌 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [I Just Have a Question](#-i-just-have-a-question)
- [How Can I Contribute?](#-how-can-i-contribute)
  - [Reporting Bugs](#-reporting-bugs)
  - [Suggesting Features](#-suggesting-features)
  - [Your First Code Contribution](#-your-first-code-contribution)
  - [Improving Documentation](#-improving-documentation)
- [Development Setup](#-development-setup)
- [Branching Strategy](#-branching-strategy)
- [Commit Message Convention](#-commit-message-convention)
- [Pull Request Process](#-pull-request-process)
- [Code Style Guide](#-code-style-guide)
- [Project Roadmap](#-project-roadmap)
- [Recognition](#-recognition)

---

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
By participating, you are expected to uphold this standard. Please report unacceptable behaviour to the maintainer at **your.email@example.com**.

In short: **be kind, be constructive, be inclusive.**

---

## ❓ I Just Have a Question

> **Please do not open a GitHub Issue for questions.**

Use one of these channels instead:

| Channel | Link |
|---|---|
| GitHub Discussions | [Start a Discussion](https://github.com/itxalmannkhann/cinematch-movie-recommender/discussions) |
| Email | khanhackersalman@gmail.com |

---

## 🤝 How Can I Contribute?

### 🐛 Reporting Bugs

Before submitting a bug report, please:

1. **Search existing issues** — someone may have already reported it.
2. **Confirm it is reproducible** — test on a fresh environment if possible.
3. **Check your API key** — many poster-fetch errors are TMDB API issues, not bugs.

When you open an issue, use the **Bug Report** template and include:

```
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behaviour:
1. Go to '...'
2. Select movie '...'
3. Click '...'
4. See error

**Expected behaviour**
What you expected to happen.

**Screenshots / Error logs**
Paste the full traceback from your terminal.

**Environment**
 - OS: [e.g. Windows 11 / Ubuntu 22.04]
 - Python version: [e.g. 3.10.6]
 - Streamlit version: [e.g. 1.32.0]
 - Browser: [e.g. Chrome 124]
```

---

### 💡 Suggesting Features

We love new ideas! Before submitting:

1. Check the [Project Roadmap](#-project-roadmap) — it might already be planned.
2. Search open issues for similar suggestions.

When opening a feature request, answer these questions:

```
**Is your feature request related to a problem?**
e.g. "I'm always frustrated when..."

**Describe the solution you'd like**
A clear and concise description of what you want.

**Describe alternatives you've considered**
Any alternative solutions or features you've thought about.

**Additional context**
Mockups, references, related papers, etc.
```

---

### 👩‍💻 Your First Code Contribution

Unsure where to start? Look for issues labelled:

| Label | Meaning |
|---|---|
| `good first issue` | Simple fixes, great for newcomers |
| `help wanted` | Maintainer is actively seeking help |
| `bug` | Confirmed bug needing a fix |
| `enhancement` | New feature or improvement |
| `documentation` | Docs-only change |

---

### 📝 Improving Documentation

Good documentation is as valuable as good code. You can help by:

- Fixing typos or grammar in `README.md` or `CONTRIBUTING.md`
- Adding docstrings to functions in `app.py` or the notebook
- Writing a clearer explanation of the ML pipeline
- Adding a `CHANGELOG.md` entry for your change
- Translating docs (open an issue first to coordinate)

---

## 🛠 Development Setup

### 1. Fork & Clone

```bash
# Fork via GitHub UI, then:
git clone https://github.com/itxsalmannkhann/cinematch-movie-recommender.git
cd cinematch-movie-recommender
```

### 2. Add the Upstream Remote

```bash
git remote add upstream https://github.com/your-itxalmannkhann/cinematch-movie-recommender.git
git fetch upstream
```

### 3. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt   # linting & testing tools
```

`requirements-dev.txt` should contain:

```
pytest
pytest-cov
black
flake8
isort
```

### 5. Set Up Your Environment Variables

```bash
cp .env.example .env
# Then edit .env and add your TMDB_API_KEY
```

### 6. Generate Model Files

Run the notebook end-to-end to produce `movie_list.pkl` and `similarity.pkl`, then place them in `model/`:

```bash
jupyter notebook notebook/notebook86c26b4f17.ipynb
mkdir -p model
mv movie_list.pkl similarity.pkl model/
```

### 7. Verify the App Runs

```bash
streamlit run app.py
```

Open `http://localhost:8501` — if you see the dropdown, you're ready to contribute. ✅

---

## 🌿 Branching Strategy

We follow a simplified **GitHub Flow**:

```
main (stable, always deployable)
  │
  ├── feature/tfidf-vectorizer
  ├── fix/poster-fetch-timeout
  ├── docs/update-installation-guide
  └── refactor/split-app-modules
```

| Branch prefix | When to use |
|---|---|
| `feature/` | New features or enhancements |
| `fix/` | Bug fixes |
| `docs/` | Documentation-only changes |
| `refactor/` | Code restructuring without behaviour change |
| `test/` | Adding or improving tests |
| `chore/` | Dependency updates, tooling, CI changes |

**Never push directly to `main`.** All changes go through a pull request.

```bash
# Always branch off the latest main
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name
```

---

## ✍️ Commit Message Convention

We follow the **Conventional Commits** specification. This keeps the Git history clean and enables automated changelog generation.

### Format

```
<type>(<scope>): <short summary>

[optional body]

[optional footer]
```

### Types

| Type | When to use |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `style` | Formatting, missing semicolons — no logic change |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Performance improvement |
| `test` | Adding or fixing tests |
| `chore` | Build process, dependency updates, CI changes |

### Examples

```bash
# ✅ Good
git commit -m "feat(recommender): add TF-IDF vectorizer as an alternative to CountVectorizer"
git commit -m "fix(api): handle missing poster_path with a fallback placeholder image"
git commit -m "docs(readme): add Streamlit Cloud deployment instructions"
git commit -m "refactor(app): extract fetch_poster into a separate utils module"
git commit -m "perf(model): cache similarity matrix using st.cache_data"

# ❌ Bad
git commit -m "fixed stuff"
git commit -m "update"
git commit -m "WIP"
```

### Breaking Changes

If your change breaks the existing API or interface, add `!` after the type and a `BREAKING CHANGE` footer:

```bash
git commit -m "feat(model)!: switch from pickle to joblib for model serialization

BREAKING CHANGE: existing .pkl files must be regenerated using joblib.dump()"
```

---

## 🔁 Pull Request Process

### Before You Open a PR

- [ ] Your branch is up-to-date with `upstream/main`
- [ ] The app runs without errors (`streamlit run app.py`)
- [ ] Your code follows the [style guide](#-code-style-guide)
- [ ] You have added or updated docstrings where relevant
- [ ] You have updated `README.md` if your change affects usage or setup
- [ ] You have added a `CHANGELOG.md` entry (see format below)

### Keeping Your Branch Updated

```bash
git fetch upstream
git rebase upstream/main
# Resolve any conflicts, then:
git push origin feature/your-feature-name --force-with-lease
```

### Opening the PR

1. Push your branch to your fork.
2. Open a Pull Request against `main` on the upstream repo.
3. Fill in the PR template completely — do not delete sections.
4. Link any related issues using keywords: `Closes #42`, `Fixes #17`.
5. Assign yourself and add relevant labels.
6. Request a review from a maintainer.

### PR Template

```markdown
## Summary
<!-- One paragraph explaining what this PR does and why. -->

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
<!-- Describe how you tested your changes. -->
- [ ] Ran `streamlit run app.py` and manually tested
- [ ] Ran `pytest` — all tests pass
- [ ] Tested on movie: _____________

## Screenshots (if applicable)
<!-- Before / After screenshots or a short GIF -->

## Checklist
- [ ] My code follows the project style guide
- [ ] I have added docstrings to new functions
- [ ] I have updated README.md where necessary
- [ ] I have added a CHANGELOG.md entry
```

### Review & Merge

- A PR requires **at least 1 approving review** before merging.
- Maintainers may request changes — please respond within **7 days** or the PR may be closed.
- Merges use **Squash and Merge** to keep the commit history clean.
- Delete your branch after the PR is merged.

---

## 🎨 Code Style Guide

### Python

We use **Black** for formatting, **isort** for import sorting, and **Flake8** for linting.

```bash
# Format code
black app.py

# Sort imports
isort app.py

# Lint
flake8 app.py --max-line-length=88
```

**Key conventions:**

```python
# ✅ Use descriptive function names with docstrings
def fetch_poster(movie_id: int) -> str:
    """
    Fetch the full poster URL for a given TMDB movie ID.

    Args:
        movie_id (int): The TMDB movie ID.

    Returns:
        str: Full URL of the movie poster image.

    Raises:
        KeyError: If 'poster_path' is missing from the TMDB response.
    """
    ...

# ✅ Use type hints
def recommend(movie: str) -> tuple[list[str], list[str]]:
    ...

# ✅ Use constants for magic values
TMDB_BASE_URL = "https://api.themoviedb.org/3/movie/{}"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500/"
NUM_RECOMMENDATIONS = 5

# ❌ Avoid hardcoded strings and magic numbers scattered through code
url = "https://api.themoviedb.org/3/movie/{}?api_key=abc123".format(movie_id)
for i in distances[1:6]:
    ...
```

### Jupyter Notebooks

- Keep cells small and focused — one logical step per cell.
- Add a Markdown cell before every major section explaining what it does.
- Clear all outputs before committing (`Kernel → Restart & Clear Output`).
- Use `#` comments inside code cells for inline explanation.

### Streamlit

- Use `st.cache_data` for data loading and `st.cache_resource` for models.
- Keep `app.py` as the UI layer only — move business logic to helper modules.
- Avoid `st.beta_columns` (deprecated); use `st.columns` instead.

---

## 🗺 Project Roadmap

Here's what's planned. Pick any of these up if you'd like to contribute a meaningful feature:

### v1.1 — Model Improvements
- [ ] Replace `CountVectorizer` with `TfidfVectorizer`
- [ ] Experiment with BERT / sentence-transformers for semantic similarity
- [ ] Add a hybrid recommender (content-based + collaborative filtering)

### v1.2 — UI Enhancements
- [ ] Add genre, year, and language filters
- [ ] Show movie rating, release year, and overview on hover
- [ ] Dark/light mode toggle
- [ ] Add a "Surprise Me" random movie button

### v1.3 — Performance & Reliability
- [ ] Cache TMDB API responses with `st.cache_data` + TTL
- [ ] Graceful fallback poster when TMDB returns no image
- [ ] Replace `pickle` with `joblib` for safer serialization
- [ ] Add error handling for network timeouts

### v2.0 — Deployment & Scale
- [ ] GitHub Actions CI pipeline (lint + test on every PR)
- [ ] Deploy to Streamlit Cloud with automated deployment on merge to `main`
- [ ] Dockerize the application
- [ ] Add a REST API layer using FastAPI

---

## 🏆 Recognition

All contributors are acknowledged in the project. Here's how we say thank you:

- Your name and GitHub profile will be added to the **Contributors** section of `README.md`.
- Significant contributions earn a shoutout in the `CHANGELOG.md` release notes.
- First-time contributors receive the `🌟 First Contribution` label on their merged PR.

---

## 📋 Changelog Format

When adding an entry to `CHANGELOG.md`, follow this format:

```markdown
## [Unreleased]

### Added
- TF-IDF vectorizer as an alternative to CountVectorizer (#12)

### Fixed
- Fallback poster shown when TMDB returns null poster_path (#8)

### Changed
- Switched from st.beta_columns to st.columns (#15)

### Removed
- Hardcoded API key replaced with environment variable (#10)
```

---

<div align="center">

**Thank you for making CineMatch better. Happy coding! 🚀**

*This document was inspired by best practices from [Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md), [Rails](https://github.com/rails/rails/blob/main/CONTRIBUTING.md), and the [Contributor Covenant](https://www.contributor-covenant.org/).*

</div>