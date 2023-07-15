# code pick the spaces for parking....

import cv2
import pickle  

rectW,rectH=107,48#dimenssion of rectangle....

try:
    with open('carParkPos','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]#intializing the list with empty

def mouseClick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:   #after clicking left button (mouse) poslist will append(add to the list) the rectangles
        posList.append((x,y)) #adding the area of every single selected to poslist
    if events==cv2.EVENT_RBUTTONDOWN:#after clicking right(mouse) button poslist will pop(delete) the rectangles
        for i,pos in posList.pop():
            x1,y1=pos
            if x1<x<x1+rectW and y1<y<y1+rectH:
                posList.pop(i)      #pop means delete 
    with open('carParkPos','wb') as f:
        pickle.dump(posList,f)
    
         

while True:
    img=cv2.imread("img.png")#image for selecting the area
    for pos in posList: cv2.rectangle(img,pos,(pos[0]+rectW,pos[1]+rectH),(0,0,255),2)
    
    cv2.imshow("Image",img)#showing image
    cv2.setMouseCallback("Image",mouseClick)#the code to work as mouse click..
    cv2.waitKey(0)# to destroy the window by pressing any key
cv2.destroy()
# after completion of the parking selection  the window is not closing we will work on that