from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from task import nameToTask, nameToRender
from commands import getEnabledCommands, getAllCommands
import sys
import view.settingsDialog as sd
import view.confirmationDialog as cd
import settingsPaths
import browserAutomation as browser


def update():
    os.execl(sys.executable, sys.executable, *sys.argv)


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("icon.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

# main task option list
for displayName in sorted(getEnabledCommands()):
    if displayName in nameToTask:
        action = nameToTask[displayName].action
        inst = nameToTask[displayName].inst
        inst.triggered.connect(action)
        menu.addAction(inst)

# sub adding task option list
menu.addSeparator()
addComamnds = QMenu("Edit Menu")
for displayName in sorted(getAllCommands()):
    renderAction = nameToRender[displayName].renderAction
    status = nameToRender[displayName].status
    inst = addComamnds.addAction(displayName)
    inst.setCheckable(True)
    inst.setChecked(status)
    addComamnds.addAction(inst)
    inst.triggered.connect(renderAction)
    inst.triggered.connect(update)
menu.addMenu(addComamnds)

# Browser Menu
browserMenu = QMenu("Browser Shortcuts")
browserOpen = browser.BrowserAutomation()
menu.addSeparator()

google = QAction("Google")
google.triggered.connect(lambda: browserOpen.open("https://www.google.com/"))
browserMenu.addAction(google)
menu.addMenu(browserMenu)

gmail = QAction("Gmail")
gmail.triggered.connect(lambda: browserOpen.open("https://accounts.google.com/"))
browserMenu.addAction(gmail)
menu.addMenu(browserMenu)

youtube = QAction("Youtube")
youtube.triggered.connect(lambda: browserOpen.open("https://www.youtube.com/"))
browserMenu.addAction(youtube)
menu.addMenu(browserMenu)

spotify = QAction("Spotify")
spotify.triggered.connect(lambda: browserOpen.open("https://open.spotify.com/"))
browserMenu.addAction(spotify)
menu.addMenu(browserMenu)

# Setting for default paths
menu.addSeparator()

settingDialog = QDialog()
ui = sd.Ui_settingDialog()
ui.setupUi(settingDialog)
ui.macPath.setText(settingsPaths.getMacPath())
ui.ubuntuPath.setText(settingsPaths.getUbuntuPath())
ui.ubuntuName.setText(settingsPaths.getUbuntuHostname())

confiramtionDialog = QDialog()
confUi = cd.Ui_confirmationDialog()
confUi.setupUi(confiramtionDialog)


def setSettings():
    modifiedMacPath = ui.macPath.text()
    settingsPaths.changeMacPath(modifiedMacPath)

    modifiedUbuntuPath = ui.ubuntuPath.text()
    settingsPaths.changeUbuntuPath(modifiedUbuntuPath)

    modifiedUbuntuName = ui.ubuntuName.text()
    settingsPaths.changeUbuntuHostname(modifiedUbuntuName)

    confiramtionDialog.exec_()


ui.buttonBox.accepted.connect(setSettings)


def loadSettings():
    settingDialog.exec_()


settings = QAction("Settings")
settings.triggered.connect(loadSettings)
menu.addAction(settings)

# adding quit option
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

sys.exit(app.exec_())
