import sys

def main():
    args = sys.argv[1:]  # Skip the script name
    if not args:
        print("none")
        return

    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")

if __name__ == "__main__":
    main()