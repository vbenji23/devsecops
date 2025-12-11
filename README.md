# DevSecOps – Application de Gestion de Produits Sécurisée

## 🎯 Objectif
Développer une application complète de gestion pour e-commerçants, intégrant la sécurité dès la conception (approche DevSecOps).  
Le projet combine apprentissage de Python, sécurité des applications et expérience utilisateur.

---

## 🔑 Concepts Clés

- **Hachage & Salage** : SHA-256 avec salt unique par utilisateur, protection contre les rainbow tables.
- **Vérification locale** : contrôle des mots de passe contre une base de credentials compromis (600M+).
- **Architecture modulaire** : séparation en couches (Présentation, Application, Données), principe du moindre privilège.

---

## 🏗️ Architecture Globale

┌───────────────────────────────┐ │ Couche Présentation (GUI) │ │ Tkinter / PyQt / pywebview │ └───────────────┬───────────────┘ │ ┌───────────────▼───────────────┐ │ Couche Application (Python) │ │ Produits • Auth • Commandes │ │ Statistiques • API • Audit │ └───────────────┬───────────────┘ │ ┌───────────────▼───────────────┐ │ Couche Données (CSV + Logs) │ │ Produits • Utilisateurs • │ │ Commandes • Sécurité │ └─────────────────────────────


---

## 📦 Modules à développer

| # | Module                     | Description                        | Priorité   |
|---|----------------------------|------------------------------------|------------|
| 1 | Gestion des Produits       | CRUD complet en CSV                | Haute      |
| 2 | Authentification Sécurisée | Hachage SHA-256 + Salt             | Critique   |
| 3 | Vérification Mots de Passe | Contrôle base compromis (API/local)| Critique   |
| 4 | Interface Graphique        | GUI Tkinter/PyQt/pywebview         | Haute      |
| 5 | Commandes & Statistiques   | Gestion + Visualisations           | Moyenne    |
| 6 | API REST                   | Endpoints Flask/FastAPI            | Moyenne    |
| 7 | Sécurité & Audit           | Bandit, Pylint, Safety             | Critique   |

---

## 📂 Structure du projetscripts/ 
├── main.py # Logique Python (modules) 
├── index.html # Interface graphique (pywebview) 
├── README.md # Documentation └── data/ # Créé automatiquement 
├── products.csv 
├── users.csv 
├── orders.csv 
├── security_logs.csv └── compromised_passwords.txt


---

## 🚀 Installation & Lancement

```bash
pip install pywebview flask matplotlib seaborn bandit pylint safety
cd scripts
python main.py

Compte par défaut : admin / admin123
API REST (exemple endpoints)
Méthode	Endpoint	Fonction
GET	/api/products	Liste des produits
POST	/api/products	Ajouter un produit (auth requise)
PUT	/api/products/:id	Modifier un produit
DELETE	/api/products/:id	Supprimer un produit
POST	/api/auth/login	Authentification (JWT)
GET	/api/orders	Liste des commandes
POST	/api/orders	Créer une commande
GET	/api/stats	Statistiques agrégées
🔒 Sécurité intégrée
SHA-256 + Salt : hachage robuste des mots de passe.

Comparaison temporelle constante : protection contre attaques timing.

Logs détaillés : traçabilité complète des accès.

Audit automatisé : Bandit, Pylint, Safety intégrés en CI/CD.

📌 Compétences acquises
Python : programmation modulaire, gestion CSV, tests unitaires.

Sécurité : hachage, salage, audit, gestion des secrets.

GUI : Tkinter/PyQt/pywebview, UX sécurisée.

API REST : endpoints Flask/FastAPI, JWT, documentation OpenAPI.

DevOps : CI/CD, logging, monitoring, audit automatisé.

📚 Ressources utiles
Documentation Python

API Pwned Passwords

PyQt5 Docs

Flask Framework

Bandit / Pylint / Safety

✅ Bonnes pratiques
Toujours saler les hash.

Jamais de secrets en dur dans le code.

Logger les accès et actions critiques.

Tests unitaires systématiques.

Code review en équipe.

Commits atomiques et clairs.

🎯 Conclusion
Ce projet est une application professionnelle DevSecOps : sécurité intégrée dès la conception, architecture modulaire, documentation complète. Il peut servir de portfolio ou de démo en entretien pour démontrer tes compétences en Python, sécurité et DevOps.



