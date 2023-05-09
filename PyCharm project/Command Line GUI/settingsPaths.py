import json


def getMacPath():
    file = open('paths.json')

    data = json.load(file)
    path = data["MacPath"]
    file.close()

    return path


def getUbuntuPath():
    file = open('paths.json')

    data = json.load(file)
    path = data["UbuntuPath"]
    file.close()

    return path


def getUbuntuHostname():
    file = open('paths.json')

    data = json.load(file)
    path = data["UbuntuHostname"]
    file.close()

    return path


def changeMacPath(newPath):
    file = open('paths.json', "r")
    json_object = json.load(file)
    file.close()

    json_object["MacPath"] = newPath

    file = open('paths.json', "w")
    json.dump(json_object, file)
    file.close()


def changeUbuntuPath(newPath):
    file = open('paths.json', "r")
    json_object = json.load(file)
    file.close()

    json_object["UbuntuPath"] = newPath

    file = open('paths.json', "w")
    json.dump(json_object, file)
    file.close()


def changeUbuntuHostname(newPath):
    file = open('paths.json', "r")
    json_object = json.load(file)
    file.close()

    json_object["UbuntuHostname"] = newPath

    file = open('paths.json', "w")
    json.dump(json_object, file)
    file.close()
