import iterm2
import time
from commands import getCommands


async def ls(connection):
   app = await iterm2.async_get_app(connection)
   window = app.current_terminal_window


   commands = getCommands("ls")
   if window is not None:
       tab = window.current_tab
       session = tab.current_session
       time.sleep(1)
       for command in commands:
           await session.async_send_text(command)
   else:
       print("No current window")


async def lsla(connection):
   app = await iterm2.async_get_app(connection)
   window = app.current_terminal_window


   commands = getCommands("ls -la")
   if window is not None:
       tab = window.current_tab
       session = tab.current_session
       for command in commands:
           await session.async_send_text(command)
   else:
       print("No current window")