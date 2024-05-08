import pyautogui
import time
import pygetwindow as gw

# Define delay in seconds
delay = 1.2  # Adjust as needed

try:
    # Minimize all windows
    pyautogui.hotkey('win', 'd')
    time.sleep(delay)
    
    # Move mouse to the top-left corner with delay
    pyautogui.moveTo(30, 320, duration=delay)
    pyautogui.doubleClick()
    time.sleep(delay)
    
    # Get the active window
    active_window = gw.getActiveWindow()
    if active_window is not None:
        # Maximize the window
        active_window.maximize()
        time.sleep(delay)
        
        # Click on the address bar and type the path
        pyautogui.click(1030, 55)
        time.sleep(delay)
        text_to_type = "C:\\Users\\joanm\\Desktop\\Noly\\python 2\\2024\\here"
        pyautogui.write(text_to_type, interval=0.02)
        time.sleep(delay)
        
        # Press Enter to navigate to the folder
        pyautogui.press('enter')
        time.sleep(delay)
        pyautogui.click(2550, 180)
        
        # Scroll down to view more files/folders
        pyautogui.scroll(-200)  # Adjust the scroll amount as needed
        time.sleep(delay)
        
    else:
        print("No active window found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
