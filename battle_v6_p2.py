
import random
import time
import platform
import subprocess
from time import sleep

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower()=="windows" else "clear"

    # Action
    return subprocess.call(command) == 0

def play2():
    """
    """    
