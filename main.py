from detector import analyze_transaction
import sys
import pprint

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <txid>")
        sys.exit(1)
    pprint.pp(analyze_transaction(sys.argv[1]))
