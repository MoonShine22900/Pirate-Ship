import subprocess
# Sorry if the comments are in English, it's just that I speak that language and for development it is not convenient for me to put the comments in English
#SOURCE CODE TO COMPILE: If you don't feel confident with my build or you just created something custom or just got bored, compile it

BLUE = "\033[34m"
GREEN = "\033[32m"
#Colors For Make "Friendly" the Program
print(GREEN + "Welcome to The Pirate Ship")
print("Drag the file you are going to work with (the file only works with certain commands like 'xattr -cr'). and if u dont need file just click enter or type anything you want")
your_file = input("Your file: ").strip().strip("'")

print("Your file is: " + your_file + ". If this is NOT your file, please restart the program.")

# Definición de funciones para ejecutar los comandos
def disable_gatekeeper_program_verification():
    subprocess.run(["sudo", "spctl", "--master-disable"])

def default_disable_gatekeeper_program_verification():
    subprocess.run(["sudo", "spctl", "--master-enable"])

def open_damaged_programs(file):
    try:
        subprocess.run(["xattr", "-cr", file])
    except FileNotFoundError:
        print(f"File '{file}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error running 'xattr -cr {file}': {e}")

def disable_software_updates():
    subprocess.run(["sudo", "softwareupdate", "--schedule", "off"])

def default_disable_software_updates():
    subprocess.run(["sudo", "softwareupdate", "--schedule", "on"])

def disable_macos_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "AutomaticDownload", "-boolean", "false"])

def default_disable_macos_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "AutomaticDownload", "-boolean", "true"])

def disable_macos_download_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "AutomaticCheckEnabled", "-bool", "false"])

def default_disable_macos_download_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "AutomaticCheckEnabled", "-bool", "true"])

def disable_security_macos_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "CriticalUpdateInstall", "-bool", "false"])

def default_disable_security_macos_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "CriticalUpdateInstall", "-bool", "true"])

def install_homebrew():
    subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])

def disable_app_store_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.commerce", "AutoUpdate", "-bool", "false"])

def default_disable_app_store_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.commerce", "AutoUpdate", "-bool", "true"])

def restart_software_update_service():
    subprocess.run(["sudo", "launchctl", "kickstart", "-k", "system/com.apple.softwareupdated"])

# Variable para controlar el bucle
bucle = False

# Ejecutar el programa principal
while not bucle:
    action = input(BLUE + "Enter command (or 'INFO' for available commands, 'Close' to exit): ")

    if action == "Close" or action == "exit":
        bucle = True
    
    elif action == "INFO":
        print("Available commands:")
        print("- Disable Gatekeeper Program Verification")
        print("- Open Damaged Programs")
        print("- Disable Software Updates")
        print("- Disable MacOS Updates")
        print("- Disable MacOS Download Updates")
        print("- Disable Security MacOS Updates")
        print("- Install Homebrew")
        print("- Disable App Store Updates")
        print("- Restart Software Update Service")
        print("piracy")
        print("web : shows you a list of craks websites (rebember than this is illegal and is only for testing purposes)" )
        print("TO RUN A COMMAND JUST COPY AND PASTE")
        print("Wanna Undo A command? just tipe default and the code, example default Disable Security MacOS Updates, Install homebrew, Open damaged Programs and Restart Software Update Service dont have this function")
     

    elif action == "Disable Gatekeeper Program Verification":
        disable_gatekeeper_program_verification()
    elif action == "default Disable Gatekeeper Program Verification":
        default_disable_gatekeeper_program_verification()
    elif action == "Open Damaged Programs":
        open_damaged_programs(your_file)
    elif action == "default Open Damaged Programs":
        print("Cannot use default in this command")
    elif action == "Disable Software Updates":
        disable_software_updates()
    
    elif action == "default Disable Software Updates":
        default_disable_software_updates()
    
    elif action == "Disable MacOS Updates":
        disable_macos_updates()
    
    elif action == "default Disable MacOS Updates":
        default_disable_macos_updates()
    
    elif action == "Disable MacOS Download Updates":
        disable_macos_download_updates()
    
    elif action == "default Disable MacOS Download Updates":
        default_disable_macos_download_updates()
    
    elif action == "Disable Security MacOS Updates":
        disable_security_macos_updates()
    
    elif action == "default Disable Security MacOS Updates":
        default_disable_security_macos_updates()
    
    elif action == "Install Homebrew":
        install_homebrew()

    elif action == "default Install Homebrew":
        print("Cannot use default in this command")
    elif action == "Disable App Store Updates":
        disable_app_store_updates()
    
    elif action == "default Disable App Store Updates":
        default_disable_app_store_updates()
    
    elif action == "Restart Software Update Service":
        restart_software_update_service()
    
    elif action == "default Restart Software Update Service":
        print("Cannot use default in this command")
    
    elif action == "default INFO":
        print("Cannot use default in this command")
    
    elif action == "default INFO":
        print("Cannot use default in this command")
    
    elif action == "piracy":
        print("We want to remind you that using and installing pirated software is illegal. We strongly discourage any form of piracy. If you find software valuable, please support its creators by purchasing a legitimate copy. Piracy not only hurts developers but also compromises your system's security. However, if you still decide to use pirated software, consider making donations to the developers or contributing in other ways. Remember, while piracy is illegal and wrong, it is especially unethical if you are generating profits from the pirated software or if you have the means to pay for it. The primary purpose of this program is to allow you to download and try software that might have limited trial versions. If you find the software useful, please purchase it to support the developers. If you do not like it, please delete it. Supporting legal software ensures continued development and innovation. If you are unable to afford the software, consider looking for free or open-source alternatives. Let’s support the hardworking developers who bring valuable tools and applications to the world. Please note that I am not responsible if you encounter viruses or other security issues as a result of using pirated software.")
    
    elif action == "web":
        print(GREEN + "https://www.artistapirata.com", BLUE + "https://www.audiotools.in", GREEN + "https://thepiratebay.org/index.html" + "to open just press command and then press the link you want to open, REBEMBER, JUST TEST IT, DONT HAVE IT MORE THAN 1 WEEK")
    else:
        print("Invalid command. Please try again.")
