# Embedded twitter links fix

## Explanation:
Sometimes on Discord, Messenger and whatnot, the video or image contained in the tweet wouldn't be shown directly under the posted link. So I made a fix for that.
With the script, when you copy a twitter url link, it will change the value in your clipboard ("x" => "fxtwitter" in the url),
so that when you paste it it will be the correct way to show the video or image directly.
When running the script, a cmd.exe command prompt will appear. You need to run the script once, and keep the command prompt open and it will work at all times.

## Technical details:
I used python and some modules for the script. I will explain also how to use a create a batch file to enhance automation and accessiblity.

Step 1: Create a new .txt file with an explicit name (like run_twitter_link_fix or whatever)
Step 2: Write this in the file
  
  call C:\(Project Path)\First\.venv\Scripts\activate
  C:\(Project Path)\.venv\Scripts\python.exe C:\(Project Path)\Main.py

(You have to write the whole path, usually starting with the C drive but not necessarily)

Step 3: Turn the .txt file that you used into .bat file to turn it into a batch file (script file).
Step 4: Profit!!!

Now you can just double click that .bat file to make the script keep working

## Bonus:
You can use Microsoft PowerToys (or Linux/Mac alternatives) feature called "Keyboard Manager" to create a shortcut to link to the batch file,
that will start with only a simple keybind, whenever you are on your computer to enhance ease of use, speed and accessiblity.
