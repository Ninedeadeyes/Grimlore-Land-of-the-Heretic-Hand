import winsound
import time
from animation import intro_animation

def Intro():
    winsound.PlaySound(".\\music\\intro.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
    intro_animation()   
    time.sleep(1)
    input("Press enter to begin your struggle")
    print("\033c", end="")


    print ("""


            dd                                                                                      
            MM                                                                                      
          hhMMhh                                                                                    
        hh::MM::hh                                                                                  
      yy//  MM  //yy                                                                                
      //  yyMMyy  //                                                                                
        yy//MM//yy                                                                                  
      yy//  MM  //yy                                                                                
    ss++    MM    ++ss                                                                              
    ++    ssMMss    ++                                                                              
        ss++MM++ss            ssssssssssssssss                                                      
      ss++  MM  ++ss        ss++++++++++++++++ss                                                    
    oooo    MM    oooo    oooo                oooo                                                  
    oo    ooMMoo    oo    MM      oooooooo      MM                                                  
        ooooMMoooo        MM                    MM                                                  
      ++ss  MM  ss++      MM    ++++++++++++    MM                                                  
    ++ss    MM    ss++    MM                    MM                                                  
  ++ss      MM      ss++  MM      ++++++++      MM                                                  
  ss        MM        ss  MM      ssssssss      MM                                                  
            MM            MM                    MM                                                  
            MM            MM    yyyyyyyyyyyy    MM            ////////////////                      
            MM            MM                    MM          //yyyyyyyyyyyyyyyy//                    
            MM            MM                    MM        //yy                yy//                  
::::::::::::MM::::::::::::MM                    MM::::::::MM::::::::::::::::::::MM::::::            
hhhhhhhhhhhhhhhhhhhhhhhhhhhh                    hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh    

""")

    
    print("A hand reaches out from a shallow grave...")
    time.sleep(1.5)
    print("That hand is yours.. You gasp for air as you free yourself")
    print("The only thing you can remember is your name")
    name=input("Your name:")
    if name =="":
        name=("Nameless")
        print("Alas, your memory betrays you")
        print("You see a wood sign pointing south east label 'Beggar's Hole' ")
        time.sleep(1)
        print("Maybe you will find some answers there or at least a safe place to sleep")
        print("                                                            ")
        input("Press enter to continue your struggle")

    

    else:
        
        print("You think it is",name)
        print("You see a wood sign pointing south east label 'Beggar's Hole' ")
        time.sleep(1)
        print("Maybe you will find some answers there or at least a safe place to sleep")
        print("                                                            ")
        input("Press enter to continue your struggle")

    winsound.PlaySound(None,  winsound.SND_ALIAS)

    return name

