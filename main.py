import os, csv, hashlib, hmac, secrets
import webview

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
PRODUCTS_FILE = os.path.join(DATA_DIR, "products.csv")
USERS_FILE = os.path.join(DATA_DIR, "users.csv")

def init_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id","nom","description","prix","quantite","categorie"])
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username","salt","hash"])
        register_user("admin","admin123")

def hash_password(password, salt):
    return hashlib.sha256(salt + password.encode()).digest()

def register_user(username, password):
    salt = secrets.token_bytes(16)
    pwd_hash = hash_password(password, salt)
    with open(USERS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, salt.hex(), pwd_hash.hex()])

def login(username, password):
    with open(USERS_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username:
                salt = bytes.fromhex(row["salt"])
                expected = row["hash"]
                attempt = hash_password(password, salt).hex()
                return hmac.compare_digest(expected, attempt)
    return False

class Api:
    def get_products(self):
        with open(PRODUCTS_FILE, "r", newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def add_product(self, nom, description, prix, quantite, categorie):
        produits = self.get_products()
        new_id = str(1 + max([int(p["id"]) for p in produits], default=0))
        with open(PRODUCTS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([new_id, nom, description, prix, quantite, categorie])
        return {"ok": True, "id": new_id}

    def login(self, username, password):
        return {"ok": login(username, password)}

    def register(self, username, password):
        register_user(username, password)
        return {"ok": True}

def start():
    init_files()
    api = Api()
    window = webview.create_window("DevSecOps – Accueil", os.path.join(os.path.dirname(__file__), "index.html"), js_api=api)
    webview.start()

if __name__ == "__main__":
    start()
