# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(inputtext: list) -> dict:
    result = {}

    for word_position in inputtext:

        (word, position) = word_position
        positions = result.get(word)

        if positions is None:
            positions = [position]
        else:
            positions.append(position)
        result[word] = positions

    return result
