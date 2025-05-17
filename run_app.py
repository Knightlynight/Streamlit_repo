import subprocess
import os
import sys

def main():
    # Construct the absolute path to Home.py
    app_path = os.path.join(os.path.dirname(__file__), "Home.py")
    
    # Run Streamlit using the current Python interpreter
    result = subprocess.run(
        [sys.executable, "-m", "streamlit", "run", app_path],
        shell=True
    )
    
    # Keep the console open after the process ends
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
