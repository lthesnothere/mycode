#!/usr/bin/env python3

"""
Date:  06 Oct 2021
Auth:  T. Hesmer
Vers:  1.0

Program to backup work from /mycode/ directory
to my GitHub backup.

    cd ~/mycode
    git add *
    git commit -m "Learning to troubleshoot"
    git push origin

"""

# Modules <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import getopt        # C-style parser for command line options.
import os            # Operating system dependent functionality.
import sys           # System-specific parameters and functions.
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def scan_for_arguments():
  argumentList = sys.argv[1:]
  options      = "v" 
  long_options = ["version"]
  version      = '1.0'
  try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
      if currentArgument in ("-v", "--version"):
        print (os.path.basename(sys.argv[0]), version)
  except:
    print("Error 101")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def run_git_commands():
#  os.system("cd ~/mycode")
  commit_message=input('Commit comment: ')
  os.chdir("/home/student/mycode")
  os.system('touch lth_ghbackup.txt')
  os.system('git add *') 
#  os.system('git commit -m \"studying for logic\"')
  os.system("git commit -m '"+ commit_message +"'")
  os.system('git push origin') 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def main():
  scan_for_arguments()
  run_git_commands()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    main()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

