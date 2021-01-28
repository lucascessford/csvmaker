Hello people!
I built a simple script that allows me to drop in my excel files onto the .exe icon and it generate a timestamped csv for me in the same directory.

To set up this handy tool:

1. Download pyinstaller (with "pip install pyinstaller")

2. Run the below command to turn your .py into a .exe
	>>>pyinstaller -F -w -i "csv.ico" csvmaker.py

3. Grab the newly created .exe file from the dist folder that got created and put it on your desktop.
   Delete all the other nonsense.


#### DETAILS ####
If you want a different icon, just switch out the .ico file with something else.
The conditions of this script are that it will delete the first row (as it assumed your excel had a header)
and then it will generate a timestamped .csv file for you.
If your excel file had multiple sheets, it will create the csv of whatever sheet was selected at the time of its last save.
#################


Hope it helps!