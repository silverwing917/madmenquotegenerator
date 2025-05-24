#This is a random quote generator using quotes from the TV show 'Mad Men

import tkinter as tk
import random

# Step 1: Create the list of quotes

quotes = [
    "This is America. Pick a job and become the person who does it." ,
    "People want to be told what to do so badly that they'll listen to anyone.",
    "I should have known it was near the end. Every time an old man starts talking about Napoleon, you know they're going to die",
    "I don't know if anybody's ever told you that half the time this business comes down to, 'I don't like that guy'.",
    "Just think about it deeply, then forget it, and an idea will jump up in your face.",
    "Just cash the cheques, you're going to die one day.",
    "One never knows how loyalty is born.",
    "I hate to break it to you, but there is no big lie. There is no system. The Universe is indifferent.",
    "Is that what you want, or is that what people expect of you",
    "Fear stimulates my imagination ",
    "Change is neither good nor bad. It simplpy is.",
    "Don't wake me up and throw your failures in my face.",
    "Well you know that they say about Detroit. It's all fun and games until they shoot you in the face.",
    "Sometimes we don't get to choose where our talents lie.",
    "If you don't like what's being said, change the conversation",
    "Dying doesn't make you whole. You should see what you look like.",




]



 #Function to display random quote

def display_random_quote():
     random_quote = random.choice(quotes)
     quote_label.config(text=random_quote)

#Create the main window
root = tk.Tk()
root.title("Random 'Madmen' quote generator")
root.geometry("500x300")
root.resizable(False, False)

# Add a label to display the quote
quote_label = tk.Label(root, text="Click the button to get inspired!", wraplength=400, font=("Helvetica", 12), bg="lightblue")
quote_label.pack(pady=50)

# Add a button to generate a random quote
generate_button = tk.Button(root, text="Generate Quote", 
command=display_random_quote, font=("Helvetica",12), bg="lightblue")
generate_button.pack(pady=20)

#Run the application
root.mainloop()