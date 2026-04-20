import subprocess
import platform

def shutdown_computer():
    # Identify the OS
    system = platform.system()
    
    try:
        if system == "Windows":
            subprocess.run(["shutdown", "/s", "/f", "/t", "0"], check=True)
        
        elif system == "Linux" or system == "Darwin": 
            subprocess.run(["sudo", "shutdown", "-h", "now"], check=True)
            
        else:
            print(f"OS '{system}' not supported.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error: Could not shut down. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




