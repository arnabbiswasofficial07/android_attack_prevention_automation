import os
from tkinter import *


def welcomewindow():
    window = Tk()
    window.title("Welcome")
    window.geometry("600x100")
    msg = Message(window, text="Want to check whether your mobile is hacked or not?", justify="center")
    msg.pack()
    button1 = Button(window, text="Yes", command=connectmobile)
    button1.pack(side=RIGHT, padx=50)
    button2 = Button(window, text="No", command=quit)
    button2.pack(side=LEFT, padx=50)
    window.mainloop()


def connectmobile():
    # Get the directory name
    parent_dir = os.path.abspath(os.getcwd())

    # Create an output folder
    parent_dir = "{0}\\output".format(parent_dir)
    if not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)

    # Check the list of adb devices connected
    list_of_adb_devices_txt_file = '{0}\\list.txt'.format(parent_dir)
    list_of_adb_devices_command = "cmd /c adb devices >>" + '"' + list_of_adb_devices_txt_file + '"'
    os.system(list_of_adb_devices_command)
    print(os.path.getsize(list_of_adb_devices_txt_file))
    if os.path.getsize(list_of_adb_devices_txt_file) > 28:
        window = Tk()
        window.title("Connection")
        window.geometry("600x100")
        msg = Message(window, text="Mobile device connected", justify="center")
        msg.pack()
        button1 = Button(window, text="Next", command=check_vulnerabilities)
        button1.pack(side=RIGHT, padx=50)

    else:
        window = Tk()
        window.title("Connection")
        window.geometry("600x100")
        msg = Message(window, text="Mobile device not connected. Connect device and try again", justify="center")
        msg.pack()
        button1 = Button(window, text="Back", command=welcomewindow)
        button1.pack(side=LEFT, padx=50)

    os.remove(list_of_adb_devices_txt_file)


def check_vulnerabilities():
    parent_dir = os.path.abspath(os.getcwd())
    count = 0
    # ps command
    ps_path = '{0}\\ps.txt'.format(parent_dir)
    ps_command = "cmd /c adb shell ps -A >>" + '"' + ps_path + '"'
    os.system(ps_command)
    ps_metasploit_string = 'com.metasploit.stage'
    ps_file = open(ps_path, "r")
    read_ps_file = ps_file.read()
    # Check whether the string is present in ps text file
    if ps_metasploit_string in read_ps_file:
        print("ps command hack present")
        count = count + 1
    else:
        print("ps command hack not present")
    # Close the file
    ps_file.close()
    # Delete the text file
    os.remove(ps_path)

    # netstat command
    netstat_path = '{0}\\netstat.txt'.format(parent_dir)
    netstat_command = "cmd /c adb shell netstat -a >" + '"' + netstat_path + '"'
    os.system(netstat_command)
    netstat_string = '::ffff:192.168.0.1:4444 '
    netstat_file = open(netstat_path, "r")
    read_netstat_file = netstat_file.read()
    # Check whether the string is present in netstat text file
    if netstat_string in read_netstat_file:
        print("netstat command hack present")
        count = count + 1
    else:
        print("nestat command hack not present")
    # Close the file
    netstat_file.close()
    # Delete the text file
    os.remove(netstat_path)

    # top command
    f = 0;
    for x in range(0, 3):
        top_path = '{0}\\top.txt'.format(parent_dir)
        top_command = "cmd /c adb shell top -b -n 1 >" + '"' + top_path + '"'
        os.system(top_command)
        top_string = ' sh '
        top_metasploit_string = 'com.metasploit.stage'
        top_file = open(top_path, "r")
        read_top_file = top_file.read()
        # Check whether the string is present in netstat text file
        if top_string in read_top_file or top_metasploit_string in read_top_file:
            f = f + 1
        # Close the file
        top_file.close()
        # Delete the text file
        os.remove(top_path)

    if f > 0:
        print("top command hack present")
        count = count + 1
    else:
        print("top command hack not present")

    window = Tk()
    window.title("Vulnerabilities")
    window.geometry("600x100")
    s = "Vulnerabilities not found"
    if count >= 1:
        s = str(count) + " vulnerabilities found"
    msg = Message(window, text=s, justify="center")
    msg.pack()
    button1 = Button(window, text="Close", command=quit)
    button1.pack(side=RIGHT, padx=50)


if __name__ == '__main__':
    welcomewindow()
