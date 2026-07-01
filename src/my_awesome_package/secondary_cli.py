import sys
import argparse

def main2():
    parser = argparse.ArgumentParser(description="My Awesome Package Secondary CLI")
    parser.add_argument("--name", type=str, default="Universe", help="Name to greet")
    args = parser.parse_args()

    print(f"Hello again, {args.name}!")
    print(f"Running on Python {sys.version}")

if __name__ == "__main__":
    main2()
