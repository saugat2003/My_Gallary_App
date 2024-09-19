'''Student Name : Saugat Bhattarai
   Student ID   : W##########
   Programming Coursework Gallary App 
'''
# Import necessary modules
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import shutil
import os

# Global variables section - add variables that are required

path = 'images/' # folder that has all the images

# Define themes for the application
THEME1 = {
    'bg': '#b2dfed',       # Background color
    'button_bg': 'blue',   # Button background color
    'button_fg': 'red'     # Button foreground color
}

THEME2 = {
    'bg': 'black',         # Background color
    'button_bg': 'white',  # Button background color
    'button_fg': 'black'   # Button foreground color
}

# Set the initial theme
current_theme = THEME1

# Function to change to dark theme
def change_to_dark_theme():
    global current_theme
    # Ask for confirmation before changing theme
    check = messagebox.askyesno(title="Change Theme", message="Are you sure you want to change the theme?")
    if check:
        # Toggle the theme
        if current_theme == THEME1:
            current_theme = THEME2
        else:
            current_theme = THEME1
        # Update the main window and button colors based on the current theme
        myApp.configure(bg=current_theme['bg'])
        # Button.configure(bg=current_theme['button_bg'], fg=current_theme['button_fg'])
         # Update the main window, button colors, and bodyFrame background based on the current theme
        bodyFrame['background'] = current_theme['bg']   # Update bodyFrame background color

# List to store image buttons
imageButtonList = []

# Function to display a friend's friends
def showFriendFriends(head, count): 

    # '''This function shows friend's friends images and their names if they exist.'''
    # # Deactivate the "Delete Friends" button
    # ButtonDeleteFriends.configure(state=DISABLED)
    # rest of the function code...


    '''this function show friend friends image and their name if exist '''
    print(f"show friend friends in column {count}")
    friendFolderPath = path + head # Full path of friend friends
    print(friendFolderPath)
    friend = head +"'s" # Friend's name to add in remove button
    row = 2
    
    # Check if friend friends are already displayed
    if bodyFrame.grid_slaves(row=row, column=count):
        messagebox.showinfo("Information",f"{friend} friends are already displayed!")
        return
    
    if os.path.isdir(friendFolderPath): # Check if images exist in friend's friend folder
        if os.listdir(friendFolderPath): # Check if files exist
            for file in os.listdir(friendFolderPath):
                print(file,"line 34")
                (head,tail)= os.path.splitext(file)
                print(f"head is {head}, tail is {tail} line 39")
                if tail.lower() not in [".png",".jpg"]:
                    continue
                fullPath = friendFolderPath + "/" + file
                print(fullPath)
                print(row)
                friendPhoto = PhotoImage(file=fullPath)
                friendPhoto = friendPhoto.subsample(3,3)
                FriendsLabel = ttk.Label(bodyFrame, image=friendPhoto)
                FriendsLabel.image = friendPhoto
                FriendsLabel.grid(row=row, column=count)
                friendFreindsNameButton = ttk.Label(bodyFrame, text=head, style='friendFreindsName.TLabel', anchor='center')
                friendFreindsNameButton.grid(row=row+1, column=count)
                row = row + 2
            clearFriendFriendsButton = ttk.Button(bodyFrame, text=f"Remove\n{friend}\nfriends", style='clearFriendFriendsButton.TButton', command=lambda:clearFriendFriends(count))
            clearFriendFriendsButton.grid(row=row, column=count)
        else:
            messagebox.showinfo("No Images Found",f"Friends folder does exist for {friend} but no image in the folder")
    else:
        messagebox.showinfo("No Folder",f"Friends folder does not exist for {friend}")

# Function to display friends
def showFriends():
    print("show friends clicked")
    showFrame()
    ButtonShowFriends.configure(state=DISABLED)
    ButtonClearAll.configure(state=NORMAL)
    processPath()

# Function to process the path and display images
def processPath():
    global path
    if os.path.exists(path):
        print("path exist") 
        if os.path.isdir(path):
            print("its a dirctory")
            count =0 # keep track how many image files are dealt with
            for file in os.listdir(path):
                print(file)
                (head, tail)= os.path.splitext(file)
                print(f"head is {head}, tail is {tail}")
                
                if tail.lower() not in  [".png",".jpg"]:
                    continue 
                print(file)  
                count += 1
                print(f"number of images is {count}") # 6 images 
                displayImage(file, count)
        else:
            print("path exist but no folders") 
            messagebox.showinfo("Folder Information","Path exists but has no folder")    
    else:
        print("not path") 
        messagebox.showinfo("Path Information","Path does not exists")

# Function to display an image
def displayImage(item, count):
    column = count * 2
    print(f"number of column is {column} in line 89")
    (head, tail) = os.path.splitext(item)
    print(head)
    print(tail)
    
    # itemLoc = path + item # photoTmage need full path
    itemLoc = os.path.join(path, item) # Using os.path.join for creating paths
    print(itemLoc)
    photo = PhotoImage(file=itemLoc)
    photo = photo.subsample(2,2) # Reduce size of image
    print(photo)
    
    buttonName = head + "'s friends"
    imageButtons = ttk.Button(bodyFrame, image=photo, command=lambda:showFriendFriends(head, column-2))
    imageButtons.image = photo
    imageButtons.grid(row=0, column=column-2)
    imageButtonList.append((buttonName, item))
    friendsName = ttk.Button(bodyFrame, text=buttonName.capitalize(), style='friendName.TButton', command=lambda:friendButton(head, column-2))
    friendsName.grid(row=1, column=column-2, ipadx=5)

# Function to handle click on friend's button
def friendButton(head,column):
    head1 = head
    column1 = column
    showFriendFriends(head1, column1)

# Function to clear all displayed images
def clearAll():
    answer = messagebox.askquestion('Information',' Are you sure you want to clear all images')
    if answer == 'yes':
        for widget in bodyFrame.winfo_children():
            widget.destroy()
        bodyFrame.grid_remove()
    
    ButtonShowFriends.configure(state=NORMAL)
    ButtonClearAll.config(state=DISABLED)

# Function to delete a friend
def delFriend():

    # global showFriendFriends

    # # Check if showFriendFriends() function is active
    # if showFriendFriends:
    #     messagebox.showinfo("Action Not Allowed", "You cannot delete friends while viewing a friend's friends.")
    #     return

    delFile = filedialog.askopenfilename(initialdir="images/", title="Select file to delete", filetypes=(("Image file","*.png;*.jpg;*.jpeg;*.gif"),('All files', '*.*')))
    if delFile:
        # Confirm deletion
        check = messagebox.askyesno(title="Delete file?", message="Are you sure you want to delete this file?")
        if check == True:
            filename = os.path.basename(delFile)
            os.remove(delFile)

            # Remove everything inside bodyFrame
            for widget in bodyFrame.winfo_children():
                widget.destroy()
            # Show friends by removing deleted image
            showFriends()
            messagebox.showinfo("Delete a file",f"{filename} deleted")
        else:
            messagebox.showinfo("Delete a file","Change your mind, file not deleted")

# Function to add a friend
def addFriend():
    filetypes = (("Image files","*.png;*.jpg;*.jpeg;*.gif"),("All files","*.*"))
    selectFile = filedialog.askopenfilename(initialdir="./extra_friends", title="Select File", filetypes=filetypes)
    if selectFile:
        print(selectFile)
        check = messagebox.askquestion("Add a New File","Are you sure you want to add a new friend?")
        if check == "yes":
            # Check file extension
            (head, tail) = os.path.splitext(selectFile)
            
            if tail.lower() in [".png",".jpeg"]:
                shutil.copy(selectFile,"./images")
                # Extract the file name from the full path
                filename = os.path.basename(selectFile)
                # displayImage(filename, len(imageButtonList) + 1) 
                imageButtonList.sort()  # Sort the list alphabetically
                showFriends()  # Re-display the friends in the UI
                messagebox.showinfo("Add a New File",f"{filename} added")
            else:
                messagebox.showwarning("Add a New File","Not an image file, not added")
                # showFriends()
        else:
            messagebox.showinfo("Add a New File","Changed your mind, file not added")

# Function to quit the application
def quitApp():
    see_more = messagebox.askyesno(message='Are you sure you want to quit?', detail='Click yes to quit')
    if see_more:
        exit()

# Function to clear a friend's friends
def clearFriendFriends(column):

    '''Function to clear a friend's friends'''
    # Activate the "Delete Friends" button when friend's friends are cleared
    ButtonDeleteFriends.configure(state=NORMAL)
    # rest of the function code...


    print(f"column to be cleared is {column}")
    widgets = bodyFrame.grid_slaves(column=column)
    num_widgets = len(widgets)
    print(num_widgets)
    for widget in widgets[:num_widgets-2]: # Iterate over widgets starting from index 4 onwards
        print(widget)
        widget.grid_remove()

# Function to show the body frame again after clearing all
def showFrame():
    bodyFrame.grid(row=2, column=0, padx=10, pady=10, sticky=NW)
    ButtonShowFriends.configure(state=DISABLED)
    ButtonClearAll.configure(state=NORMAL)        

# Basic Window for your app
myApp = Tk()
myApp.title("Image display app by: Saugat Bhattarai")
myApp.geometry("1350x750")
myApp.maxsize(1350,750)
myApp.configure(background='#b2dfed')

# Adding Icon to the App
photo = PhotoImage(file="Icon//icon.png")
myApp.iconphoto(False, photo)

# Code to configure styles for your ttk widgets
style = ttk.Style()
style.theme_use("alt")

style.configure('Menu.TLabelframe', background="green", borderwidth=1)
style.configure('body.TLabelframe', background="#b2dfee", fg="black")

style.configure('TButton',
                background="#8eb2bd",
                foreground='#060c8c',
                width=19,
                font=('arial, 14'),
                relief='raised')

style.map('TButton', background=[('active','orange')]) 
style.map('Tbutton',background=[('disabled','purple')])

style.configure('friendName.TButton',
                width=14,
                borderwidth=8,
                bordercolor='black',
                background="white", 
                font="arial 10", 
                foreground="black",
                relief='groove',
                ANCHOR='center')

style.configure('clearFriendFriendsButton.TButton',
                background="white", 
                width=8,
                font=('times 8'))

style.configure('friendFriendsName.TLabel',
                width=8,
                background="black",
                borderwidth=6,
                foreground="white",
                font=('times', 9),
                relief='sunken',
                anchor='center')

style.map('TButton', foreground=[('active','#04416f'),('disabled','#fa0202')])

# Create a frame(mainMenu) that will hold buttons to manage the app.
mainMenu = ttk.LabelFrame(myApp, text="App Menu:", width=1200, style='Menu.TLabelframe') 
mainMenu.grid(row=0, column=0, ipady=1, sticky=NW)

bodyFrame = ttk.LabelFrame(myApp, text="My Friends - Click on Friends photo to see their friends", style='body.TLabelframe' )
bodyFrame.grid(row=2, column=0, padx=10, pady=10, sticky=NW)

# Create buttons that have been described in the coursework specification and add to the frame above
ButtonShowFriends = ttk.Button(mainMenu, text="Show Friends", command=showFriends )
ButtonShowFriends.grid(row=0, column=0, ipadx=2, ipady=5, sticky=W)
ButtonClearAll = ttk.Button(mainMenu, text="Clear All", command=clearAll )
ButtonClearAll.grid(row=0, column=1, ipadx=2, ipady=5, sticky=W)
ButtonClearAll.config(state=DISABLED)

ButtonDeleteFriends = ttk.Button(mainMenu, text="Delete Friends", command=delFriend )
ButtonDeleteFriends.grid(row=0, column=2, ipadx=2, ipady=5, sticky=W)
ButtonAddFriends = ttk.Button(mainMenu, text="Add Friends", command=addFriend)
ButtonAddFriends.grid(row=0, column=3, ipadx=2, ipady=5, sticky=NW)
ButtonQuit = ttk.Button(mainMenu, text="Quit", command=quitApp )
ButtonQuit.grid(row=0, column=5, ipadx=2, ipady=5, sticky=NW)
ButtonTheme = ttk.Button(mainMenu, text="Change Theme", command=change_to_dark_theme)
ButtonTheme.grid(row=0, column=4, ipadx=2, ipady=5, sticky=NW)

myApp.mainloop()

