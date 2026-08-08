import sys

def main():
    # Yahan se 'f' hata diya hai taaki CLI jab isko replace kare toh ye normal string ban jaye
    print("Hello, World! Welcome to {project_name}.")

    # Ye theek hai kyunki sys.version evaluate hona chahiye
    print(f"Python Version: {sys.version.split()[0]}")

if __name__ == "__main__":
    main()
