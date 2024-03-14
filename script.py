import os, colorama, configparser

cfg = configparser.ConfigParser()

drives = os.popen("fsutil fsinfo drives").read().split(" ")[1:-1]

def findXAMPP():
    for drive in drives:
        for root,dirs,files in os.walk(drive):
            if "xampp" in dirs:
                print(colorama.Fore.GREEN + 'XAMPP found at '+ root + "xampp" + colorama.Style.RESET_ALL)
                cfg.set("XAMPP", "path", root + "xampp")
                with open('data.ini', 'w') as configfile:
                    cfg.write(configfile)
                    configfile.close()
                return True
        print(colorama.Fore.RED + 'XAMPP not found at '+ drive+ colorama.Style.RESET_ALL)
    return False

if os.path.exists('data.ini'):
    print(colorama.Fore.GREEN + 'Data file found'+ colorama.Style.RESET_ALL)
    cfg.read('data.ini')
else:
    print(colorama.Fore.YELLOW + 'Data file not found. Creating...'+ colorama.Style.RESET_ALL)
    cfg.add_section("XAMPP")
    cfg.set("XAMPP", "path", "C:\\xampp")
    with open('data.ini', 'w') as configfile:
        cfg.write(configfile)
        configfile.close()



if cfg.get("XAMPP", "path").endswith("xampp") and os.path.exists(cfg.get("XAMPP", "path")):
    print(colorama.Fore.GREEN + 'XAMPP found at '+ cfg.get("XAMPP", "path")+ colorama.Style.RESET_ALL)
else:
    print(colorama.Fore.RED + 'XAMPP not found at '+ cfg.get("XAMPP", "path")+ colorama.Style.RESET_ALL)
    findXAMPP()

workingDir = ""
workingDir = input("Enter the working directory: ")
workingDir = workingDir.replace('"','')

if os.path.exists(workingDir):
    print(colorama.Fore.GREEN + 'Working directory found at '+ workingDir+ colorama.Style.RESET_ALL)
    cfg.set("XAMPP", "workingDir", workingDir)
    with open('data.ini', 'w') as configfile:
        cfg.write(configfile)
        configfile.close()
    data = []
    with open(cfg.get("XAMPP", "path") + "\\apache\\conf\\httpd.conf", "r") as file:
        data = file.readlines()
        data[251] = 'DocumentRoot "' + workingDir + '"\n'
        data[252] = '<Directory "' + workingDir + '">\n'
        file.close()
    with open(cfg.get("XAMPP", "path") + "\\apache\\conf\\httpd.conf", "w") as file:
        file.writelines(data)
        file.close()
    print(colorama.Fore.GREEN + 'DocumentRoot and Directory updated. Restart Apache to apply changes!'+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + 'Thank you for using my program @NotZiggyIsBack xoxo'+ colorama.Style.RESET_ALL)
else:
    print(colorama.Fore.RED + 'Working directory not found at '+ workingDir+ colorama.Style.RESET_ALL)

input("Press Enter to exit...")
        