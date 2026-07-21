<div align="center">

# 🚀 CI/CD Pipeline Demo

**Automated Testing & Deployment with GitHub Actions, Flask & Render**

[![CI/CD Pipeline](https://github.com/Parikshithurs>/CI-CD/actions/workflows/cicd.yml/badge.svg)](https://github.com/<Parikshithurs>/CI-CD/actions/workflows/cicd.yml)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A minimal yet production-ready CI/CD pipeline that automatically **tests** and **deploys** a Flask REST API every time code is pushed to `main`.

</div>

---

## 📋 Table of Contents

- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [API Endpoints](#-api-endpoints)
- [Getting Started](#-getting-started)
- [Pipeline Setup](#-pipeline-setup)
- [Running Tests](#-running-tests)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🏗 Architecture

```
Push to main / Open PR
        │
        ▼
┌──────────────────────────────┐
│     GitHub Actions Runner    │
│                              │
│  ┌────────────────────────┐  │
│  │   JOB 1 — Run Tests   │  │
│  │  • Checkout code       │  │
│  │  • Setup Python 3.11   │  │
│  │  • Install dependencies│  │
│  │  • Run pytest suite    │  │
│  └──────────┬─────────────┘  │
│             │ ✅ Pass        │
│  ┌──────────▼─────────────┐  │
│  │  JOB 2 — Deploy       │  │
│  │  • Trigger Render hook │  │
│  │  (main branch only)    │  │
│  └────────────────────────┘  │
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│   Render.com — Live App 🌐  │
└──────────────────────────────┘
```

---

## 🛠 Tech Stack

| Layer          | Technology                          |
| -------------- | ----------------------------------- |
| **Language**   | Python 3.11                         |
| **Framework**  | Flask 3.0                           |
| **Testing**    | pytest 7.4                          |
| **CI/CD**      | GitHub Actions                      |
| **Hosting**    | Render                              |
| **IaC**        | `render.yaml` (Infrastructure as Code) |

---

## 📡 API Endpoints

| Method | Endpoint             | Description                | Example Response                          |
| ------ | -------------------- | -------------------------- | ----------------------------------------- |
| `GET`  | `/`                  | Welcome message            | `{"message": "Welcome to...", "status": "running"}` |
| `GET`  | `/health`            | Health check               | `{"status": "ok"}`                        |
| `GET`  | `/add/<int>/<int>`   | Add two numbers            | `/add/3/4` → `{"result": 7}`             |
| `GET`  | `/reverse/<string>`  | Reverse a string           | `/reverse/hello` → `{"result": "olleh"}` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip

### Local Development

```bash
# Clone the repository
git clone https://github.com/<your-username>/CI-CD.git
cd CI-CD

# Install dependencies
pip install -r requirements.txt

# Run the application
python app/main.py
```

The API will be available at `http://localhost:5000`.

---

## ⚙ Pipeline Setup

To enable the full CI/CD pipeline, follow these steps:

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/CI-CD.git
git push -u origin main
```

### 2. Configure Render

1. Create a new **Web Service** on [Render](https://render.com)
2. Connect your GitHub repository
3. Render will auto-detect `render.yaml` for build & start commands

### 3. Add Deploy Hook

1. In Render Dashboard → **Settings** → **Deploy Hook** → Copy the URL
2. In GitHub → **Settings** → **Secrets and variables** → **Actions**
3. Create a new secret:
   - **Name:** `RENDER_DEPLOY_HOOK_URL`
   - **Value:** *(paste the Render Deploy Hook URL)*

### 4. Done! 🎉

Every push to `main` will now:
1. Run the full test suite
2. If all tests pass, automatically deploy to Render

---

## 🧪 Running Tests

```bash
# Run all tests with verbose output
pytest tests/ -v
```

**Test coverage includes:**

| Test                       | Validates                              |
| -------------------------- | -------------------------------------- |
| `test_home`                | Home endpoint returns status "running" |
| `test_health_check`        | Health endpoint returns status "ok"    |
| `test_add_two_numbers`     | Addition logic (3 + 4 = 7)            |
| `test_add_negative_numbers`| Negative number handling (-2 + 5 = 3)  |
| `test_reverse_string`      | String reversal ("hello" → "olleh")    |
| `test_reverse_single_char` | Edge case: single character            |

---

## 📁 Project Structure

```
CI-CD/
├── .github/
│   └── workflows/
│       └── cicd.yml          # GitHub Actions pipeline definition
├── app/
│   └── main.py               # Flask application & API routes
├── tests/
│   └── test_app.py           # pytest test suite
├── render.yaml                # Render deployment configuration
├── requirements.txt           # Python dependencies
└── README.md
```

---

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

The CI pipeline will automatically run tests against your PR.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

</div>