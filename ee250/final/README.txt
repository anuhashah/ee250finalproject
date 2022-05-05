Selina Martinez, Anuja Shah
EE250 Final Project

Link to Demo: 

Instructions to run program 

1. Clone the repo on both your raspberry pi and regular computer terminal
2.On your terminal and on your raspberry pi cd into the directory where client.py and server.py live 
3. Sample path is: "/usr/selinama/ee250finalproject/ee250/final/")
4. Ensure that your computer and raspberry pi are on the same network (i.e have both nodes connect to your phone's hotspot)
5. Run 'python3 server.py' on your computer's terminal
6. Run 'python3 client.py's on your raspberry pi
7. As the program runs, your computer will take a photo. Prepare for a photo to be taken. 
8. Photo is sent to the raspberry pi and the LCD will change to reflect the most dominant color, and an output image, a photomosaic of the photo your computer just took, will appear.


External libraries used:
-Numpy
-PILLOW
-Scipy
-dominantcolors
-subprocess
-openCV
-pickle
-socket
-glob
