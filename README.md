# Textsend - Send text messages through your phone with UDP messages

Textsend will allow you to send textmessages directly from received UDP broadcasted messages. This can be used if you have a spare Android phone and have a need for sending text messages to your phone in case you have a custom burglary alarm or custom made smoke detector with for example a raspberry pi. It uses the Textsend app along with a UDP broadcast script to run on your computer. The Android application receives the broadcasted UDP messages in your network over a specific port which in turn will be sent to specified numbers. 

Feel free to let me know if something isn't working as it should at bouwe.ceunen@gmail.com

### Things to consider
- Your phone and computer must be connected to the same network through wifi or ethernet when your text message arrives.
- Make sure there are no firewall restrictions on outgoing UDP messages.

### Get it running (macOS, Windows, Linux)

Run this command in your terminal of choice.
```sh
$ python broadcast.py 7011 "custom message"
```
This will run the python script and broadcast the custom message to UDP port 7011, which is the same port specified on the Textsend app (can be changed). This port has to be the same on your Textsend app in order to work. Note that anyone in your network can send UDP messages on that specific port and will receive those messages if they are listening in on that port.

### Textsend app

The Textsend app is needed to send the actual text messages on the phone on which the app is installed and running. It sends the messages which were UDP broadcasted throughout your network as soon as you broadcast them. This app is available on 

https://play.google.com/store/apps/details?id=com.bouweceunen.textsend

[![](http://www.bouweceunen.com/textsend/textsend.png)](http://www.bouweceunen.com/textsend/textsend.png)

[![](http://www.bouweceunen.com/textsend/textsend2.png)](http://www.bouweceunen.com/textsend/textsend2.png)
