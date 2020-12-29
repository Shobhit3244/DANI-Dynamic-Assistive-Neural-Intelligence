# DANI-Dynamic-Assistive-Neural-Intellegence
A machine learning based Desktop assistand operated on voice command

More features are being added over time to make more use of the available resources

As it is an open source project if you want to download the code and 
edit it for yourself un "pip install -r requirements.txt" in the command prompt
by navigating to the containing folder or setting path before
running the command as "pip install -r path\to\requirements.txt"
beforehand to install the required libraries.
Or open the console in the same folder by pressing shift+right
click and selecting "open powershell here"

pyinstaller "E:/Python Projects/DANI Test/Main.py" --noconfirm --onefile --console --icon "E:/Python Projects/DANI Test/Assets/DANI Logo 2.ico" --name "DANI" --clean --add-data "E:/Python Projects/DANI Test/Calc.py;." --add-data "E:/Python Projects/DANI Test/Replies.py;." --add-data "E:/Python Projects/DANI Test/Spk_Listen.py;." --add-data "E:/Python Projects/DANI Test/Assets;Assets/" --hidden-import "pyttsx3.drivers.sapi5"