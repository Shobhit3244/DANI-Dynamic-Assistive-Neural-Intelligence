# DANI-Dynamic-Assistive-Neural-Intelligence
A machine learning based Desktop assistand operated on voice command

More features are being added over time to make more use of the available resources

The Exe Installer file for this project can be downloaded
from this link: https://www.mediafire.com/file/7f6wl3d3w2oxzjp/DANI.exe/file
or Zip File from here: https://www.mediafire.com/file/sccogx7fu0qjvl2/Dani.zip/file
for non Admin users.

Currently I am solving the issue with exe that it does not run if tensorflow is not installed on your computer.
but you can run it with the virtual enviroment as used by the raw project files. See below for the steps

Currently Mac and linux Support has not been tested for the program compatability.

If you wish to use the project files as python file itself then, go ahead and download
this enviroment: https://www.mediafire.com/file/l20edc7bhc5ncli/Dani_Env.rar/file

After downloading go to the the downloaded folder and extract the downloaded file
into the same folder where the other project files are and follow the below steps.

Step 1: open power shell as administrator

Step 2: use command 'cd path\to\the\project\folder' to change the directory to
        the project directory.

Step 3: write this command "Dani_Env\Scripts\activate" to activate the environment.
        NOTE: if you are getting Windows not allowed to run scripts error then 
        run this command: "set-executionpolicy remotesigned". 
        This command will work only if you have started the powershell as administrator.
        and then accept everything by pressing y

Step 4: Run the program.


As it is an open source project if you want to download the code and 
edit it for yourself un "pip install -r requirements.txt" in the command prompt
by navigating to the containing folder or setting path before
running the command as "pip install -r path\to\requirements.txt"
beforehand to install the required libraries.
Or open the console in the same folder by pressing shift+right
click and selecting "open powershell here"

Additional Modules which usually generates error while installation are included as
whl files in the Imp Modules Folder. Be sure to install those Modules Before Hand to avoid any Errors
