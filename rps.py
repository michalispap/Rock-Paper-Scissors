from tkinter import *
import tkinter as tk
import pyautogui
import random
import time
import os #optional
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #optional
import pygame

pygame.init()
pygame.mixer.init()

win = pygame.mixer.Sound("win.mp3")
loss = pygame.mixer.Sound("loss.mp3")
tie = pygame.mixer.Sound("tie.mp3")

root = tk.Tk()
root.withdraw()

root = Toplevel()
root.title("Rock Paper Scissors")
root.geometry("1300x700")

label = tk.Label(root,text="Welcome to Rock Paper Scissors!\n\n\nTake your pick:", fg = "blue", font = "Times 20").pack()

def logic(user_action):
   possible_actions = ["rock", "paper", "scissors"]
   computer_action = random.choice(possible_actions)

   if user_action == computer_action:
       pygame.mixer.Sound.play(tie)
       pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nBoth players selected " + user_action + ".\nIt's a tie!", title='Result', button='OK')
   elif user_action == "rock":
       if computer_action == "scissors":
          pygame.mixer.Sound.play(win)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nRock smashes scissors!\nYou win!", title='Result', button='OK')
       else:
          pygame.mixer.Sound.play(loss)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nPaper covers rock!\nYou lose.", title='Result', button='OK')
   elif user_action == "paper":
       if computer_action == "rock":
          pygame.mixer.Sound.play(win)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nPaper covers rock!\nYou win!", title='Result', button='OK')
       else:
          pygame.mixer.Sound.play(loss)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nScissors cuts paper!\nYou lose.", title='Result', button='OK')
   elif user_action == "scissors":
       if computer_action == "paper":
          pygame.mixer.Sound.play(win)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nScissors cuts paper!\nYou win!", title='Result', button='OK')
       else:
          pygame.mixer.Sound.play(loss)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nRock smashes scissors!\nYou lose.", title='Result', button='OK')
   
rock_button= PhotoImage(file='rock.png')
paper_button= PhotoImage(file='paper.png')
scissors_button= PhotoImage(file='scissors.png')

button_rock = Button(root, image = rock_button, command = lambda: logic("rock"), highlightthickness = 0, bd = 0)
button_paper = Button(root, image = paper_button, command = lambda: logic("paper"), highlightthickness = 0, bd = 0)
button_scissors = Button(root, image = scissors_button, command = lambda: logic("scissors"), highlightthickness = 0, bd = 0)

button_rock.pack(side = LEFT)
button_paper.pack(side = LEFT)
button_scissors.pack(side = LEFT)

root.mainloop()
