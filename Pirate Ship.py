import subprocess

print("Welcome to The Pirate Ship")
print("Drag the file you are going to work with (the file only works with certain commands like 'xattr -cr').")
your_file = input("Your file: ").strip().strip("'")

print("Your file is: " + your_file + ". If this is NOT your file, please restart the program.")

# Definición de funciones para ejecutar los comandos
def disable_gatekeeper_program_verification():
    subprocess.run(["sudo", "spctl", "--master-disable"])

def open_damaged_programs(file):
    try:
        subprocess.run(["xattr", "-cr", file])
    except FileNotFoundError:
        print(f"File '{file}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error running 'xattr -cr {file}': {e}")

def disable_software_updates():
    subprocess.run(["sudo", "softwareupdate", "--schedule", "off"])

def disable_macos_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "AutomaticDownload", "-boolean", "false"])

def disable_macos_download_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "AutomaticCheckEnabled", "-bool", "false"])

def disable_security_macos_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "CriticalUpdateInstall", "-bool", "false"])

def install_homebrew():
    subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])

def disable_app_store_updates():
    subprocess.run(["sudo", "defaults", "write", "/Library/Preferences/com.apple.commerce", "AutoUpdate", "-bool", "false"])

def restart_software_update_service():
    subprocess.run(["sudo", "launchctl", "kickstart", "-k", "system/com.apple.softwareupdated"])

# Variable para controlar el bucle
bucle = False

# Ejecutar el programa principal
while not bucle:
    action = input("Enter command (or 'INFO' for available commands, 'Close' to exit): ")

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
        print("For example, for run a comand, like isable MacOS Updates, type 'Disable_MacOS_Updates' because my code not support spaces.")
    
    elif action == "Disable Gatekeeper Program Verification":
        disable_gatekeeper_program_verification()
    
    elif action == "Open Damaged Programs":
        open_damaged_programs(your_file)
    
    elif action == "Disable Software Updates":
        disable_software_updates()
    
    elif action == "Disable MacOS Updates":
        disable_macos_updates()
    
    elif action == "Disable MacOS Download Updates":
        disable_macos_download_updates()
    
    elif action == "Disable Security MacOS Updates":
        disable_security_macos_updates()
    
    elif action == "Install Homebrew":
        install_homebrew()
    
    elif action == "Disable App Store Updates":
        disable_app_store_updates()
    
    elif action == "Restart Software Update Service":
        restart_software_update_service()

    else:
        print("Invalid command. Please try again.")