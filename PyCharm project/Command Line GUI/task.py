import scriptFunctions as sf
from PyQt5.QtWidgets import *
import json
from commands import configCommands

class Task:
    def __init__(self, action, inst):
          self.action = action
          self.inst = inst

class Render:
    def __init__(self, renderAction, status):
          self.renderAction = renderAction
          self.status = status

def getNameToTask():
    nameToTask = {}
    file = open('config.json')

    data = json.load(file)
    taskObjs = data["commands"]
    for obj in taskObjs:
        nameToTask[obj["name"]] = Task(eval(obj["action"]), eval(obj["inst"]))
    file.close()
    return nameToTask

def getNameToRender():
    nameToRender = {}
    file = open('config.json')

    data = json.load(file)
    renderObjs = data["commands"]
    for obj in renderObjs:
        nameToRender[obj["name"]] = Render(eval(obj["renderAction"]), eval(obj["status"]))
    file.close()
    return nameToRender

nameToTask = getNameToTask()
nameToRender = getNameToRender()
