import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="My Awesome Package CLI")
    parser.add_argument("--name", type=str, default="World", help="Name to greet")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    print(f"Running on Python {sys.version}")

if __name__ == "__main__":
    main()
