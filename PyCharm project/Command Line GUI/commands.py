import json
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def getCommandsObject():
   file = open('config.json')


   data = json.load(file)
   commandObjs = data["commands"]
   file.close()


   return commandObjs


def getEnabledCommands():
   commandObjs = getCommandsObject()
   enabledCommands = set()
   for obj in commandObjs:
       # True if selected from the list
       if(eval(obj["status"])):
           enabledCommands.add(obj["name"])
   return enabledCommands


def getAllCommands():
   commandObjs = getCommandsObject()
   commands = set()
   for obj in commandObjs:
       commands.add(obj["name"])
   return commands


def getCommands(displayName):
   commandObjs = getCommandsObject()
   commandText = ""
   commands = list()
   for obj in commandObjs:
       if(obj["name"] == displayName):
           commandText = obj["command"]
           break
   commands = commandText.split(";")
   return commands


def configCommands(name):
   print(name)
   a_file = open("config.json", "r")
   json_object = json.load(a_file)
   a_file.close()


   commandObjs = json_object["commands"]
   for obj in commandObjs:
       if obj["name"] == name:
           obj["status"] = str(not eval(obj["status"]))
           break
   a_file = open("config.json", "w")
   json.dump(json_object, a_file)
