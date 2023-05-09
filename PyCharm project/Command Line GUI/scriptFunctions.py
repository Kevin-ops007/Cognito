import iterm2
import scripts.pwdScript as pwd
import scripts.homeScript as home
import scripts.stashScript as stash
import scripts.lsScript as ls
import scripts.logScript as log


modes = [iterm2.PromptMonitor.Mode.PROMPT,
                iterm2.PromptMonitor.Mode.COMMAND_START,
                iterm2.PromptMonitor.Mode.COMMAND_END]


def runpwd():
   iterm2.run_until_complete(pwd.pwd, True)


def runcdHome():
   iterm2.run_until_complete(home.cdHome, True)


def runcdNewHome():
   iterm2.run_until_complete(home.openNewHome, True)


def runstash():
   iterm2.run_until_complete(stash.stash, True)


def runstashApply():
   iterm2.run_until_complete(stash.stashApply, True)


def runstashDrop():
   iterm2.run_until_complete(stash.stashDrop, True)


def runls():
   iterm2.run_until_complete(ls.ls, True)


def runlsla():
   iterm2.run_until_complete(ls.lsla, True)


def runlog():
   iterm2.run_until_complete(log.log, True)


def runreflog():
   iterm2.run_until_complete(log.reflog, True)