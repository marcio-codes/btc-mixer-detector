def score_equal_outputs(outputs):
    values = [o['value'] for o in outputs]
    most_common = max(set(values), key=values.count)
    count = values.count(most_common)
    if count >= 3:
        return 3
    return 0

def score_many_inputs(inputs):
    return 1 if len(inputs) >= 5 else 0

def score_many_outputs(outputs):
    return 1 if len(outputs) >= 5 else 0

def score_unique_output_addresses(outputs):
    addresses = [o['scriptpubkey_address'] for o in outputs if 'scriptpubkey_address' in o]
    if len(addresses) == len(set(addresses)):
        return 1
    return 0

def score_total(inputs, outputs):
    return (
        score_many_inputs(inputs) +
        score_many_outputs(outputs) +
        score_equal_outputs(outputs) +
        score_unique_output_addresses(outputs)
    )
