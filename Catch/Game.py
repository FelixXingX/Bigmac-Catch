##Name: Felix
## Assignment: ISU
## Date Completed : 06/14/2019




from graphics import *
import time
from random import randint
import threading
import winsound
win = GraphWin("window",500,800,autoflush = False)
win.setBackground("black")
menu = True
menuI = True
start = False
lifeC = 5
regen = 0
deth = False
miss = False
score = 0
R = True
class startMove (threading.Thread):    ## Thread to do animation at the beginning(not really nessessary)
    def __init__ (self):
        threading.Thread.__init__(self)
    def run (self):
        global menuI
        direction = 1
        x1 = 100
        x2 = 400
        catch = Image(Point(x1,700),"Catch.gif")
        catch2 = Image(Point(x2,700),"Catch2.gif")

        while menuI == True:
            if direction == 1:
                catch2.undraw()
                catch = Image(Point(x1,700),"Catch.gif")
                catch.draw(win)
                win.update()
                time.sleep(0.1)
                catch.undraw()
                x1 = x1 + 10
                if x1 == 400:
                    x1 = 100
                    direction = -1
            if direction == -1:
                catch.undraw()
                catch2 = Image(Point(x2,700),"Catch2.gif")
                catch2.draw(win)
                win.update()
                time.sleep(0.1)
                catch2.undraw()
                x2 = x2 - 10
                if x2 == 100:
                    x2 = 400
                    direction = 1

            

                
            




        
class intro (threading.Thread):  ## The menu thread 
    def __init__ (self):
        threading.Thread.__init__(self)
    def run (self):
        global start
        global menuI
        global menu
        while menu == True:
            
## I wanted to add background music but i dont know how to  play multiple sounds simultaneously using winsound 
            aOval = Oval(Point(50,50),Point(450,200))
            aOval.setOutline("white")
            aOval.setWidth(5)
            aOval.draw(win)
            TiText = Text(Point(250,125),"Osu!Catch")
            TiText.setSize(35)
            TiText.setFill("white")
            TiText.draw(win)
            xdText = Text(Point(250,165),"The Rip Off")
            xdText.setSize(10)
            xdText.setFill("white")
            xdText.draw(win)

            stRec = Rectangle(Point(100,300),Point(400,400))
            stRec.setOutline("white")
            stRec.setWidth(2)
            stRec.draw(win)
            stText = Text(Point(250,350),"Start")
            stText.setFill("white")
            stText.setSize(25)
            stText.draw(win)

            dc = Text(Point(250,450),"Date Completed: 06/14/2019")
            dc.setSize(10)
            dc.setFill("white")
            dc.draw(win)
            nm = Text(Point(250,475),"Created By: Felix Xing")
            nm.setSize(10)
            nm.setFill("white")
            nm.draw(win)
            
                      
            while True:
                nxt = win.getMouse()
                if nxt.getX() >= 100 and nxt.getX() <=400 and nxt.getY() >= 300 and nxt.getY() <=400:
                    menuI = False ## goes to next screen from start screen
                    stRec.undraw()
                    aOval.undraw()
                    xdText.undraw()
                    TiText.undraw()
                    stText.undraw()
                    nm.undraw()
                    dc.undraw()
                    while menu == True:         ## I dont think these while loops are necessary but yea whatever
                        Instruction = Image(Point(250,400),"Instruction.gif")
                        Instruction.draw(win)
                        staRec = Rectangle(Point(150,650),Point(350,750))
                        staRec.setOutline("white")
                        staRec.setWidth(5)
                        staRec.draw(win)
                        staText = Text(Point(250,700),"START")
                        staText.setTextColor("light blue")
                        staText.setSize(30)
                        staText.draw(win)
                        while menu == True:
                            nxt = win.getMouse()
                            if nxt.getX() >= 150 and nxt.getX() <= 350 and nxt.getY() >= 650 and nxt.getY() <= 750:
                                staRec.undraw()     
                                Instruction.undraw()
                                staText.undraw()
                                menu == False
                                start = True     ## Game starts
                    
                    
            
class startGame (threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
    def run (self):
        global x3
        global miss
        global hit
        global regen
        global lifeC
        global life
        global deth
        global catch
        global catch2
        

        while R == True:   ## R is just a variable that helps with restarting the program when they wanna retry
            time.sleep(1)
            while start == True:

                if deth == True:
                    catch.undraw()
                    catch2.undraw()
                    break

                life1 = Image(Point(460,520),"Life.gif")    ## Draws everything
                life2 = Image(Point(460,460),"Life.gif")
                life3 = Image(Point(460,400),"Life.gif")
                life4 = Image(Point(460,340),"Life.gif")
                life5 = Image(Point(460,280),"Life.gif")
                life1.draw(win)
                life2.draw(win)
                life3.draw(win)
                life4.draw(win)
                life5.draw(win)
                life = [life1,life2,life3,life4,life5]
                x1 = 250
                x2 = 250
                x3 = 160
                catch = Image(Point(x1,700),"Catch.gif")
                catch2 = Image(Point(x2,700),"Catch2.gif")
                catch.draw(win)
                line = Line(Point(x3,610),Point(x3+175,610))


                while start == True:   ## moves the character
                    if deth == True:    ## checks if you have died
                        catch.undraw()
                        catch2.undraw()
                        

                        break

                    move = win.checkKey()
                   
                    
                    if x1 >= 110:
                        if move == "Left":
                            x1 = x1 - 80
                            x2 = x2 - 80
                            x3 = x3 - 80
                            catch.undraw()
                            catch2.undraw()
                            line.undraw()
                            catch = Image(Point(x1,700),"Catch.gif")
                            catch2 = Image(Point(x2,700),"Catch2.gif")
                            line = Line(Point(x3,610),Point(x3+175,610))
                        
                            catch2.draw(win)

                            win.update()
                        if move.upper() == "A":
                            x1 = 90
                            x2 = 90
                            x3 = 0
                            catch.undraw()
                            catch2.undraw()
                            line.undraw()
                            catch = Image(Point(x1,700),"Catch.gif")
                            catch2 = Image(Point(x2,700),"Catch2.gif")
                            line = Line(Point(x3,610),Point(x3+175,610))
                     
                            catch2.draw(win)

                            win.update()
                            
                    if x1 <= 400:
                        
                        if move == "Right":
                            x1 = x1 + 80
                            x2 = x2 + 80
                            x3 = x3 + 80
                            catch.undraw()
                            catch2.undraw()
                            line.undraw()
                            catch = Image(Point(x1,700),"Catch.gif")
                            catch2 = Image(Point(x2,700),"Catch2.gif")
                            line = Line(Point(x3,610),Point(x3+175,610))

                            catch.draw(win)

                            win.update()
                        if move.upper() == "D":
                            x1 = 400
                            x2 = 400
                            x3 = 310
                            catch.undraw()
                            catch2.undraw()
                            line.undraw()
                            catch = Image(Point(x1,700),"Catch.gif")
                            catch2 = Image(Point(x2,700),"Catch2.gif")
                            line = Line(Point(x3,610),Point(x3+175,610))

                            catch.draw(win)

                            win.update()
       

                        
                        
                   
                        
                        
                    
                    
                        
                            
                        
                    
                  
class objectFall (threading.Thread):   ## the hamburgers falling
    def __init__ (self):
        threading.Thread.__init__(self)
    def run (self):
        global posY    ## a bunch of global stuff that I dont think I even used all of
        global hit
        global x
        global lifeC
        global miss
        global regen
        global life
        global deth
        global catch
        global catch2
        global score
        global start
        while R == True:  ## helps with restarting the program
            A = True   ## this is necessary for program to restart
            time.sleep
            ct = 0.05   ## time.sleep counter
            ct2 = 0.00005    ## time.sleep counter lowerer
            hit = False
            x = [randint(50,450),randint(50,450),randint(50,500)]
            posY = [-50,-250,-450]
            posY2 = [-50, -250, -450]
            obj1 = Image(Point(x[0],posY[0]),"bigmac.gif")  ## all the objects and stuff
            obj2 = Image(Point(x[1],posY[1]),"bigmac.gif")
            obj3 = Image(Point(x[2],posY[2]),"bigmac.gif")
            obj = [obj1,obj2,obj3]
            regen = 0
            Rtext = Text(Point(460,220),regen)
            Rtext.setFill("white")
            Rtext.setSize(20)
            Rtext.draw(win)
            Stext = Text(Point(460,170),score)
            Stext.setFill("white")
            Stext.setSize(30)
            Stext.draw(win)
            for i in range (0,3):    ## draws all the objects
                    obj[i].draw(win)
          
            while deth == False:     ## makes sure your still alive
                time.sleep(2)     
                if A == False:
                    break
                
                while start == True:
                    if A == False:    ## all the "A" is just to allow the game to restart
                        break
                  
                    for i in range (0,3):    ## makes all the borgors to move down
                       
                        obj[i].move (0,10)
                        posY[i] = posY[i] + 10 
                        win.update()
                        if posY[i] == 610 and x[i] >= x3 and x[i] <= x3 + 175:    ## checks if it you caught the object
                            obj[i].undraw()
                            posY[i] = posY2[i]
                            x[i] = randint(50,450)
                            obj[i] = Image(Point(x[i],posY[i]),"bigmac.gif")               
                            obj[i].draw(win)
                            hit = True
                            Stext.undraw()
                            score = score + 1
                            Stext = Text(Point(460,170),score)
                            Stext.setFill("white")
                            Stext.setSize(30)
                            Stext.draw(win)
                            winsound.PlaySound("minecraft_hitsound.wav",winsound.SND_ASYNC)  ## minecraft hit sound 
                                
                        if posY[i] >= 800:    ## checks if you missed
                            obj[i].undraw()
                            posY[i] = posY2[i]
                            x[i] = randint(50,450)
                            obj[i] = Image(Point(x[i],posY[i]),"bigmac.gif")
                            obj[i].draw(win)
                            miss = True
                            winsound.PlaySound("Minecraft_deathsound.wav",winsound.SND_ASYNC)
                        if miss == True:  ## your life counter
                            miss = False
                            lifeC = lifeC-1
                            life[lifeC].undraw()
                            Rtext.undraw()
                            regen = 0
                            Rtext = Text(Point(460,220),regen)
                            Rtext.setFill("white")
                            Rtext.setSize(20)
                            Rtext.draw(win)
                        if hit == True:
                            
                            hit = False
                            if lifeC != 5:   ## your regen counter
                                Rtext.undraw()
                                
                                regen = regen + 1
                                Rtext = Text(Point(460,220),regen)
                                Rtext.setFill("white")
                                Rtext.setSize(20)
                                Rtext.draw(win)
                                if regen == 5:
                                    Rtext.undraw()
                                    regen = 0
                                    Rtext = Text(Point(460,220),regen)
                                    Rtext.setFill("white")
                                    Rtext.setSize(20)
                                    Rtext.draw(win)
                
                                   
                                    life[lifeC].draw(win)
                                    lifeC = lifeC + 1
                                    
                            else:     ##i dont think this is necessary but too lazy to edit
                                Rtext.undraw()
                                regen = 0
                                Rtext = Text(Point(460,220),regen)
                                Rtext.setFill("white")
                                Rtext.setSize(20)
                                Rtext.draw(win)
                                
                               
                            
                    ct = ct - ct2 ## difficulty increase

                    time.sleep(ct)
                    if ct <= 0.01:
                        ct2 = 0
                    if lifeC == 0:   ## deth screen C:<
                        
                        deth = True
                        obj[1].undraw()
                        obj[2].undraw()
                        obj[0].undraw()
                        catch.undraw()
                        catch2.undraw()
                        Rtext.undraw()
                        Stext.undraw()
                        endgame = Text(Point(250,300),("Score: ",score))
                        endgame.setFill("white")
                        endgame.setSize(30)
                        endgame.draw(win)
                        eRec = Rectangle(Point(150,350),Point(350,450))
                        eRec.setOutline("white")
                        eRec.draw(win)
                        eText = Text(Point(250,400),"Retry?")
                        eText.setSize(20)
                        eText.setFill("white")
                        eText.draw(win)
                        qRec = Rectangle(Point(150,500),Point(350,600))
                        qRec.setOutline("white")
                        qRec.draw(win)
                        qText = Text(Point(250,550),"Quit")
                        qText.setSize(20)
                        qText.setFill("white")
                        qText.draw(win)
                        while True:
                            winsound.PlaySound("Evil.wav",winsound.SND_ASYNC)  ## Deth music
                            nxt = win.getMouse()   ## end game screen
                            if nxt.getX() >= 150 and nxt.getX() <= 350 and nxt.getY() >=350 and nxt.getY() <= 450:
                                
                                regen = 0
                                ct = 0.05
                                deth = False
                                eRec.undraw()
                                qRec.undraw()
                                qText.undraw()
                                eText.undraw()
                                eRec.undraw()
                                endgame.undraw()
                                score = 0
                                lifeC = 5
                                start = True
                                A = False
                                winsound.PlaySound(None,winsound.SND_PURGE)
                                break
                            if nxt.getX() >= 150 and nxt.getX() <= 350 and nxt.getY() >=500 and nxt.getY() <= 600:
                                winsound.PlaySound(None,winsound.SND_PURGE)
                                win.close()
                                break
                                

                    
                            
                    
                    

              
              
                
                
        
        
            
            


            
##class moveCatch (threading.Thread):
##    def __init__ (self):
##        threading.Thread.__init__(self)
##    def run (self):
##        while True:
objectThread = objectFall()
objectThread.start()
startGameThread = startGame()
startGameThread.start()
startImageThread = startMove()
startImageThread.start()
introThread = intro()
introThread.start()
win.mainloop()
