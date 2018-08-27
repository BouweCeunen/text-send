# Textsend - Send text messages through your phone with UDP messages (UNMAINTAINED)

Textsend will allow you to send text messages directly from received UDP broadcasted messages. This can be used if you keep your wifi on and want to send text messages from you phone. It uses the Textsend app along with a UDP broadcast script to run on your computer. The Android application receives the broadcasted UDP messages in your network over a specific port which in turn will be sent to given number(s). 

Make sure to check Textcast (https://play.google.com/store/apps/details?id=com.bouweceunen.textcast) to display text messages on your computer in that way you wont need to touch your phone to send and receive text messages! 

Feel free to let me know if something isn't working as it should at bouwe.ceunen@gmail.com

### Things to consider
- Your phone and computer must be connected to the same network through wifi or ethernet when your text message arrives.
- Make sure there are no firewall restrictions on outgoing UDP messages.

### Get it running (macOS, Windows, Linux)

Run this command in your terminal of choice to send text messages to a specified recipient.
```sh
$ python broadcast.py -port 7011 -recipient name -message custom message
```

If you want to send messages to the registered numbers in the Textsend app leave the -recipient blank.
```sh
$ python broadcast.py -port 7011 -recipient -message custom message
```

This will run the python script and broadcast the custom message to the default port 7011, which is the same port specified on the Textsend app (can be changed) to a specific recipient or to the registered numbers in the Textsend app. This port has to be the same on your Textsend app in order to work. Note that anyone in your network can send UDP messages on that specific port and will receive those messages if they are listening in on that port.

### Textsend app

The Textsend app is needed to send the actual text messages on the phone on which the app is installed and running. It sends the messages which were UDP broadcasted throughout your network as soon as you broadcast them. This app is available on 

https://play.google.com/store/apps/details?id=com.bouweceunen.textsend

[![](http://www.bouweceunen.com/textsend/textsend.png)](http://www.bouweceunen.com/textsend/textsend.png)
