#

import subprocess
import os.path
import sys
import time

#-----------------------------   Package Installation   ------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
installcheck_file_path = "C:\\Users\\Public\\Documents\\install_check.txt"

def installer():
    def install_package(package_name):
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing package '{package_name}'.")

    if __name__ == "__main__":
        package_to_install = "tk"  
        install_package(package_to_install)

    if __name__ == "__main__":
        package_to_install = "pillow"  
        install_package(package_to_install)

    # if __name__ == "__main__":
    #     package_to_install = "playsound==1.2.2"  
    #     install_package(package_to_install)

    if __name__ == "__main__":
        package_to_install = "pygame"  
        install_package(package_to_install)

    try:
        with open(installcheck_file_path, 'x') as file:
         print(f"{installcheck_file_path} created successfully.")
    except FileExistsError:
        print(f"{installcheck_file_path} already exists.")



if os.path.isfile(installcheck_file_path):
    print(f"{installcheck_file_path} exists.")
else:
    print(f"{installcheck_file_path} does not exist. Creating...")
    installer()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#----------------------------   Importing fresh packages   ----------------------------------------------------
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
# from playsound import playsound
import pygame
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#------------------------------------   Global functions   ---------------------------------------------------
def resize_image(image, new_width):
    current_width = image.size[0]
    current_height = image.size[1]

    new_height = int((new_width / current_width) * current_height)
    image = image.resize((new_width, new_height))
    return image

dis_token=[]
adv_token=[]
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#---------------------------------   Stories   -------------------------------------
A_death="""YOU DIED!"""


A_stories=[
    " ",
    """While on your way to your parents' house in southern Florida for Thanksgiving,
      you have run out of gas.Your GPS hasn't been working for a while now,
        and you end up right outside of the main gate for a town called 'Lost',
    You need help getting back on the road and it's starting to get cold.
      But something about this place feels... off.""",

      """After a few hours, the car has reached very uncomfortably cold temperatures.
      You feel that the only reasonable thing to do at this point is to head into town.""",

      """You look around as you enter the town of Lost, all around you lies a dark,
      impenetrable swampland. The only notable structures in sight are a small, 
      dinghy police station, a drab looking town hall, and around 20 small cabins 
      scattered haphazardly about. The sun has already begun to rise over the horizon
      and you notice several dirty-looking townspeople giving you ugly looks.""",

      """You knock hestitantly on the closed window at the front of the police station.
      An angry, dirty police officer peers out of the window, glaring at you.
      'What do you think you're doing here son?' You take a step back in surprise.
      You quickly and nervously explain why you're there, but it's clear that the 
      officer isn't listening. With a final cold stare, he proclaims: 'If I see you
      ever again, I will kill you.' With that he slams the window shut and walks away.""",

      """You begin to question your decision the moment you step into the nasty-looking
      water that surrounds the nearest cabin. The door swings open moments after you've
      finished knocking on it. A dirty-looking man, kneeling and hunched over looks up at you.
      'We don't like visitors here, you should leave before... *cough*' Panicked, you ask:
      'Before what?' A sly grin appears on the man's face, and is soon replaced with a grimace.
      'Before the Smiler finds you.' You, being quite alarmed by this little man, turn and leave.""",

      """As you walk into the town hall, you are shocked by how much nicer and cleaner everything
      looks compared to the rest of the town. A man in a suit and tie, sitting at a desk at the back
      of the room greets you warmly saying: 'It's been so long since we've had visitors around here!'
      He tells you that the mayor is very busy at the moment, but will be able to meet with you if
      you're patient and wait. After what you've seen outside, sitting in the waiting area doesn't
      sound like a bad idea.""",

      """After about 10 hours of waiting, your phone battery has died completely from playing angry
      birds. You are just getting ready to stand up and leave, when a cheeful and portly figure
      calls you into his office: the mayor! Once you step inside, he shakes your hand and asks
       you what brings you to his town. You explain your situation and he hands you
      an empty gas container. 'There's an old gas pump out in the forest, You can go fill this
      up. It should be just enough to make it to the nearest gas station. Just be sure not to go
      out there at night.'""",

      """The mayor cheerfully wishes you the best of luck as you walk out of the town hall with
      the gas can. You, wanting to leave the town as soon as possible, begin walking toward the
      treeline. As you walk, you notice a general sense of fear and forboding througout the town.
      You see panicked mothers urgently gathering their children inside and locking their doors.
      Soon, there isn't anybody left in sight, other than a couple of police officers loading large
      guns. You decide that it might be a good idea to bring some sort of weapon along, just in 
      case. Looking around, you spot three viable options: a knife, a shovel, and a lighter with
    some cloth. Which do you chose to bring with you?""",

    """'That's okay.' The mayor says, clearly dissapointed. 'Here's the gas can anyway, in case you
    change your mind.' You decide to take a walk in the town to clear your head and think of another
    solution. to your dismay, there isn't anybody in sight. Suddenly, you hear a strange sound
      from behind...""",

      """As you walk through the forest, everything around you begins to grow darker. Shivers of
      fear run down your spine as strange and menacing sounds echo throughout the forest around
      you. You feel that someone, or something is hunting you.""",

      """After a couple of hours of walking through the forest, the gas pump is in sight!
      You're flooded with a sense of relief upon seeing it, and begin to quickly walk towards it.
      As you draw closer, you notice a dark figure approaching. Terror stuns your senses and you drop
      the empty gas can. Your grip tightens around your weapon, and you prepare for action.""",

      """Using your cloth and lighter, you successfully light the creature ablaze! A horrendous
      sound emenates from the creature as it burns. You turn and run as fast as you possibly can,
      through the forest and past the town towards your car.""",
      
      """Filled with panic, you turn and run, leaving the empty gas can on the ground behind you.
      You can hear the creature following close behind, its footsteps making wet sounds in the mud
      behind you. You can feel it gaining on you as your stamina begins to wear thin. You're 
      surrounded by water and trees and you begin to wonder if running is the best option for escape.""",

      """After arriving at your car, you notice a note taped to your windshield. You quickly grab it
      as you lunge into the car and lock the doors. the note is from the mayor and says that he was able
      to find some spare gas in a storage closet and refueled your car for you. You are flooded with a 
      sense of relief and start your engine. You successfully drive away from Lost, never to return again.
                                                 YOU ESCAPED!""",
    
    """The treeline is just in sight now, but the Smiler isn't far behind. Just beyond the trees, you can see
    three police officers pointing their guns in your general direction. You feel a cold, painful grip take hold
    of your shoulder just as you make it out of the forest. You hear the sounds of gunfire as the officers shoot
    the creature, repelling it back into the swamp. 'You're safe now.' one of the officers says. You quickly rush out
    of the town and go to your car to think.""",

    """The treeline is just in sight now, but the Smiler isn't far behind. Just beyond the trees, you can see
    three police officers pointing their guns in your general direction. You feel a cold, painful grip take hold
    of your shoulder just as you make it out of the forest. 'I told you I'd kill ya if I ever saw you again!' one of
    the officers shouts. The officer takes aim and fires, shooting you in the chest. You fall to the ground, the last thing
    you see being the Smiler, as it drags you back into the swamp."""
]

#-------------------------------- SwampSmiler -----------------------------------
#////////////////////////////////////////////////////////////////////////////////////////////////////
def SwampDeath():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("855x880")
    root.minsize(855,880)
    root.maxsize(855,880)

    death_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\SwampSmiler.png") 
    death_image1 = resize_image(death_image1, 800) 
    death_image1 = ImageTk.PhotoImage(death_image1) 
    death_label_image1 = tk.Label(image=death_image1) 
    death_label_image1.grid(row=2,column=3)

    death_story=tk.Label(root, font=("impact",30), fg="black", bg="silver", text=A_death)
    death_story.grid(row=3,column=3) 

    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\Public\\Documents\\Symulcrum assets\\SwampSmiler sound.WAV")
    pygame.mixer.music.play()

    root.mainloop()
#///////////////////////////////////////////////////////////////////////////////////////////////////
def SwampEscape():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("950x800")
    root.minsize(950,800)
    root.maxsize(950,800)

    A14_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\escape.png") 
    A14_image1 = resize_image(A14_image1, 613) 
    A14_image1 = ImageTk.PhotoImage(A14_image1) 
    A14_label_image1 = tk.Label(image=A14_image1) 
    A14_label_image1.grid(row=2,column=3)

    A14_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[14])
    A14_story.grid(row=3,column=3)

    root.mainloop()
#///////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA14():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("1000x800")
    root.minsize(1000,800)
    root.maxsize(1000,800)

    A14_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A14 image.png") 
    A14_image1 = resize_image(A14_image1, 613) 
    A14_image1 = ImageTk.PhotoImage(A14_image1) 
    A14_label_image1 = tk.Label(image=A14_image1) 
    A14_label_image1.grid(row=2,column=3)

    betrayal=len(dis_token)
    if betrayal>0:
        A14_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[16])
        A14_story.grid(row=3,column=3)
    else:
        A14_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[15])
        A14_story.grid(row=3,column=3)
    
    def escort():
        if betrayal>0:
            print("betrayed")
            root.destroy()
            time.sleep(0.2)
            SwampDeath()
        else:
            print("escaped")
            root.destroy()
            time.sleep(0.2)
            SwampEscape()

    Next_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Next", command=lambda: escort())
    Next_button.grid(row=4, column=3)
    
    root.mainloop()
#///////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA13():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("1220x800")
    root.minsize(1220,800)
    root.maxsize(1220,800)

    A13_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A13 image.png") 
    A13_image1 = resize_image(A13_image1, 613) 
    A13_image1 = ImageTk.PhotoImage(A13_image1) 
    A13_label_image1 = tk.Label(image=A13_image1) 
    A13_label_image1.grid(row=2,column=3)

    A13_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[13])
    A13_story.grid(row=3,column=3)

    def escape_plan(checky):
        if (checky=="climb") or (checky=="swim"):
            root.destroy()
            time.sleep(0.2)
            SwampDeath()
        elif checky=="run":
            root.destroy()
            time.sleep(0.2)
            SwampSmilerA14()


    climb_tree=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Climb a tree", command=lambda: escape_plan("climb"))
    climb_tree.grid(row=4, column=2)

    keep_running=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Keep running", command=lambda: escape_plan("run"))
    keep_running.grid(row=4, column=3)

    swim=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="""Swim away""", command=lambda: escape_plan("swim"))
    swim.grid(row=4, column=4)

    root.mainloop()


#//////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA12():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("800x800")
    root.minsize(800,800)
    root.maxsize(800,800)

    A12_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A12 image.png") 
    A12_image1 = resize_image(A12_image1, 613) 
    A12_image1 = ImageTk.PhotoImage(A12_image1) 
    A12_label_image1 = tk.Label(image=A12_image1) 
    A12_label_image1.grid(row=2,column=3)

    A12_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[12])
    A12_story.grid(row=3,column=3)

    def proceed():
        root.destroy()
        time.sleep(0.2)
        SwampEscape()

    continue_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Continue", command=lambda: proceed())
    continue_button.grid(row=4, column=3)

    root.mainloop()
#//////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA11():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("1075x800")
    root.minsize(1075,800)
    root.maxsize(1075,800)

    A11_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A11 image.png") 
    A11_image1 = resize_image(A11_image1, 613) 
    A11_image1 = ImageTk.PhotoImage(A11_image1) 
    A11_label_image1 = tk.Label(image=A11_image1) 
    A11_label_image1.grid(row=2,column=3)

    A11_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[11])
    A11_story.grid(row=3,column=3)

    def action(thinger):
        root.destroy()
        time.sleep(0.2)
        is_firey=len(adv_token)
        if thinger=="hide":
            SwampDeath()
        elif (thinger=="attack") and (is_firey>0):
            SwampSmilerA12()
        elif thinger=="run":
            SwampSmilerA13()
        elif thinger=="attack":
            SwampSmilerA13()


    hide_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Hide", command=lambda: action("hide"))
    hide_button.grid(row=4, column=2)

    Attack_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Attack and run", command=lambda: action("attack"))
    Attack_button.grid(row=4, column=3)

    Run_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="""Just run""", command=lambda: action("run"))
    Run_button.grid(row=4, column=4)

    root.mainloop()
#//////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA10():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("1075x750")
    root.minsize(1075,750)
    root.maxsize(1075,750)

    A10_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A10 image.png") 
    A10_image1 = resize_image(A10_image1, 613) 
    A10_image1 = ImageTk.PhotoImage(A10_image1) 
    A10_label_image1 = tk.Label(image=A10_image1) 
    A10_label_image1.grid(row=2,column=3)

    def movement(check):
        root.destroy()
        time.sleep(0.2)
        if check=="hide":
            SwampDeath()
        elif check=="sneak":
            SwampDeath()
        elif check=="walk":
            print("good choice...")
            SwampSmilerA11()

    A10_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[10])
    A10_story.grid(row=3,column=3)

    hide_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Hide", command=lambda: movement("hide"))
    hide_button.grid(row=4, column=2)

    Sneak_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Sneak", command=lambda: movement("sneak"))
    Sneak_button.grid(row=4, column=3)

    Continue_button=tk.Button(root, font=("helvetica",18), fg="black", bg="silver", text="""Keep moving""", command=lambda: movement("walk"))
    Continue_button.grid(row=4, column=4)

    root.mainloop() 
#//////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA9():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("985x835")
    root.minsize(985,835)
    root.maxsize(985,835)

    A9_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A9 image.png") 
    A9_image1 = resize_image(A9_image1, 613) 
    A9_image1 = ImageTk.PhotoImage(A9_image1) 
    A9_label_image1 = tk.Label(image=A9_image1) 
    A9_label_image1.grid(row=2,column=3)

    A9_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[9])
    A9_story.grid(row=3,column=3)    

    def next_cmd():
            root.destroy()
            time.sleep(0.2)
            pygame.mixer.music.stop()
            SwampDeath()

    next_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="next", command=lambda:next_cmd())
    next_button.grid(row=4, column=3)

    root.mainloop()
#/////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA8():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("1000x950")
    root.minsize(1000,950)
    root.maxsize(1000,950)

    A8_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A8 image.png") 
    A8_image1 = resize_image(A8_image1, 613) 
    A8_image1 = ImageTk.PhotoImage(A8_image1) 
    A8_label_image1 = tk.Label(image=A8_image1) 
    A8_label_image1.grid(row=2,column=3)

    def weaponschoice(funny):
        root.destroy()
        time.sleep(0.2)
        if (funny=="knife")or(funny=="shovel"):
            print("useless weapon...")
        elif funny=="fire":
            print("good choice...")
            adv_token.append(funny)
        SwampSmilerA10()

    pygame.mixer.music.stop()
    time.sleep(0.2)
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\Public\\Documents\\Symulcrum assets\\Intense swamp.WAV")
    pygame.mixer.music.play()

    A8_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[8])
    A8_story.grid(row=3,column=3)

    choose_knife=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Knife", command=lambda:weaponschoice("knife"))
    choose_knife.grid(row=4, column=2)

    choose_shovel=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Shovel", command=lambda:weaponschoice("shovel"))
    choose_shovel.grid(row=4, column=3)

    choose_fire=tk.Button(root, font=("helvetica",18), fg="black", bg="silver", text="""Lighter
and fabric""", command=lambda:weaponschoice("fire"))
    choose_fire.grid(row=4, column=4)

    root.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA7():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("985x835")
    root.minsize(985,835)
    root.maxsize(985,835)

    A7_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A7 image.png") 
    A7_image1 = resize_image(A7_image1, 613) 
    A7_image1 = ImageTk.PhotoImage(A7_image1) 
    A7_label_image1 = tk.Label(image=A7_image1) 
    A7_label_image1.grid(row=2,column=3)

    A7_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[7])
    A7_story.grid(row=3,column=3)

    def mayor_choice(check):
        if check=="yes":
            print("accepted")
            root.destroy()
            time.sleep(0.2)
            SwampSmilerA8()
        elif check=="no":
            print("denied")
            root.destroy()
            time.sleep(0.2)
            # pygame.mixer.music.stop()
            SwampSmilerA9()

    accept_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="accept", command=lambda: mayor_choice("yes"))
    accept_button.grid(row=4, column=2)

    Deny_button=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="deny", command=lambda: mayor_choice("no"))
    Deny_button.grid(row=4, column=4)

    root.mainloop()

#/////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA6():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("825x815")
    root.minsize(825,815)
    root.maxsize(825,815)

    A6_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A6 image.png") 
    A6_image1 = resize_image(A6_image1, 613) 
    A6_image1 = ImageTk.PhotoImage(A6_image1) 
    A6_label_image1 = tk.Label(image=A6_image1) 
    A6_label_image1.grid(row=2,column=3)

    A6_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[6])
    A6_story.grid(row=3,column=3)

    def wait_for_mayor_cmd():
        time.sleep(5)
        root.destroy()
        time.sleep(0.2)
        SwampSmilerA7()


    wait_for_mayor=tk.Button(root, font=("helvetica",20), fg="black", bg="silver", text="Wait", command=lambda: wait_for_mayor_cmd())
    wait_for_mayor.grid(row=4, column=3)

    root.mainloop()

#/////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA5():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("900x800")
    root.minsize(900,800)
    root.maxsize(900,800)

    A5_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A5 image.png") 
    A5_image1 = resize_image(A5_image1, 613) 
    A5_image1 = ImageTk.PhotoImage(A5_image1) 
    A5_label_image1 = tk.Label(image=A5_image1) 
    A5_label_image1.grid(row=2,column=3)

    def go_to_town_cmd():
        root.destroy()
        time.sleep(0.2)
        SwampSmilerA3() 

    go_to_town=tk.Button(root, font=("helvetica",18), fg="midnightblue", bg="gray", text="Return to town", command=lambda: go_to_town_cmd())
    go_to_town.grid(row=4, column=3)

    A5_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[5])
    A5_story.grid(row=3,column=3)

    root.mainloop()
#//////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA4():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("677x800")
    root.minsize(677,800)
    root.maxsize(677,800)

    A4_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A4 image.png") 
    A4_image1 = resize_image(A4_image1, 613) 
    A4_image1 = ImageTk.PhotoImage(A4_image1) 
    A4_label_image1 = tk.Label(image=A4_image1) 
    A4_label_image1.grid(row=2,column=3)

    def go_to_town_cmd():
        root.destroy()
        time.sleep(0.2)
        SwampSmilerA3() 

    go_to_town=tk.Button(root, font=("helvetica",18), fg="midnightblue", bg="gray", text="Return to town", command=lambda: go_to_town_cmd())
    go_to_town.grid(row=4, column=3)

    A4_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[4])
    A4_story.grid(row=3,column=3)

    root.mainloop()
#//////////////////////////////////////////////////////////////////////////////////////////////////
def SwampSmilerA3():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("985x800")
    root.minsize(985,800)
    root.maxsize(985,800)

    A3_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A3 image.png") 
    A3_image1 = resize_image(A3_image1, 613) 
    A3_image1 = ImageTk.PhotoImage(A3_image1) 
    A3_label_image1 = tk.Label(image=A3_image1) 
    A3_label_image1.grid(row=2,column=3)

    A3_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[3])
    A3_story.grid(row=3,column=3)

    def A3_cmd(WR):
        root.destroy()
        time.sleep(0.2)
        if WR=="police":
            dis_token.append(WR) 
            SwampSmilerA4()
        elif WR=="doors":
            SwampSmilerA5()
        elif WR=="town hall":
            SwampSmilerA6()
        
        

    police_station=tk.Button(root, font=("helvetica",13), fg="black", bg="silver", text="Go to Police station", command=lambda:A3_cmd("police"))
    police_station.grid(row=4, column=2)

    knock_doors=tk.Button(root, font=("helvetica",13), fg="black", bg="silver", text="Knock on cabin doors", command=lambda: A3_cmd("doors"))
    knock_doors.grid(row=4, column=3)

    town_hall=tk.Button(root, font=("helvetica",13), fg="black", bg="silver", text="Enter Town hall", command=lambda: A3_cmd("town hall"))
    town_hall.grid(row=4, column=4)

    root.mainloop()


#///////////////////////////////////////////////////
def SwampSmilerA2():
    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("670x800")
    root.minsize(670,800)
    root.maxsize(670,800)

    A2_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A2 image.png") 
    A2_image1 = resize_image(A2_image1, 613) 
    A2_image1 = ImageTk.PhotoImage(A2_image1) 
    A2_label_image1 = tk.Label(image=A2_image1) 
    A2_label_image1.grid(row=2,column=3)

    def go_to_town_cmd():
        root.destroy()
        time.sleep(0.2)
        SwampSmilerA3() 

    go_to_town=tk.Button(root, font=("helvetica",18), fg="midnightblue", bg="gray", text="Go into town", command=lambda: go_to_town_cmd())
    go_to_town.grid(row=4, column=3)

    A2_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[2])
    A2_story.grid(row=3,column=3)

    root.mainloop()
#//////////////////////////////////////////////////
def SwampSmilerA1():
    print("SwampSmiler")

    root=tk.Tk()
    root.title("Lost, Florida")
    root.geometry("945x800")
    root.minsize(945,800)
    root.maxsize(945,800)

    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost theme.WAV")
    pygame.mixer.music.play(-1)

    Intro_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Lost A\\A1 image.png") 
    Intro_image1 = resize_image(Intro_image1, 613) 
    Intro_image1 = ImageTk.PhotoImage(Intro_image1) 
    Intro_label_image1 = tk.Label(image=Intro_image1) 
    Intro_label_image1.grid(row=2,column=3)

    def wait_button_cmd():
        root.destroy()
        time.sleep(0.2)
        SwampSmilerA2()

    def go_to_town_cmd():
        root.destroy()
        time.sleep(0.2)
        SwampSmilerA3() 

    go_to_town=tk.Button(root, font=("helvetica",18), fg="midnightblue", bg="gray", text="Go into town", command=lambda: go_to_town_cmd())
    go_to_town.grid(row=4, column=2)

    wait_button=tk.Button(root, font=("helvetica",18), fg="midnightblue", bg="gray", text="Wait in car", command=lambda: wait_button_cmd())
    wait_button.grid(row=4,column=4)

    A1_story=tk.Label(root, font=("helvetica",14), fg="black", bg="silver", text=A_stories[1])
    A1_story.grid(row=3,column=3)

    root.mainloop()

# pygame.mixer.music.stop()  Reminder of how to stop the audio
#------------------------------------   Initial menu   ----------------------------------------------------------

def mainmenu():
    root=tk.Tk()
    root.title("Symulcrum Menu")
    root.geometry("1375x750")
    root.minsize(1375,750)
    root.maxsize(1375,750)
    
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\Public\\Documents\\Symulcrum assets\\Main menu music.WAV")
    pygame.mixer.music.play(-1)

    menu_image1 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Main menu image.png") 
    menu_image1 = resize_image(menu_image1, 450) 
    menu_image1 = ImageTk.PhotoImage(menu_image1) 
    menu_label_image1 = tk.Label(image=menu_image1) 
    menu_label_image1.grid(row=2,column=3)

    menu_image2 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Main menu image 2.png") 
    menu_image2 = resize_image(menu_image2, 450) 
    menu_image2 = ImageTk.PhotoImage(menu_image2) 
    menu_label_image2 = tk.Label(image=menu_image2) 
    menu_label_image2.grid(row=2,column=2)

    menu_image3 = Image.open(f"C:\\Users\\Public\\Documents\\Symulcrum assets\\Main menu image 3.png") 
    menu_image3 = resize_image(menu_image3, 450) 
    menu_image3 = ImageTk.PhotoImage(menu_image3) 
    menu_label_image3 = tk.Label(image=menu_image3) 
    menu_label_image3.grid(row=2,column=4)

    Creditsimage1 = Image.open("C:\\Users\\Public\Documents\\Symulcrum assets\\credits icon.jpg") 
    Creditsimage1 = resize_image(Creditsimage1, 60) 
    Creditsimage1 = ImageTk.PhotoImage(Creditsimage1) 
    Credits_label_image1 = tk.Label(image=Creditsimage1) 
    Credits_label_image1.grid(row=1,column=4)
    Credits_clicky1=tk.Button(root, image=Creditsimage1,)
    Credits_clicky1.grid(row=1,column=4)

    instructions=tk.Label(root,font=("helvetica",25), fg="black", bg="silver", text="Select your story:")
    instructions.grid(row=3, column=3)

    main_header=tk.Label(root,font=("trebuchet ms",40), fg="red", bg="black", text="Symulcrum",width=15)
    main_header.grid(row=1, column=3)

    spaceholder=tk.Label(root, font=("arial",25))
    spaceholder.grid(row=4, column=3)

    def swampsmiler_button_press():
        root.destroy()
        time.sleep(0.2)
        pygame.mixer.music.stop()
        SwampSmilerA1()

    swampsmiler_button=tk.Button(root, font=("impact",24), fg="silver", bg="midnightblue", text="Lost, Florida", command=lambda: swampsmiler_button_press())
    swampsmiler_button.grid(row=5, column=3)

    wasatch_stalker_button=tk.Button(root, font=("trebuchet ms", 24), text="Coming soon!", fg="red", bg="darkgray")
    wasatch_stalker_button.grid(row=5, column=4)

    xenos_button=tk.Button(root, font=("comic sans",24), fg="lightgreen", bg="black", text="Coming soon!")
    xenos_button.grid(row=5, column=2)


    root.mainloop()

mainmenu()