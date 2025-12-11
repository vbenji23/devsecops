# DevSecOps – Application de Gestion de Produits Sécurisée

Application GUI avec **pywebview** pour la gestion de produits destinée aux commerçants, intégrant la sécurité dès la conception (DevSecOps).

---

## 🚀 Fonctionnalités principales

### Les 7 Modules
| # | Module                       | Description                        | Priorité   |
|---|------------------------------|------------------------------------|------------|
| 1 | Gestion des Produits         | CRUD complet en CSV                | Haute      |
| 2 | Authentification Sécurisée   | Hachage SHA-256 + Salt             | Critique   |
| 3 | Vérification Mots de Passe   | Contrôle base compromis            | Critique   |
| 4 | Interface Graphique          | GUI pywebview                      | Haute      |
| 5 | Commandes & Statistiques     | Gestion + Visualisations           | Moyenne    |
| 6 | API REST                     | Endpoints via pywebview            | Moyenne    |
| 7 | Sécurité & Audit             | Bandit, Pylint, Safety             | Critique   |

---

## 📦 Installation

```bash
pip install pywebview
cd scripts
python main.py
