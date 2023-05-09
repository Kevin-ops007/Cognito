import iterm2
import time
from commands import getCommands


async def stash(connection):
   app = await iterm2.async_get_app(connection)
   window = app.current_terminal_window


   commands = getCommands("git stash")
   if window is not None:
       tab = window.current_tab
       session = tab.current_session
       for command in commands:
           await session.async_send_text(command)
   else:
       print("No current window")




async def stashApply(connection):
   app = await iterm2.async_get_app(connection)
   window = app.current_terminal_window


   commands = getCommands("git stash apply")
   if window is not None:
       tab = window.current_tab
       session = tab.current_session
       for command in commands:
           await session.async_send_text(command)
   else:
       print("No current window")




async def stashDrop(connection):
   app = await iterm2.async_get_app(connection)
   window = app.current_terminal_window


   commands = getCommands("git stash drop")
   if window is not None:
       tab = window.current_tab
       session = tab.current_session
       for command in commands:
           await session.async_send_text(command)
   else:
       print("No current window")