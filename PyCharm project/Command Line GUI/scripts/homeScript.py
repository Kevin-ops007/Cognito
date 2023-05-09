import iterm2
import time
from commands import getCommands

# Open new terminal and run cd ~
async def openNewHome(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window

    commands = getCommands("cd home")
    if window is not None:
        tab = await window.async_create_tab()
        session = tab.current_session
        time.sleep(1)
        for command in commands:
            await session.async_send_text(command)
    else:
        print("No current window")

# Select the current terminal and run cd ~
async def cdHome(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window

    commands = getCommands("open home")
    if window is not None:
        tab = window.current_tab
        session = tab.current_session
        for command in commands:
            await session.async_send_text(command)
    else:
        print("No current window")
