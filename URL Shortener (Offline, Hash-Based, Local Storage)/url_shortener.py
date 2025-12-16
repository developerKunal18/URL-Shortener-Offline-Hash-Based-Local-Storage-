import hashlib
import json
import os
import string

DB_FILE = "urls.json"
BASE62 = string.ascii_letters + string.digits

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)

def base62_encode(num):
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        num, rem = divmod(num, base)
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)

def shorten_url(long_url, db):
    h = hashlib.sha256(long_url.encode()).hexdigest()
    num = int(h[:10], 16)
    code = base62_encode(num)[:6]

    db[code] = long_url
    save_db(db)
    return code

def expand_url(code, db):
    return db.get(code)

def main():
    print("🌐 Offline URL Shortener\n")
    db = load_db()

    while True:
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            url = input("Enter long URL: ").strip()
            code = shorten_url(url, db)
            print(f"\n🔗 Short URL code: {code}\n")

        elif choice == "2":
            code = input("Enter short code: ").strip()
            url = expand_url(code, db)
            if url:
                print(f"\n➡️ Original URL: {url}\n")
            else:
                print("\n❌ Code not found.\n")

        elif choice == "3":
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid option.\n")

if __name__ == "__main__":
    main()
