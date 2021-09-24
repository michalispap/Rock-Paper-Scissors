from tkinter import *
import tkinter as tk
import pyautogui
import random
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
#root.configure(background='black')

label = tk.Label(root,text="Welcome to Rock Paper Scissors!\n\n\nTake your pick:", fg = "blue", font = "Times 20").pack()

player_score = 0
computer_score = 0

player_score_label=Label(root,text='Player Score: ' + str(player_score), fg = "green", font = "Times 20")
player_score_label.pack()
player_score_label.place(x=150,y=100)
computer_score_label=Label(root,text='Computer Score: ' + str(computer_score), fg = "red", font = "Times 20")
computer_score_label.pack()
computer_score_label.place(x=1000,y=100)

def logic(user_action):
   possible_actions = ["rock", "paper", "scissors"]
   computer_action = random.choice(possible_actions)
   global player_score
   global computer_score

   if user_action == computer_action:
       player_score += 1
       computer_score += 1
       player_score_label["text"]='Player Score: ' + str(player_score)
       computer_score_label["text"]='Computer Score: ' + str(computer_score)
       pygame.mixer.Sound.play(tie)
       pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nBoth players selected " + user_action + ".\nIt's a tie!", title='Result', button='OK')
   elif user_action == "rock":
       if computer_action == "scissors":
          player_score += 1
          player_score_label["text"] = 'Player Score: ' + str(player_score)
          pygame.mixer.Sound.play(win)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nRock smashes scissors!\nYou win!", title='Result', button='OK')
       else:
          computer_score += 1
          computer_score_label["text"] = 'Computer Score: ' + str(computer_score)
          pygame.mixer.Sound.play(loss)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nPaper covers rock!\nYou lose.", title='Result', button='OK')
   elif user_action == "paper":
       if computer_action == "rock":
          player_score += 1
          player_score_label["text"] = 'Player Score: ' + str(player_score)
          pygame.mixer.Sound.play(win)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nPaper covers rock!\nYou win!", title='Result', button='OK')
       else:
          computer_score += 1
          computer_score_label["text"] = 'Computer Score: ' + str(computer_score)
          pygame.mixer.Sound.play(loss)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nScissors cuts paper!\nYou lose.", title='Result', button='OK')
   elif user_action == "scissors":
       if computer_action == "paper":
          player_score += 1
          player_score_label["text"] = 'Player Score: ' + str(player_score)
          pygame.mixer.Sound.play(win)
          pyautogui.alert(text = "You chose " + user_action + ", computer chose " + computer_action + ".\nScissors cuts paper!\nYou win!", title='Result', button='OK')
       else:
          computer_score += 1
          computer_score_label["text"] = 'Computer Score: ' + str(computer_score)
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
