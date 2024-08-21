import pyperclip
import re
import time
import pystray
import keyboard
from PIL import Image, ImageDraw
import threading

# Global variable to control the clipboard monitoring
monitoring = False

def is_twitter_url(url):
    # Regular expression to check if the URL is a Twitter or X link
    return re.match(r'https?://(www\.)?(twitter\.com|x\.com)/[a-zA-Z0-9_]+/status/[0-9]+$', url) is not None

def modify_twitter_url(url):
    # Replace the domain in the URL with "https://fxtwitter"
    modified_url = re.sub(r'https?://(www\.)?(twitter\.com|x\.com)', 'https://fxtwitter.com', url)
    return modified_url

def monitor_clipboard():
    global monitoring
    previous_clipboard_content = ""

    while monitoring:
        # Get the current content of the clipboard
        current_clipboard_content = pyperclip.paste()

        # Check if the clipboard content has changed
        if current_clipboard_content != previous_clipboard_content:
            # If the new content is a Twitter or X URL, perform an action
            if is_twitter_url(current_clipboard_content):
                modified_url = modify_twitter_url(current_clipboard_content)
                pyperclip.copy(modified_url)  # Copy the modified URL to the clipboard
                print(f"Original URL: {current_clipboard_content}")
                print(f"Modified URL: {modified_url}")
            else:
                print("Not a Twitter or X URL.")

            # Update the previous clipboard content
            previous_clipboard_content = current_clipboard_content

        # Wait for a short period before checking again
        time.sleep(1)

def start_script():
    global monitoring
    if not monitoring:  # Only start if not already monitoring
        print("Script started.")
        monitoring = True
        # Start the clipboard monitoring in a separate thread
        threading.Thread(target=monitor_clipboard, daemon=True).start()

def stop_script():
    global monitoring
    if monitoring:  # Only stop if currently monitoring
        monitoring = False
        print("Script stopped.")

def create_image(width, height, color1, color2):
    # Generate an image for the tray icon
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, height // 2, width, height),
        fill=color2)
    return image

def setup(icon):
    icon.icon = create_image(64, 64, "white", "blue")
    icon.visible = True

def cleanup(icon):
    print("Cleaning up resources...")
    stop_script()  # Ensure monitoring is stopped
    icon.stop()

if __name__ == "__main__":
    # Create a system tray icon
    icon = pystray.Icon("My Script")
    icon.title = "My Script"
    icon.menu = pystray.Menu(
        pystray.MenuItem("Start", start_script),
        pystray.MenuItem("Stop", stop_script),
        pystray.MenuItem("Exit", cleanup)
    )

    # Add keyboard shortcuts
    keyboard.add_hotkey("ctrl+c", start_script)
    keyboard.add_hotkey("ctrl+v", stop_script)

    # Run the tray icon
    icon.run(setup)