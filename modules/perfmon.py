# Python Performance Monitoring Module by William Castengera, v0.0
import time

def execStart():
    startTime = time.time()
    return startTime

def execStop():
    stopTime = time.time()
    return stopTime

def execTime(startTime, stopTime):
    return f"Execution Time: {startTime - stopTime} seconds.\n"

