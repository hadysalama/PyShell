import os as os
#print(system("ping 192.168.0.5"))
#print(system("uname -a"))
iphone_home = "/private/var/mobile/Containers/Data/Application/A67FEF53-0AFD-4F07-855A-7993A23BFF5A/Documents"

mac_home = "/Users/hadysalama/Desktop/Personal Code/Python Personal Projects/PersonalProjects"


def shell():
    print("Welcome to PyShell")
    while True:
        cwd = os.getcwd()
        if cwd == iphone_home or cwd == mac_home:
            cwd = "~"
        command = input(cwd + "$ ")
        if command == "exit":
            break
        elif command == "help":
            output = "psh: a simple shell written in Python"
        else:
            #output = os.popen(command).read() + "\n"
            output = os.system(command)
        print(output)
# shell()


def child(counter):
    print("Welcome to PyShell Process %d " % counter)
    while True:
        cwd = os.getcwd()
        if cwd == iphone_home or cwd == mac_home:
            cwd = " ~ "
        command = input(cwd + "$ ")
        if command == "e":
            kill = True
            break
        if command == "fork":
            kill = False
            break
        elif command == "help":
            output = "PyShell: A concurrent shell written in Python"
        else:
            output = os.popen(command).read() + "\n"
            #output = os.system(command)
        print(output)
    return kill


def parent():
    counter = 0
    # try:
    while True:
        newpid = os.fork()
        counter += 1
        if newpid == 0:
            #print("Forked Child as print()")
            kill = child(counter)
            os._exit(0)
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" % pids)
            os.waitpid(newpid, 0)
            kill = False
            #print("Q for quit / F for new fork \n")
            #reply = input()
            if kill:
                print("A Graceful Death after forking %d processes" % counter)
                break
            else:
                continue
    # except EOFError:
        


def concurrent_shell():
    parent()


concurrent_shell()
