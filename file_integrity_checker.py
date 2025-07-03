import os
import hashlib

def sha256sum(filename):
    h = hashlib.sha256()
    try:
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def main():
    folder = input("Enter folder path to check: ").strip()
    if not os.path.isdir(folder):
        print("Folder does not exist.")
        return

    print(f"\nSHA256 hashes for files in '{folder}':\n")
    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            print(f"{filepath}: {sha256sum(filepath)}")

if __name__ == "__main__":
    main()