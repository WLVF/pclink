if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
cd ..
cd AppData
cd Roaming
cd discord
cd pclink
cls
echo Please ask if the host is online.
python client.py
