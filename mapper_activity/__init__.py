# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(inputtext: tuple) -> list:
    words = inputtext[1].split()
    result = []
    for w in words:
        result.append((w, 1))
    return result

