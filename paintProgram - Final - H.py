'''
Muhammad Nadeem
PAINT PROJECT
January 28,2020
'''
#imports
from pygame import *
from random import randint
from math import sqrt
from tkinter import *
from tkinter import filedialog

root = Tk()     #removes small window
root.withdraw()

mixer.init()            #initializes music
font.init()             #initializes text
myClock = time.Clock()  #frame rate Clock

#screen dimensions
width = 1280 
height = 768
screen = display.set_mode((width,height))

#background picture
themePic=image.load('images/PaintProgramTheme.jpg')
themePic=transform.scale(themePic,(1280,768))
screen.blit(themePic,(0,0))


tool = "no tool"            #initializes tool
omx,omy,mx,my = 0,0,0,0     #initializes mouse positions

#Dimensions
dots = []       #number of points for shape tool
points= 3       #number of points to begin with
rectTh = 1      #thickness of hollow rect
circTh = 1      #thickness of hollow circle
brushTh = 10    #thickness of brush
eraserTh = 10   #thickness of eraser
hsD = 20        #highlighter surface Dimension(squared)
ssLength = 120  #length of stamps when being displayed
ssWidth = 65    #width of stamps when being displayed
sLength = 192   #length of stamps when being stamped
sWidth = 105    #width of stamps when being stamped

#Undo/Redo
undo = []       #undo empty list
redo = []       #redo empty list

#Colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

col = BLACK             #Default colour option
r,g,b,a = (0,0,0,10)    #Colour for transparency

#Rectangles
canvasRect = Rect(20,100,930,520)                       #Rectangle representing the canvas

openRect = Rect(width-260,5,50,50)                      #Rectangle representing the open tool
saveRect = Rect(width-200,5,50,50)                      #Rectangle representing the save tool

pencilRect = Rect(width-120,100,50,50)                  #Rectangle representing the pencil tool
eraserRect = Rect(width-60,100,50,50)                   #Rectangle representing the eraser tool
sprayRect = Rect(width-120,160,50,50)                   #Rectangle representing the spray tool
penRect = Rect(width-60,160,50,50)                      #Rectangle representing the pen tool
brushRect = Rect(width-120,220,50,50)                   #Rectangle representing the brush tool
hiliRect = Rect(width-60,220,50,50)                     #Rectangle representing the highlighter tool
lineRect = Rect(width-120,280,50,50)                    #Rectangle representing the line tool
squareRect = Rect(width-60,280,50,50)                   #Rectangle representing the square tool
circleRect = Rect(width-120,340,50,50)                  #Rectangle representing the circle tool
shapeRect = Rect(width-60,340,50,50)                    #Rectangle representing the shape tool
toolBackRect = Rect(width-122,98,115,356)               #Rectangle representing the backdrop of the tools
desRect = Rect(970,120,180,200)                         #Rectangle representing the area for descriptions
tempScreenCap2 = screen.subsurface(desRect).copy()      #ScreenShot for the description area

stampRect = Rect((width//2)-207,670,842,68)             #Rectangle representing the area containing stamps
stampStart = (width//2)-205                             #The point at which the first displayed stamp is shown
nextSRect = Rect(876,645,20,20)                         #Rectangle representing the button for the next stamp
prevSRect = Rect(836,645,20,20)                         #Rectangle representing the button for the previous stamp

undoRect = Rect(30,630,50,50)                           #Rectangle representing the undo tool
redoRect = Rect(90,630,50,50)                           #Rectangle representing the redo tool
clearScreenRect = Rect(30,690,110,70)                   #Rectangle representing the clear screen tool

thRectDown = Rect(width-105,410,20,20)                  #Rectangle representing the tool to raise the thickness/points
thRectUp = Rect(width-45,410,20,20)                     #Rectangle representing the tool to lower the thickness/points

musicRect = Rect(width/2-385,633,70,70)                 #Rectangle representing the music button (On and Off)
prevRect = Rect((width/2)-455,643,50,50)                #Rectangle representing the previous song button
nextRect = Rect((width/2)-295,643,50,50)                #Rectangle representing the next song button
scrollRect = Rect((width/2)-475,730,250,9)              #Rectangle representing the area for the time slider

#Text
tmrc = font.SysFont("Times New Roman",25)                       #passing a Times New Roman font for the thickness/points counter
tmrd = font.SysFont("Times New Roman",20,True)                  #passing a Times New Roman font for the descriptions
des = ["Select a Tool:", "Change colour", "with colour wheel"]  #starting description

#Importing images
wheelPic=image.load("images/colourwheel.png")
colourWheel=transform.scale(wheelPic,(90,90))
pencilPic=image.load('images/pencil.png')
pencilPic=transform.scale(pencilPic,(47,47))
eraserPic=image.load('images/eraser.png')
eraserPic=transform.scale(eraserPic,(47,47))
sprayPic=image.load('images/spray.jpg')
sprayPic=transform.scale(sprayPic,(47,47))
penPic=image.load('images/pen.png')
penPic=transform.scale(penPic,(47,47))
brushPic=image.load('images/brush.png')
brushPic=transform.scale(brushPic,(47,47))
hiliPic=image.load('images/highlighter.png')
hiliPic=transform.scale(hiliPic,(47,47))
linePic=image.load('images/line.png')
linePic=transform.scale(linePic,(47,47))
rectPic=image.load('images/rectangle.png')
rectPic=transform.scale(rectPic,(47,47))
circlePic=image.load('images/circle.png')
circlePic=transform.scale(circlePic,(47,47))
shapePic=image.load('images/polygon.png')
shapePic=transform.scale(shapePic,(47,47))
openPic=image.load('images/open.png')
openPic=transform.scale(openPic,(47,47))
savePic=image.load('images/save.png')
savePic=transform.scale(savePic,(47,47))
undoPic=image.load('images/undo.png')
undoPic=transform.scale(undoPic,(47,47))
redoPic=transform.flip(undoPic,True,False)
clearScreenPic=image.load('images/clearScreen.png')
clearScreenPic=transform.scale(clearScreenPic,(107,67))         #above images are loaded and resized (redoPic is flipped from undoPic)

tempList1 = ['images/Pic-Watcher-1.jpg','images/Pic-Strider-1.jpg','images/Pic-Bellowback-1.jpg','images/Pic-Ravager-1.jpg','images/Pic-Behemoth-1.jpg','images/Pic-Trampler-1.jpg','images/Pic-Rockbreaker-1.jpg','images/Pic-Stalker-1.jpg','images/Pic-Deathbringer-1.jpg','images/Pic-Stormbird-1.jpg','images/Pic-Snapmaw-1.jpg','images/Pic-Shellwalker-1.jpg','images/Pic-Thunderjaw-1.jpg','images/Pic-Tallneck-1.jpg']
showStampList = [] #Stamps to be displayed
#Lists of stamps to be loaded and displayed (with backgrounds)

tempList2 = ['images/Pic-Watcher-2.png','images/Pic-Strider-2.png','images/Pic-Bellowback-2.png','images/Pic-Ravager-2.png','images/Pic-Behemoth-2.png','images/Pic-Trampler-2.png','images/Pic-Rockbreaker-2.png','images/Pic-Stalker-2.png','images/Pic-Deathbringer-2.png','images/Pic-Stormbird-2.png','images/Pic-Snapmaw-2.png','images/Pic-Shellwalker-2.png','images/Pic-Thunderjaw-2.png','images/Pic-Tallneck-2.png']
stampList = []#stamps to be stamped
#Lists of stamps to be loaded and stamped (no backgrounds)

for stamp in tempList1:
    showStamp = image.load(stamp)
    showStamp = transform.scale(showStamp,(ssLength,ssWidth))
    showStampList.append(showStamp)
#loads and resizes stamps, and appends them to an empty list for displaying
for stamp in tempList2:
    picture = image.load(stamp)
    picture = transform.scale(picture,(sLength,sWidth))
    stampList.append(picture)
#loads and resizes stamps, and appends them to an empty list for stamping

stampSelect = False     #sees if a stamp is currently selected
nextS = False           #sees if the button 'nextSRect' has been pressed
prevS = False           #sees if the button 'prevSRect' has been pressed

#Music
tracks = ['music/01.Tank!.ogg','music/flyers_-_bradio.ogg','music/1-01 DANGANRONPA.ogg'] #song filenames
song = 0                #song number (index for 'tracks')
num = len(tracks)       #number of songs in 'tracks'
musicTime = 0           #initializes the value for 'seconds per pixel' on the time slider
totalTime = []          #empty list for total lengths of songs
musicIncrement = 0      #initializes the increase in the slider's length every frame
for i in range (num):
    totalTime.append(mixer.Sound(tracks[i]).get_length())
#finds the lengths of all songs and appends them to the empty list

draw.rect(screen,WHITE,canvasRect)

screenCap = screen.subsurface(canvasRect).copy() #takes a ScreenShot of the blank canvas
undo.append(screenCap)                           #appends the blank canvas into undo

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = evt.pos                                 #initializes initial click coordinates
            hiliHead = Surface((hsD,hsD),SRCALPHA)          #creates a surface for the highlighter to be used for transparency
        if evt.type == MOUSEBUTTONUP:
            screen.set_clip(canvasRect)                     #keeps all updates within the canvas
            if mb[0]==1 and thRectUp.collidepoint(sx,sy):   #checks if the increase thickness/points tool is clicked
                dots = []                                   #empties the points list
                if tool == "hollow square" and rectTh<20:
                    rectTh+=1
                    number = rectTh
                if tool == "hollow circle" and circTh<20:
                    circTh+=1
                    number = circTh
                if tool == "shape" and points<10:
                    points+=1
                    number = points
                if tool == "brush" and brushTh<20:
                    brushTh+=1
                    number = brushTh
                if tool == "eraser" and eraserTh<20:
                    eraserTh+=1
                    number = eraserTh
                if tool == "highlighter" and hsD<40:
                    hsD+=2
                    number = hsD
                #increases the thickness/points of the specific tool selected 
            if mb[0]==1 and thRectDown.collidepoint(sx,sy): #checks if the decrease thickness/points tool is clicked
                dots = []                                   #empties the points list
                if tool == "hollow square" and rectTh>1:
                    rectTh-=1
                    number = rectTh
                if tool == "hollow circle" and circTh>1:
                    circTh-=1
                    number = circTh
                if tool == "shape" and points>3:
                    points-=1
                    number = points
                if tool == "brush" and brushTh>1:
                    brushTh-=1
                    number = brushTh
                if tool == "eraser" and eraserTh>1:
                    eraserTh-=1
                    number = eraserTh
                if tool == "highlighter" and hsD>10:
                    hsD-=2
                    number = hsD
                #dencreases the thickness/points of the specific tool selected
                #variable 'number' represents the counter value to be displayed as text
            if mb[0]==1:
                if nextRect.collidepoint(sx,sy):
                    song = (song+1)%num
                    musicTime = 0
                    musicIncrement = 0
                    if mixer.music.get_busy():
                        print (tracks[song])
                        mixer.music.load(tracks[song])
                        mixer.music.play(0)
                if prevRect.collidepoint(sx,sy):
                    song = (song-1)%num
                    musicTime = 0
                    musicIncrement = 0
                    if mixer.music.get_busy():
                        print (tracks[song])
                        mixer.music.load(tracks[song])
                        mixer.music.play(0)
                if musicRect.collidepoint(sx,sy) and mixer.music.get_busy() == False:
                    print (tracks[song])
                    mixer.music.load(tracks[song])
                    mixer.music.play(0)
                    track = mixer.Sound(tracks[song])
                elif musicRect.collidepoint(sx,sy) and mixer.music.get_busy():
                    mixer.music.stop()
                if mb[0]==1 and scrollRect.collidepoint(mx,my):
                    musicTime = (sx-165)*(totalTime[song]/250)
                    mixer.music.set_pos(musicTime)
            if tool == "line":
                draw.line(screen,col,(sx,sy),(mx,my))
                screenCap = screen.subsurface(canvasRect).copy()
                screen.blit(screenCap,(20,100))
            if tool == "square":
                draw.rect(screen,col,(sx,sy,mx-sx,my-sy))
                screenCap = screen.subsurface(canvasRect).copy()
                screen.blit(screenCap,(20,100))
            if tool == "hollow square":
                for i in range (rectTh):
                    if sx<mx and sy<my:
                        draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1)
                    if sx>mx and sy>my:
                        draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1)
                    if sx>mx and sy<my:
                        draw.rect(screen,col,(mx-i,sy-i,sx-mx+i*2,my-sy+i*2),1)
                    if sx<mx and sy>my:
                        draw.rect(screen,col,(sx-i,my-i,mx-sx+i*2,sy-my+i*2),1)
                screenCap = screen.subsurface(canvasRect).copy()
                screen.blit(screenCap,(20,100))
            if tool == "circle":
                if sx<mx and sy<my:
                    draw.ellipse(screen,col,(sx,sy,mx-sx,my-sy))
                if sx>mx and sy>my:
                    draw.ellipse(screen,col,(mx,my,sx-mx,sy-my))
                if sx<mx and sy>my:
                    draw.ellipse(screen,col,(sx,my,mx-sx,sy-my))
                if sx>mx and sy<my:
                    draw.ellipse(screen,col,(mx,sy,sx-mx,my-sy))
                screenCap = screen.subsurface(canvasRect).copy()
                screen.blit(screenCap,(20,100))
            if tool == "hollow circle":
                for i in range (circTh):
                    try:
                        if sx<mx and sy<my:
                            draw.ellipse(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1)
                            if circTh>1:
                                draw.ellipse(screen,col,(sx-i+1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(sx-i+1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                        if sx>mx and sy>my:
                            draw.ellipse(screen,col,(mx-i,my-i,sx-mx+i*2,sy-my+i*2),1)
                            if circTh>1:
                                draw.ellipse(screen,col,(mx-i+1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(mx-i+1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                        if sx<mx and sy>my:
                            draw.ellipse(screen,col,(sx-i,my-i,mx-sx+i*2,sy-my+i*2),1)
                            if circTh>1:
                                draw.ellipse(screen,col,(sx-i+1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(sx-i+1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                        if sx>mx and sy<my:
                            draw.ellipse(screen,col,(mx-i,sy-i,sx-mx+i*2,my-sy+i*2),1)
                            if circTh>1:
                                draw.ellipse(screen,col,(mx-i+1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(mx-i+1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)

                    except:
                        pass
                screenCap = screen.subsurface(canvasRect).copy()
                screen.blit(screenCap,(20,100))
            if tool == "shape" and canvasRect.collidepoint(mx,my):
                dots.append((mx,my))
                for i in range (len(dots)):
                    draw.circle(screen,col,(dots[i]),1)
                    screenCap=screen.subsurface(canvasRect).copy()
                    screen.blit(screenCap,(20,100))
                if len(dots)==points:
                    draw.polygon(screen,col,dots)
                    screenCap=screen.subsurface(canvasRect).copy()
                    screen.blit(screenCap,(20,100))
                    undo.append(screenCap)
                    dots = []
            if tool!= "no tool" and canvasRect.collidepoint(mx,my):
                screenCap = screen.subsurface(canvasRect).copy()
                if tool == "shape":
                    pass
                else:
                    undo.append(screenCap)
            if stampRect.collidepoint(mx,my):
                pos = (sx-((width//2)-200))//ssLength
                tool = "stamp"
                nextS = False
                prevS = False
            if mb[0]==1 and nextSRect.collidepoint(sx,sy) and nextS:
                temp1 = showStampList[0]
                showStampList = showStampList[1:]+[temp1]
                temp2 = stampList[0]
                stampList = stampList[1:]+[temp2]
            if mb[0]==1  and prevSRect.collidepoint(sx,sy) and prevS:
                temp1 = showStampList.pop()
                showStampList = [temp1]+showStampList
                temp2 = stampList.pop()
                stampList = [temp2]+stampList
            if mb[0]==1 and tool == "stamp":
                stampSelect = True
                screen.set_clip(canvasRect)
                screen.blit(stampList[pos],(sx-(sLength//2),sy-(sWidth//2)))
                screenCap = screen.subsurface(canvasRect).copy()
                if mb[0]==1 and canvasRect.collidepoint(sx,sy):
                    stampSelect = False
                    tool = "no tool"
            if mb[0]==1 and undoRect.collidepoint(sx,sy) and len(undo)>1:
                z = undo.pop()
                screen.blit(undo[-1],(20,100))
                redo.append(z)
            if mb[0]==1 and redoRect.collidepoint(sx,sy) and len(redo)>1:
                w = redo.pop()
                undo.append(w)
                screen.blit(undo[-1],(20,100))
            screen.set_clip(None)

    #mouse information
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    
    #drawing tools
    draw.rect(screen,BLACK,toolBackRect)
    draw.rect(screen,BLUE,openRect,2)
    screen.blit(openPic,(width-258,7))
    draw.rect(screen,BLUE,saveRect,2)
    screen.blit(savePic,(width-198,7))
    
    draw.rect(screen,GREEN,pencilRect,2)
    screen.blit(pencilPic,(1162,102))
    draw.rect(screen,GREEN,eraserRect,2)
    screen.blit(eraserPic,(1222,102))
    draw.rect(screen,GREEN,sprayRect,2)
    screen.blit(sprayPic,(1162,162))
    draw.rect(screen,GREEN,penRect,2)
    screen.blit(penPic,(1222,162))
    draw.rect(screen,GREEN,brushRect,2)
    screen.blit(brushPic,(1162,222))
    draw.rect(screen,GREEN,hiliRect,2)
    screen.blit(hiliPic,(1222,222))
    draw.rect(screen,GREEN,lineRect,2)
    screen.blit(linePic,(1162,282))
    draw.rect(screen,GREEN,squareRect,2)
    screen.blit(rectPic,(1222,282))
    draw.rect(screen,GREEN,circleRect,2)
    draw.rect(screen,WHITE,(width-118,342,47,47))
    screen.blit(circlePic,(1162,342))
    draw.rect(screen,GREEN,shapeRect,2)
    draw.rect(screen,WHITE,(width-58,342,47,47))
    screen.blit(shapePic,(1222,342))
    
    draw.rect(screen,PURPLE,stampRect,2)
    screen.blit(colourWheel,(1185,3))
    draw.rect(screen,WHITE,nextSRect)
    draw.polygon(screen,BLACK,[(876,645),(876,665),(896,655)])
    draw.rect(screen,WHITE,prevSRect)
    draw.polygon(screen,BLACK,[(855,645),(855,665),(836,655)])

    draw.rect(screen,CYAN,undoRect,2)
    screen.blit(undoPic,(32,632))
    draw.rect(screen,CYAN,redoRect,2)
    screen.blit(redoPic,(92,632))
    draw.rect(screen,PURPLE,clearScreenRect,2)
    screen.blit(clearScreenPic,(32,692))

    if tool == "hollow square" or tool == "hollow circle" or tool == "shape" or tool == "brush" or tool == "eraser" or tool == "highlighter":
        draw.rect(screen,WHITE,thRectUp,2)
        draw.rect(screen,WHITE,thRectDown,2)
        draw.line(screen,WHITE,(width-35,414),(width-35,426))
        draw.line(screen,WHITE,(width-41,420),(width-29,420))
        draw.line(screen,WHITE,(width-101,420),(width-89,420))
        counter = tmrc.render(str(number),0,WHITE)
        tempScreenCap1 = screen.subsurface(toolBackRect).copy()
        screen.blit(tempScreenCap1,(width-122,98))
        if number<10:
            screen.blit(counter,(width-70,407))
        else:
            screen.blit(counter,(width-77,407))
    else:
        draw.rect(screen,BLACK,thRectUp,2)
        draw.rect(screen,BLACK,thRectDown,2)

    #music player
    draw.rect(screen,RED,musicRect,2)
    draw.rect(screen,BLACK,(width/2-383,635,67,67))
    if mixer.music.get_busy():
        draw.circle(screen,RED,(int(width/2-349),669),15)
    else:
        draw.polygon(screen,RED,[(width/2-368,652),(width/2-368,687),(width/2-333,670)])
    draw.rect(screen,RED,nextRect,2)
    draw.rect(screen,BLACK,(width/2-293,645,47,47))
    draw.polygon(screen,RED,[(width/2-281,657),(width/2-281,682),(width/2-268,670)])
    draw.polygon(screen,RED,[(width/2-268,657),(width/2-268,682),(width/2-256,670)])
    draw.rect(screen,RED,prevRect,2)
    draw.rect(screen,BLACK,(width/2-453,645,47,47))
    draw.polygon(screen,RED,[(width/2-420,657),(width/2-420,682),(width/2-432,670)])
    draw.polygon(screen,RED,[(width/2-432,657),(width/2-432,682),(width/2-445,670)])

    draw.rect(screen,BLACK,scrollRect)
    draw.rect(screen,WHITE,((width/2)-475,730,250*(musicTime/totalTime[song])+musicIncrement,9))
    if mixer.music.get_busy():
        musicIncrement += (totalTime[song]/250)/60
    elif 250*(musicTime/totalTime[song])+musicIncrement>=totalTime[song]:
        musicTime = 0
        musicIncrement = 0
        mixer.music.load(tracks[song])
        mixer.music.play()
    if mb[0]==1 and scrollRect.collidepoint(sx,sy) or mixer.music.get_busy()==False:
        musicIncrement = 0
        musicTime = 0
        
    #selecting tools
    if openRect.collidepoint(mx,my):
        draw.rect(screen,RED,openRect,2)
        des = ["Open File"]
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
        des = ["Save File"]
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,RED,pencilRect,2)
        if mb[0]==1:
            tool = "pencil"
            des = ["Pencil:","Draw whatever", "you want"]
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,RED,eraserRect,2)
        if mb[0]==1:
            tool = "eraser"
            number = eraserTh
            des = ["Eraser:", "Erase your work", "Change thickness", "with + and -"]
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,RED,sprayRect,2)
        if mb[0]==1:
            tool = "spray"
            des = ["Spray:","Spray paint", "texture"]
    if penRect.collidepoint(mx,my):
        draw.rect(screen,RED,penRect,2)
        if mb[0]==1:
            tool = "pen"
            des = ["Pen:","Draws lines", "that look like", "caligraphy"]
    if brushRect.collidepoint(mx,my):
        draw.rect(screen,RED,brushRect,2)
        if mb[0]==1:
            tool = "brush"
            number = brushTh
            des = ["Brush:", "Thicker than a", "pencil", "draw whatever", "you want", "Change thickness", "with + and -"]
    if hiliRect.collidepoint(mx,my):
        draw.rect(screen,RED,hiliRect,2)
        if mb[0]==1:
            tool = "highlighter"
            number = hsD
            des = ["Highlighter:","Draws transparent" ,"lines wherever you", "want", "Change thickness","with + and - (By 2)"]
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,RED,lineRect,2)        
        if mb[0]==1:
            tool = "line"
            des = ["Line:","Click and drag", "to draw a line", "from mouse click", "to release point"]
    if squareRect.collidepoint(mx,my):
        draw.rect(screen,RED,squareRect,2)
        if mb[0]==1:
            tool = "square"
            des = ["Square:", "Draws a filled","rectangular object", "Right click for", "hollow square"]
        if mb[2]==1:
            tool = "hollow square"
            number = rectTh
            des = ["Hollow Square:","Draws an unfilled", "rectangular object", "Left click for", "filled square", "Change thickness","with + and -"]
    if circleRect.collidepoint(mx,my):
        draw.rect(screen,RED,circleRect,2)        
        if mb[0]==1:
            tool = "circle"
            des = ["Circle:","Draws a filled", "circle", "Right click for", "hollow circle"]
        if mb[2]==1:
            tool = "hollow circle"
            number = circTh
            des = ["Hollow Circle:","Draws an unfilled", "circle", "Left click for", "filled circle", "Change thickness","with + and -"]
    if shapeRect.collidepoint(mx,my):
        draw.rect(screen,RED,shapeRect,2)        
        if mb[0]==1:
            tool = "shape"
            number = points
            des = ["Shape:", "Click on the", "canvas as many", "times as the", "counter says and", "you will draw", "a shape", "Change # of", "points with + and -"]
    if stampRect.collidepoint(mx,my):
        des = ["Stamp:", "Select a stamp", "and paste it", "to the canvas", "Click Left and", "Right to scroll", "through options"]
    if nextSRect.collidepoint(mx,my):
        draw.polygon(screen,RED,[(876,645),(876,665),(896,655)])
        nextS = True
        prevS = False
    if prevSRect.collidepoint(mx,my):
        draw.polygon(screen,RED,[(855,645),(855,665),(836,655)])
        prevS = True
        nextS = False

    screen.blit(tempScreenCap2,(970,120))
    for i in range (len(des)):
        description = tmrd.render(des[i],0,BLACK)
        screen.blit(description,(975,135+i*20))
            
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
        des = ["Undo"]
    elif redoRect.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect,2)
        des = ["Redo"]
    elif clearScreenRect.collidepoint(mx,my):
        draw.rect(screen,RED,clearScreenRect,2)
        des = ["Clear Screen"]
    else:
        pass

    if musicRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,musicRect,2)
        if mixer.music.get_busy():
            draw.circle(screen,GREEN,(int(width/2-349),669),15)
        else:
            draw.polygon(screen,GREEN,[(width/2-368,652),(width/2-368,687),(width/2-333,670)])
    if prevRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,prevRect,2)
        draw.polygon(screen,GREEN,[(width/2-420,657),(width/2-420,682),(width/2-432,670)])
        draw.polygon(screen,GREEN,[(width/2-432,657),(width/2-432,682),(width/2-445,670)])
    if nextRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,nextRect,2)
        draw.polygon(screen,GREEN,[(width/2-281,657),(width/2-281,682),(width/2-268,670)])
        draw.polygon(screen,GREEN,[(width/2-268,657),(width/2-268,682),(width/2-256,670)])
            
    #using tools
    if mb[0]==1 and openRect.collidepoint(mx,my):
        try:
            fname=filedialog.askopenfilename()
            mypic=image.load(fname)
            if mypic.get_rect().size[0]>950 or mypic.get_rect().size[1]>620:
                mypic=transform.scale(mypic,(950,620))
            screen.blit(mypic,(20,100))
        except:
            print("Load error")
    if mb[0]==1 and saveRect.collidepoint(mx,my):
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            image.save(screenCap, fname)
        except:
            print("Saving error")
    screen.set_clip(canvasRect)
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool == "pencil":
            draw.line(screen,col,(mx,my),(omx,omy))
        if tool == "eraser":
            draw.circle(screen,WHITE,(mx,my),eraserTh)
            dx = mx-omx
            dy = my-omy
            h = int(sqrt((dx**2)+(dy**2)))
            for i in range (1,h):
                cx,cy = int(omx+i*dx/h),int(omy+i*dy/h)
                draw.circle(screen,WHITE,(cx,cy),eraserTh)
        if tool == "spray":
            for i in range (16):
                rx,ry = randint(-15,15),randint(-15,15)
                dx = mx - rx
                dy = my - ry
                if (dx-mx)**2+(dy-my)**2<=15**2:
                    draw.circle(screen,col,(mx-rx,my-ry),int(0.5))
        if tool == "pen":
            draw.polygon(screen,col,[(omx,omy-5),(omx,omy+5),(mx,my+5),(mx,my-5)])
        if tool == "brush":
            draw.circle(screen,col,(mx,my),brushTh)
            dx = mx-omx
            dy = my-omy
            h = int(sqrt((dx**2)+(dy**2)))
            for i in range (1,h):
                cx,cy = int(omx+i*dx/h),int(omy+i*dy/h)
                draw.circle(screen,col,(cx,cy),brushTh)
        if tool == "highlighter":
            draw.circle(hiliHead,(r,g,b,15),(hsD//2,hsD//2),hsD//2)
            screen.blit(hiliHead,(mx-(hsD//2),my-(hsD//2)))
            dx = mx-omx
            dy = my-omy
            h = int(sqrt((dx**2)+(dy**2)))
            for i in range (1,h):
                cx,cy = int(omx+i*dx/h),int(omy+i*dy/h)
                screen.blit(hiliHead,(cx-(hsD//2),cy-(hsD//2)))
        if tool == "line":
            screen.blit(screenCap,(20,100))
            draw.line(screen,col,(sx,sy),(mx,my))
        if tool == "square":
            screen.blit(screenCap,(20,100))
            draw.rect(screen,col,(sx,sy,mx-sx,my-sy))
        if tool == "hollow square":
            screen.blit(screenCap,(20,100))
            for i in range (rectTh):
                if sx<mx and sy<my:
                    draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1)
                if sx>mx and sy>my:
                    draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1)
                if sx>mx and sy<my:
                    draw.rect(screen,col,(mx-i,sy-i,sx-mx+i*2,my-sy+i*2),1)
                if sx<mx and sy>my:
                    draw.rect(screen,col,(sx-i,my-i,mx-sx+i*2,sy-my+i*2),1)
        if tool == "circle":
            screen.blit(screenCap,(20,100))
            if sx<mx and sy<my:
                draw.ellipse(screen,col,(sx,sy,mx-sx,my-sy))
            if sx>mx and sy>my:
                draw.ellipse(screen,col,(mx,my,sx-mx,sy-my))
            if sx<mx and sy>my:
                draw.ellipse(screen,col,(sx,my,mx-sx,sy-my))
            if sx>mx and sy<my:
                draw.ellipse(screen,col,(mx,sy,sx-mx,my-sy))
        if tool == "hollow circle":
            screen.blit(screenCap,(20,100))
            for i in range (circTh):
                try:
                    if sx<mx and sy<my:
                        draw.ellipse(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1)
                        if circTh>1:
                            draw.ellipse(screen,col,(sx-i+1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                            draw.ellipse(screen,col,(sx-i-1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                            draw.ellipse(screen,col,(sx-i+1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                            draw.ellipse(screen,col,(sx-i-1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                    if sx>mx and sy>my:
                        draw.ellipse(screen,col,(mx-i,my-i,sx-mx+i*2,sy-my+i*2),1)
                        if circTh>1:
                            draw.ellipse(screen,col,(mx-i+1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                            draw.ellipse(screen,col,(mx-i-1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                            draw.ellipse(screen,col,(mx-i+1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                            draw.ellipse(screen,col,(mx-i-1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                    if sx<mx and sy>my:
                        draw.ellipse(screen,col,(sx-i,my-i,mx-sx+i*2,sy-my+i*2),1)
                        if circTh>1:
                            draw.ellipse(screen,col,(sx-i+1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                            draw.ellipse(screen,col,(sx-i-1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                            draw.ellipse(screen,col,(sx-i+1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                            draw.ellipse(screen,col,(sx-i-1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                    if sx>mx and sy<my:
                        draw.ellipse(screen,col,(mx-i,sy-i,sx-mx+i*2,my-sy+i*2),1)
                        if circTh>1:
                            draw.ellipse(screen,col,(mx-i+1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)
                            draw.ellipse(screen,col,(mx-i-1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                            draw.ellipse(screen,col,(mx-i+1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                            draw.ellipse(screen,col,(mx-i-1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)
                except:
                    pass
    if mb[0]==1 and clearScreenRect.collidepoint(mx,my):
        screen.subsurface(canvasRect).fill(WHITE)
        undo = []
        redo = []
        screenCap = screen.subsurface(canvasRect).copy()
        undo.append(screenCap)
    screen.set_clip(None)

    #using stamps
    for i in range (7):
        screen.blit(showStampList[i],(stampStart+(i%7*ssLength),672))
    if tool == "stamp" and canvasRect.collidepoint(mx,my) and stampSelect:
        screen.set_clip(canvasRect)
        screen.blit(screenCap,(20,100))
        screen.blit(stampList[pos],(mx-(sLength//2),my-(sWidth//2)))

    #selecting colour
    if mb[0]==1 and ((mx-1230)**2+(my-48)**2)<=45**2:
        col = screen.get_at((mx,my))
        r,g,b,a = screen.get_at((mx,my))
    if mb[2]==1 and ((mx-1230)**2+(my-48)**2)<=45**2:
        col = BLACK
        r,g,b,a = (0,0,0,255)

    display.flip()
    omx,omy = mx,my
    myClock.tick(60)
    
quit()
