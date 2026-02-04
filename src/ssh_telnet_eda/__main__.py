import argparse
import sys
import tomllib

def main():
    parser = argparse.ArgumentParser(description="ssh-telnet-eda proxy")
    parser.add_argument("--config", default="/etc/ssh-telnet-eda/config.toml")
    args = parser.parse_args()

    try:
        with open(args.config, "rb") as f:
            config = tomllib.load(f)
    except Exception as e:
        print(f"Error loading config: {e}", file=sys.stderr)
        sys.exit(1)

    print("ssh-telnet-eda started")
    print(f"Config loaded from {args.config}")
    print("Telnet target:", config.get("telnet", {}))

if __name__ == "__main__":
    main()
