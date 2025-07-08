from utils import get_tx, get_tx_outputs, get_tx_inputs, analyze
from detector import analyze_transaction
import sys
import pprint

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <txid>")
        sys.exit(1)
    #analyze(sys.argv[1])
    pprint.pp(analyze_transaction(sys.argv[1]))
