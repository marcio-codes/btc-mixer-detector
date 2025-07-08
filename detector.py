from utils import get_tx_inputs, get_tx_outputs
from heuristics import (
    score_equal_outputs,
    score_many_inputs,
    score_many_outputs,
    score_unique_output_addresses,
)

def analyze_transaction(txid, verbose=False):
    inputs = get_tx_inputs(txid)
    outputs = get_tx_outputs(txid)

    scores = {
        "many_inputs": score_many_inputs(inputs),
        "many_outputs": score_many_outputs(outputs),
        "equal_outputs": score_equal_outputs(outputs),
        "unique_output_addresses": score_unique_output_addresses(outputs),
    }

    total_score = sum(scores.values())

    if verbose:
        print(f"Analysis for TXID: {txid}")
        for k, v in scores.items():
            print(f"  {k}: {v}")
        print(f"  → Total Heuristic Score: {total_score}/6")

    return {
        "txid": txid,
        "score": total_score,
        "details": scores,
        "classification": classify_score(total_score)
    }

def classify_score(score):
    if score >= 5:
        return "🟢 Likely CoinJoin or Mixer"
    elif score >= 3:
        return "🟡 Possibly a Mixer"
    else:
        return "🔴 Unlikely to be a Mixer"
