# Gallery App

This is a simple GUI-based application for displaying, managing, and interacting with images of "friends" and their "friends". The application allows users to add new friends, view existing friends, delete friends, and toggle between light and dark themes. The app is built using **Python** and **Tkinter** for the GUI, along with some external libraries for handling images.

--
## Features

1. **Show Friends**: Display images of friends from the `images/` folder.
2. **View Friends' Friends**: Click on a friend's image to see their friends, if any exist, inside a sub-folder within `images/`.
3. **Add Friends**: Add new friends by selecting image files from your computer. Supported file types: `.png`, `.jpg`, `.jpeg`.
4. **Delete Friends**: Delete selected friends from the app.
5. **Clear All Images**: Remove all displayed friends and friends' friends from the UI.
6. **Change Theme**: Toggle between a light and dark theme.
7. **Quit App**: Quit the application after confirmation.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/gallery-app.git
   ```

2. Navigate to the project folder:

   ```bash
   cd gallery-app
   ```

3. Install the required dependencies:

   You will need `Pillow` for image handling, so install it via pip:

   ```bash
   pip install pillow
   ```

4. Run the application:

   ```bash
   python gallery_app.py
   ```

---

## File Structure

```
gallery-app/
│
├── images/                 # Directory containing friends' images
├── extra_friends/          # Directory for selecting additional friends to add
├── Icon/                   # Directory containing the app's icon
│   └── icon.png
├── gallery_app.py          # Main application code
└── README.md               # Documentation file
```

- **images/**: Stores the initial images of your friends. Each image represents a friend, and subdirectories under `images/` can hold pictures of friends' friends.
- **extra_friends/**: Directory where additional images for new friends can be selected from.
- **Icon/**: Holds the app icon that is displayed in the window.
- **gallery_app.py**: The main Python script that runs the Gallery App.

---

## Usage Instructions

### Display Friends
1. Click **"Show Friends"** to display friends from the `images/` folder.
2. Click on a friend's image to view their friends (if any) inside subfolders of the `images/` directory.

### Add a Friend
1. Click **"Add Friends"** to select an image from the `extra_friends/` folder or any location on your system.
2. The selected image will be added to the `images/` folder and displayed in the app.

### Delete a Friend
1. Click **"Delete Friends"** to select an image from the `images/` folder.
2. Confirm to permanently delete the image from the app.

### Clear All
1. Click **"Clear All"** to remove all displayed images from the app's view.
2. This will not delete any images from the disk.

### Change Theme
1. Click **"Change Theme"** to switch between the default light theme and a dark theme.

### Quit the App
1. Click **"Quit"** to close the application.

---

## Customization

You can modify the app's themes by changing the values in the `THEME1` and `THEME2` dictionaries inside the script.

```python
THEME1 = {
    'bg': '#b2dfed',       # Light theme background color
    'button_bg': 'blue',   # Button background color
    'button_fg': 'red'     # Button text color
}

THEME2 = {
    'bg': 'black',         # Dark theme background color
    'button_bg': 'white',  # Button background color
    'button_fg': 'black'   # Button text color
}
```

You can also extend the app to add more features, like adding a search functionality for friends or managing different folders dynamically.

---

## Libraries Used

- **Tkinter**: Used for creating the graphical user interface.
- **Pillow (PIL)**: Used for image handling, especially for resizing images to fit the GUI layout.
- **shutil**: Used to copy files into the `images/` folder.
- **os**: Used to handle file paths and directory operations.

---

## Future Improvements

- Implement search functionality to easily find friends.
- Add support for drag-and-drop file additions.
- Add the ability to edit a friend's name or image.
- Make the app responsive to handle different window sizes.
- Add more themes or theme customization options.

---

## Author

**Saugat Bhattarai**  

---
**License**
This project is licensed under the MIT License. See the LICENSE file for details.
