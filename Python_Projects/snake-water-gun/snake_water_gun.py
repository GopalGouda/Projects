import tkinter as tk
import random

# Game values
choices = {
    "snake": 1,
    "water": -1,
    "gun": 0
}

computer_choices = {
    1: "snake",
    -1: "water",
    0: "gun"
}

# Create window
root = tk.Tk()
root.title("Snake Water Gun")
root.geometry("500x500")

# Title
title = tk.Label(
    root,
    text="🐍 Snake Water Gun 💧",
    font=("Arial", 24, "bold")
)
title.pack(pady=30)

# Result labels
user_label = tk.Label(
    root,
    text="You: -",
    font=("Arial", 16)
)
user_label.pack(pady=10)

computer_label = tk.Label(
    root,
    text="Computer: -",
    font=("Arial", 16)
)
computer_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="Choose your weapon!",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=20)


# Game function
def play(user_choice):

    computer_choice = random.choice([1, -1, 0])

    user_value = choices[user_choice]

    user_label.config(
        text=f"You: {user_choice}"
    )

    computer_label.config(
        text=f"Computer: {computer_choices[computer_choice]}"
    )

    # Draw
    if user_value == computer_choice:
        result = "Draw!"

    # User wins
    elif (
        (user_value == 1 and computer_choice == -1) or
        (user_value == -1 and computer_choice == 0) or
        (user_value == 0 and computer_choice == 1)
    ):
        result = "🎉 You Win!"

    # Computer wins
    else:
        result = "😢 You Lose!"

    result_label.config(text=result)


# Buttons
snake_button = tk.Button(
    root,
    text="🐍 Snake",
    font=("Arial", 14),
    command=lambda: play("snake")
)
snake_button.pack(pady=5)

water_button = tk.Button(
    root,
    text="💧 Water",
    font=("Arial", 14),
    command=lambda: play("water")
)
water_button.pack(pady=5)

gun_button = tk.Button(
    root,
    text="🔫 Gun",
    font=("Arial", 14),
    command=lambda: play("gun")
)
gun_button.pack(pady=5)


# Start the application
root.mainloop()