# Customtray app on Ubuntu

I basically followed the example posted on this link: https://fosspost.org/custom-system-tray-icon-indicator-linux/ and applied some changes to meet my needs.

### What does it do?

It shows an icon on your taskbar displaying the status of your microphone (on/off). 

As now I'm working from home I've been having issues on checking whether my headset's microphone is muted or not. So I decided to look up for some solutions to help me mute and unmute my microphone using a key combo.


We can config a key combo easily using the GUI by going to: **Configuration -> Devices -> Keyboard**, scrolling to the bottom and clicking on the **+**(add) button.

You can use the key combo you want. The command I used to toggle the mic on/off is:
```
amixer set Capture toggle
```

**The following steps were executed on Ubuntu 18.04** 

Before executing the app you need the following dependencies:

```
sudo apt-get install gir1.2-appindicator3 -y
```

```
sudo apt-get install python-gobject -y
```

**I know the code is not optimized, it was just an experiment! Feel free to fork it and improve it!**

After that all you have to do is run the customtray.tray
```
python customtray.py
```