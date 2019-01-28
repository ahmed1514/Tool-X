# Tool Name :- Tool Ahmed
# Author :- Ahmed Alqhoom
# Date :- 28/4/2018
# Powered By :- Ahmed Alqhoom

import sys
import os
from modules.logo import exit
from modules.menu import ToolX

class chk(object):
  def chos(self):
    if "linux" in sys.platform:
      # Running Tool-X on linux ....
      pass
    elif "darwin" in sys.platform:
      pass
      # print("Sorry, its not available for mac right now...")
      ex()
    elif "win" in sys.platform:
      print("Sorry, its not available for windows right now...")
      ex()
    else:
      print("If Tool-X not support for \'%s\' right now !!!" %sys.platform)

def Tool_X():
  try:
	chk().chos()
	ToolX()

  except KeyboardInterrupt:
	exit()
Tool_X()
