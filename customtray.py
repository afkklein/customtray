import os
import subprocess
import time
import thread

from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def getMicIcon():
  try:
    subprocess.check_output("amixer get Capture | grep '\[off\]'", shell=True)
    return("microphone-sensitivity-muted-symbolic")
  except:
    return("audio-input-microphone-symbolic")

def reloadIcon(delay):
  while True:
    time.sleep(delay)
    indicator.set_icon(getMicIcon())

indicator = appindicator.Indicator.new("customtray", getMicIcon(), appindicator.IndicatorCategory.APPLICATION_STATUS)

def main():  
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  thread.start_new_thread(reloadIcon, (1, ))
  gtk.main()

def menu():
  menu = gtk.Menu()

  exit = gtk.MenuItem('Exit')
  exit.connect('activate', quit)
  menu.append(exit)
  
  menu.show_all()
  return menu

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()
