Teleoperate your CNC machine with Web Services
Introduction
Welcome to my CNC Web Service presentation.  The purpose of this project is to use web technologies to control Industrial machines.  The 3 main hardware components are; a CNC machine, a Raspberry Pi3 with a webcam, and a Windows 10 PC.  We are using REST web services.  The front-end uses HTML, CSS, Javascript, JQuery.  The service uses 2 back-ends (servers); Webcam server running on a Raspberry Pi3 with Raspbian Linux, and a Python webserver running on a Windows 10 PC.  

The app from this project allows the user the teleoperate the machine.  In other words, a user can run the machine from a cell phone, tablet, and laptop ..etc.  Also to mention, excluding the CNC machine, the components are very inexpensive and the software is open source.

Origins of CNC webserver
This is actually version 2 of this project.  The first version used a server written C# and required a lot of code.  Also, I did not use the raspberry pi for the video.  I realized that to implement the project, it was going to take some time. I was trying to figure out a better way to implement the web app.  I got the idea for version 2 while attending the AEC Hackathon in Seattle and VR Hackathon in Seattle 2019.  Most importantly the Principal Researcher at ThinkPredict helped a lot.  He did not say how to actually do the project, but he pointed out the direction to look.
Technology used in this Project
In regards to the CNC machine, we are using the KFLOP motion controller from Dynomotion.  Its has the capacity to control 8 axes (servo motors).   For this project we are only controlling 3 axis.  The 3 servo motors are driven by the Snapamp driver from Dynomotion.  I recommend using the Snapamp over Gecko drives, because it provides more torque at higher speeds.  The software to control the machine in written C++ and C#.  The software uses the .NET Framework.

The front-end was developed with HTML, CSS and Javascript, JQuery.  The javascript was modified to implement press and hold on the arrow buttons.  The original HTML required the user to click the button multiple times.  Not a big change to the javascript.

The back-end (server) was developed using Python Flask.  The server runs on the Windows 10 PC.  It is a mixture of the C# code and Python code.  Calling a C# dll in Python is very straightforward.  You will need to install Python and Flask on your PC.  You can use VS Code to debug the Python script.

The Webcam server runs on the Raspbian Linux installed on the Raspberry Pi3.  The server uses the Motion Project to control the video feeds.  You can find it here;

https://github.com/Motion-Project/motion
