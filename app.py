# Import all needed libraries
import os
import sys
import streamlit
import streamlit.web.cli as stcli
import sounddevice as sd
import soundfile as sf
import json

# Resolve path (NOTE: AI)
def resolve_path(path: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))

if __name__ == "__main__":
    # Ensure we are in the project directory so relative JSON paths work
    os.chdir(os.path.dirname(__file__))

    # Run streamlit application
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("streamlit/Introduction.py"),  # change if your main file is different
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())