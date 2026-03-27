#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 23:49:55 2026

@author: jamesdodds
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

##recipe data
recipes = {
    "Mince and Dumplings": ['Mince', 'Onion', 'Carrot','Garlic', 'Beef stock cube', 'Potatoes', 'Suet', 'Self raising flour'],
    "Chorizo Stew": ['Chorizo', 'Tinned Tomatoes', 'Onion', 'Garlic', 'Chillis', 'Parsley', 'Stock Cube', 'Paprika', 'Tinned Green Lentils'],
    "Mince and Yorkshires" : ['Mince', 'Onion', 'Carrot','Garlic', 'Beef stock cube', 'Potatoes', '6 Eggs', 'Plain Flour', 'Milk'],
    "Burritos" : ['Chicken', 'Hot Sauce', 'Black beans', 'Onion', 'Chillis', 'Garlic', 'Paprika', 'Cumin', 'Stock Cube', 'Rice', 'Coriander', 'Lime', 'Wraps', 'Avocado' ],
    "Spaghetti Bolognese" : ['Mince', 'Onion', 'Carrot', 'Celery','Garlic', 'Tinned Tomatoes', 'Stock cube', 'Dried Herbs', 'Milk', 'Pasta'],
    "Meatballs" : ['Meatballs', 'Onion', 'Tinned tomatoes', 'Basil', 'Stock cube', 'Pasta', 'Garlic'],
    "Chicken Karahi" : ['Chicken', 'Tomatoes', 'Garlic', 'Ginger', 'Karahi Masala', 'Green finger chillis'],
    "Honey Soy Chicken" : ['Chicken', 'Dark Soy Sauce', 'Honey', 'Garlic', 'Chillis', 'Oyster Sauce', 'Worcestershire Sauce'],
    "Thai Green Curry" : ['Green Curry Paste', 'Green Beans', 'Baby Corn', 'Chillis', 'Chicken', 'Coconut Milk', 'Garlic', 'Ginger'],
    "Bangers and Mash" : ['Sausages', 'Potatoes', 'Onions', 'Stock Cube', 'Worcestershire Sauce', 'Gravy granules'],
    "Toad in the Hole" : ['Sausages', 'Plain Flour', '6 eggs', 'Milk'],
    "Chilli con carne" : ['Mince', 'Onion', 'Kidney Beans', 'Tinned Tomatoes', 'Cumin', 'Chillis', 'Garlic'],
    "Pad Kra Pao" : ['Minced meat', 'Garlic', 'Ginger', 'Thai Basil', 'Soy Sauce', 'Oyster Sauce', 'Thai Chillis'],
    "Full English" : ['Bacon', 'Sausage', 'Eggs', 'Black Pudding', 'Haggis', 'Square Sausage', 'Hash Browns', 'Beans', 'Mushrooms', 'Tomatoes', 'Bread'],
    "Chicken and Vegetable Soup" : ['Chicken', 'Carrot', 'Parsnip', 'Potato', 'Onion', 'Leek', 'Barley', 'Vegetable Stock', 'Dried Parsley'],
    "Beef Stew" : ['Stewing Beef', 'Onions', 'Carrots', 'Potatoes', 'Turnip', 'Parsnip', 'Beef Stock'],
    "Chicken Stew" : ['Chicken', 'Leek', 'Onion', 'Potato', 'Carrot', 'Chicken Stock', 'Dried herbs'],
    "Cabbage Salad" : ['White or Sweetheart Cabbage', 'Onion', 'Spring onion', 'Garlic', 'Lemon Juice', 'Fresh Mint', 'Dried Mint', 'Sumac', 'Fresh Parsley', 'Olive Oil'],
    "Risotto" : ['Risotto Rice', 'Onion', 'Stock Cube', 'Garlic', 'Optional White Wine'],
    "Fajitas" : ['Chicken', 'Red Onions', 'Bell Peppers', 'Cumin', 'Chilli Powder', 'Hot Sauce', 'Paprika', 'Wraps', 'CHips', 'Lettuce'],
    "Baked Potatoes" : ['Baking potatoes', 'Beans', 'Cheese'],
    "Asian Cabbage Salad" : ['Red Cabbage', 'Sesame Oil', 'Olive Oil', 'Vinegar', 'Garlic', 'Ginger', 'Soy Sauce', 'Spring Onions', 'Quinoa', 'Edamame Beans', 'Red Bell Pepper', 'Chillis', 'Carrots'],
    "Tortellini" : ['Tortellini', 'Jar of Mascarpone Sauce'],
    "Tomato Pasta Sauce" : ['Bacon', 'Onions', 'Garlic', 'Chillis', 'Tinned Tomatoes', 'Stock Cube', 'Pasta'],
    "Carbonara" : ['Eggs', 'Bacon', 'Parmesan', 'Black Pepper'],
    "Lahmacun" : ['Minced Meat', 'Bell Pepper', 'Onion', 'Cumin', 'Paprika', 'Chilli Powder', 'Sumac', 'Dried Mint', 'Black Pepper', 'Lebanese flat bread', 'White or Sweetheart Cabbage', 'Spring onion', 'Lemon Juice', 'Fresh Mint', 'Fresh Parsley', 'Olive Oil'],
    "Steak Frite" : ['Steak', 'Chips', 'Peppercorn Sauce', 'Tenderstem Broccoli or Asparagus'],
    "Steak and Potatoes" : ['Steak', 'Potatoes', 'Peppercorn Sauce', 'Tenderstem Broccoli or Asparagus'],
    "Cottage Pie" : ['Mince', 'Onion', 'Carrot','Garlic', 'Beef stock cube','Frozen Peas', 'Potatoes', 'Cheese'],
    "Pork and Barley Gravy" : ['Pork Chops', 'Onions', 'Stock Cube', 'Flour', 'Worcestershire Sauce', 'Garlic', 'Potatoes', 'Marrowfat peas or Butter beans'],
    "Sausage Casserole" : ['Sausages', 'Beans', 'Stock Cube', 'Onions', 'Carrots', 'Potatoes'],
    "Chinese Chicken Curry" : ['Chinese Curry Paste', 'Onions', 'Chicken', 'Chillis', 'Garlic', 'Frozen Peas', 'Rice', 'Eggs', 'Soy Sauce'],
    "Chickpea Curry": ['Chickpeas', 'Onions', 'Garlic', 'Ginger', 'Chillis', 'Mixed Powder', 'Curry Powder', 'Turmeric', 'Chilli powder', 'Cumin Seeds', 'Mustard Seeds', 'Coriander seeds', 'Tomatoes'],
    "Lentil Pasta Sauce" : ['Lentils', 'Onions', 'Garlic', 'Tinned Tomatoes', 'Pasta', 'Stock Cube', 'Paprika', 'Chilli Powder']
    }


## shopping list generator function
def shoplistgen(choose_recipes, recipes_dict):
    shopping_list = []
    for recipe in choose_recipes:
        if recipe in recipes_dict:
            shopping_list.extend(recipes_dict[recipe])
        else:
            print(f"'{recipe}' not found")
    return shopping_list

## creating the window
window = tk.Tk()
window.title("Bollock")

##creating the frame

mainframe = ttk.Frame(window, padding=(20, 20, 20, 20))
mainframe.grid(column=0, row=0)

##creating the label and entry for the number of meals to have
ttk.Label(mainframe, text="Number of Meals:").grid(row=0, column=0, sticky="w")
num_entry = ttk.Entry(mainframe, width=5)
num_entry.grid(row=0, column=1, padx=5)

##frame for dropdowns
dropdown_frame = ttk.Frame(mainframe)
dropdown_frame.grid(row=1, column=0, columnspan=3, pady=10)

#number of dropdowns
dropdown_vars = []

def create_dropdowns(n):
    global dropdown_vars
    
    for widget in dropdown_frame.winfo_children():
        widget.destroy()
    dropdown_vars = []

    for i in range(n):
        var = tk.StringVar()
        var.set(list(recipes.keys())[0])  # default value
        dropdown = tk.OptionMenu(dropdown_frame, var, *recipes.keys())
        dropdown.grid(row=i, column=0, pady=5)
        dropdown_vars.append(var)
   
    generate_button = ttk.Button(dropdown_frame, text="Generate Shopping List", command=generate_shopping_list_file)
    generate_button.grid(row=n, column=0, pady=10)


def create_dropdowns_button():
    try:
        n = int(num_entry.get())
        if n < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer.")
        return
    create_dropdowns(n)

ttk.Button(mainframe, text="Next", command=create_dropdowns_button).grid(row=0, column=2, padx=10)

#  gen shopping list files
def generate_shopping_list_file():
    selected_recipes = [var.get() for var in dropdown_vars]
    shopping_list = shoplistgen(selected_recipes, recipes)

    today_str = datetime.today().strftime("%d %m %Y")
    filename = f"Shopping_List_{today_str.replace(' ', '_')}.txt"
    filepath = os.path.join(os.path.expanduser("~"), "Desktop", filename)

    try:
        with open(filepath, "w") as f:
            f.write(f"Shopping List for {today_str}:\n")
            for item in shopping_list:
                f.write(f"- {item}\n")
        messagebox.showinfo("Saved", f"Shopping list saved to '{filepath}'")
    except Exception as e:
        messagebox.showerror("Save Failed", f"Could not save file:\n{e}")

window.mainloop()