# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
from unittest import result

import azure.functions as func
import azure.durable_functions as df

# import functools
from functools import reduce


""" def orchestrator_function(context: df.DurableOrchestrationContext):
    result1 = yield context.call_activity('Hello', "Tokyo")
    result2 = yield context.call_activity('Hello', "Seattle")
    result3 = yield context.call_activity('Hello', "London")
    return [result1, result2, result3]

main = df.Orchestrator.create(orchestrator_function) """

def orchestrator_function(context: df.DurableOrchestrationContext):
    #get data with GetInputDataFN
    get_data = yield context.call_activity('GetInputDataFn', "mapreducecontainer")
    #return get_data

    tasks = []
    for file in get_data:
        tasks.append(context.call_activity("mapper_activity", file))
    results = yield context.task_all(tasks)
    result1 = reduce(lambda z, y :z + y, results)
    result2 = yield context.call_activity('shuffler_activity', result1)

    result3 = []
    for w in result2:
        intermediate_result = yield context.call_activity('reducer_activity', (w, result2[w]))
        result3.append(intermediate_result)

    return result3




    

   


  

"""     result1 = yield context.call_activity('mapper_activity', tuple([1,"Hello my name is Anastasia . The name is greek . Anastasia means something good"]))
    result2 = yield context.call_activity('shuffler_activity', result1)
    #result3 = yield context.call_activity('reducer_activity', tuple(["Anastasia",[1,1]]))
    result3 = []
    for w in result2:
        intermediate_result = yield context.call_activity('reducer_activity', (w, result2[w]))
        result3.append(intermediate_result) """
    

main = df.Orchestrator.create(orchestrator_function)