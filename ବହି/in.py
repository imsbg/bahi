import os
import platform

def shutdown_pc():
    # Detect the operating system
    current_os = platform.system()

    if current_os == "Windows":
        # /s = shutdown, /t 0 = time delay of 0 seconds
        os.system("shutdown /s /t 0")
    elif current_os == "Linux" or current_os == "Darwin": # Darwin is macOS
        # now = shutdown immediately
        os.system("sudo shutdown -h now")
    else:
        print("Operating system not supported.")

# Call the function
if __name__ == "__main__":
    confirm = input("Are you sure to download the json Book Bundles? (y/n): ")
    if confirm.lower() == 'y':
        shutdown_pc()
