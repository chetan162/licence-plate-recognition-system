# Main.py
import cv2
import os
import DetectChars
import DetectPlates
import numpy as np
import  imutils
from tkinter import *
from PIL import Image
from PIL import ImageTk


# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False

###################################################################################################
def main():
    l1=[]
    pos=0
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         # attempt KNN training

    if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
        print("\nerror: KNN traning was not successful\n")  # show error message
        return                                                          # and exit program
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if img_counter == 201:
        # ESC pressed
            break
        elif img_counter <= 200:
        # SPACE pressed
            img_name = "{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()
    k=300
    for i in range (1,199,1):
        imgOriginalScene  = cv2.imread("{}.jpg".format(i))             # open image
        if imgOriginalScene is None:                            # if image was not read successfully
#            print("\nerror: image not read from file \n\n")  # print error message to std out
            
            os.system("pause")                              # pause so user can see error message
            continue                # and exit program
    # end if

        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates
        listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates
        if len(listOfPossiblePlates) == 0:                          # if no plates were found
#            print("\nno license plates were detected\n")  # inform user no plates were found
            cv2.destroyAllWindows()
            continue
        else:
            listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
            licPlate = listOfPossiblePlates[0]
            if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
#                print("\nno characters were detected\n\n")  # show message
                continue                                       # and exit program

       # print("\nlicense plate read from image = " + licPlate.strChars + "\n")  # write license plate text to std out
#        print("----------------------------------------")
        cv2.imwrite("{}.jpg".format(k),imgOriginalScene )
        l1.append(licPlate.strChars)
        k=k+1
    maxi=l1.count(l1[0])
    rept=l1[0]
    for st in l1:
        max1=l1.count(st)
        if max1>maxi:
            rept=st
            maxi=max1
            pos=l1.index(st)
#    print('{} has maximum occurence of {} times found at {} position'.format(rept,maxi,pos))
#    print(l1[pos])
    pos=pos+300
    
    
    image=cv2.imread("{}.jpg".format(pos))

    imgOriginalScene=cv2.imread("{}.jpg".format(pos))

    if imgOriginalScene is None:                            # if image was not read successfully
        print("\nerror: image not read from file \n\n")  # print error message to std out
        os.system("pause")                                  # pause so user can see error message
        return                                              # and exit program
    # end if

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates

    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates

    cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image

    if len(listOfPossiblePlates) == 0:                          # if no plates were found
        print("\nno license plates were detected\n")  # inform user no plates were found
        cv2.destroyAllWindows()
        return
    else:                                                       # else
                # if we get in here list of possible plates has at leat one plate

                # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]
        cv2.imshow("imgThresh", licPlate.imgThresh)
 
        if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
            print("\nno characters were detected\n\n")  # show message
            return                                          # and exit program
        # end if

                  # draw red rectangle around plate
        drawRedRectangleAroundPlate(image, licPlate)

        print("\nlicense plate read from image = " + rept + "\n")  # write license plate text to std out
        print("----------------------------------------")

                 # write license plate text on the image
        cv2.imshow("image orignal", image)# re-show scene image
         
        cv2.imwrite("imgOriginalScene.png", imgOriginalScene)           # write image out to file
        cv2.imshow("original image ", cv2.imread("187.jpg")) 
        
        con=sqlite3.connect('rto.db')
        cor=con.cursor()
        var1='HR26DK8337'
        
        z=8
        s=0
        def red():
            global z
            z=1
        def yellow():
            global z
            z=1
        def green():
            global z
            z=0
        def close():
            light.destroy()
        def close1():
            global s
            s=txt2.get("1.0","end-1c")
            speed.destroy()
        
        light=Tk()
        light.geometry("400x170")
        light.title("select light")
        label1=Label(light,text="SELECT TRAFFIC LIGH COLOR",fg='blue',bg='yellow',relief="solid",font=("arial",15,"bold")).grid(row=0,column=1)
        btn1=Button(light,text="RED",fg='red',bg='red',command=red)
        btn2=Button(light,text="YELLOW",fg='yellow',bg='yellow',command=yellow)
        btn3=Button(light,text="__GREEN__ ",fg='green',bg='green',command=green)
        btn4=Button(light,text="OK",fg='brown',bg='white',font=("arial",15,"bold"),command=close)
        btn1.grid(row=1,column=0)
        btn2.grid(row=2,column=0)
        btn3.grid(row=3,column=0)
        btn4.grid(row=4,column=1)
        light.mainloop()
        
        speed =Tk()
        speed.geometry("400x170")
        speed.title("input speed")
        label1=Label(speed,text="Input speed",fg='blue',bg='yellow',relief="solid",font=("arial",15,"bold")).grid(row=0,column=1)
        txt2=Text(speed,width=20,height=2,wrap=WORD)
        txt2.grid(row=1,column=1)
        btn5=Button(speed,text="OK",fg='brown',bg='white',font=("arial",15,"bold"),command=close1)
        btn5.grid(row=3,column=1)
        speed.mainloop()
        
        
        if z==1:
            t='red/yellow'
        else:
            t='green'
        def show():
            
            
            
            window.destroy()
        
        window=Tk()
        
        window.geometry("1020x1020")
        window.title("welcome")
        label1=Label(window,text="welcome to rto window",fg='blue',bg='yellow',relief="solid",font=("arial",25,"bold")).grid(row=0,column=1)

        photo=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")
        photo1=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")
        photo2=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")
        photo3=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")
        
        label7=Label(window,image=photo)
        label8=Label(window,image=photo1)
        label9=Label(window,image=photo2)
        label10=Label(window,image=photo3)
        label7.grid(row=1,column=0)
        label8.grid(row=1,column=1)
        label9.grid(row=1,column=2)
        label10.grid(row=1,column=3)
        label2=Label(window,text="NO_PLATE :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
        label3=Label(window,text="NAME :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
        label4=Label(window,text="MOBILE_NO :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
        label5=Label(window,text="ADDRESS :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
        label6=Label(window,text="light signal:",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
        label15=Label(window,text="speed:",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
        label2.grid(row=2,column=0)
        label3.grid(row=3,column=0)
        label4.grid(row=4,column=0)
        label5.grid(row=5,column=0)
        label6.grid(row=6,column=0)
        label15.grid(row=7,column=0)


        cor.execute("select * from rto where noplate=?", (var1,) )
        data=cor.fetchone()
        b1=data[0]
        b2=data[1]
        b3=data[2]
        b4=data[3]
        label11=Label(window,text=str(b1),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
        label12=Label(window,text=str(b2),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
        label13=Label(window,text=str(b3),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
        label14=Label(window,text=str(b4),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
        label16=Label(window,text=(str(t)),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
        label17=Label(window,text=(str(s)+" km/hr"),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
        label11.grid(row=2,column=1)
        label12.grid(row=3,column=1)
        label13.grid(row=4,column=1)
        label14.grid(row=5,column=1)
        label16.grid(row=6,column=1)
        label17.grid(row=7,column=1)
        btn=Button(window,text="send_info",width=20,height=4,font=("arial",20,"bold"),fg='brown',bg='white',command=show)
        btn.grid(row=9,column=1)
        con.close()
        window.mainloop()
        
        
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

        
        
        
    return
# end main

###################################################################################################
def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)            # get 4 vertices of rotated rect

    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)         # draw 4 red lines
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)
# end function

###################################################################################################
def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
    ptCenterOfTextAreaX = 0                             # this will be the center of the area the text will be written to
    ptCenterOfTextAreaY = 0

    ptLowerLeftTextOriginX = 0                          # this will be the bottom left of the area that the text will be written to
    ptLowerLeftTextOriginY = 0

    sceneHeight, sceneWidth, sceneNumChannels = imgOriginalScene.shape
    plateHeight, plateWidth, plateNumChannels = licPlate.imgPlate.shape

    intFontFace = cv2.FONT_HERSHEY_SIMPLEX                      # choose a plain jane font
    fltFontScale = float(plateHeight) / 30.0                    # base font scale on height of plate area
    intFontThickness = int(round(fltFontScale * 1.5))           # base font thickness on font scale

    textSize, baseline = cv2.getTextSize(licPlate.strChars, intFontFace, fltFontScale, intFontThickness)        # call getTextSize

            # unpack roatated rect into center point, width and height, and angle
    ( (intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg ) = licPlate.rrLocationOfPlateInScene

    intPlateCenterX = int(intPlateCenterX)              # make sure center is an integer
    intPlateCenterY = int(intPlateCenterY)

    ptCenterOfTextAreaX = int(intPlateCenterX)         # the horizontal location of the text area is the same as the plate

    if intPlateCenterY < (sceneHeight * 0.75):                                                  # if the license plate is in the upper 3/4 of the image
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) + int(round(plateHeight * 1.6))      # write the chars in below the plate
    else:                                                                                       # else if the license plate is in the lower 1/4 of the image
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) - int(round(plateHeight * 1.6))      # write the chars in above the plate
    # end if

    textSizeWidth, textSizeHeight = textSize                # unpack text size width and height

    ptLowerLeftTextOriginX = int(ptCenterOfTextAreaX - (textSizeWidth / 2))           # calculate the lower left origin of the text area
    ptLowerLeftTextOriginY = int(ptCenterOfTextAreaY + (textSizeHeight / 2))          # based on the text area center, width, and height

            # write the text on the image
    cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY), intFontFace, fltFontScale, SCALAR_YELLOW, intFontThickness)
# end function

###################################################################################################
if __name__ == "__main__":
    main()


















