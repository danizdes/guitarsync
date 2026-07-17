import os
import sys
import streamlit
import streamlit.web.cli as stcli
import sounddevice as sd
import soundfile as sf
import json


def resolve_path(path: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_dir = sys._MEIPASS
    elif "__compiled__" in dir(__builtins__):
        if "app.app/Contents/MacOS" in os.path.abspath(sys.executable):
            base_dir = os.path.abspath(
                os.path.join(os.path.dirname(sys.executable), "..", "..", "..")
            )
        else:
            base_dir = os.path.dirname(os.path.abspath(sys.executable))
    elif "app.app/Contents/MacOS" in os.path.abspath(__file__):
        base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..")
        )
    elif not os.path.basename(sys.executable).lower().startswith("python"):
        base_dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(base_dir, path))


if __name__ == "__main__":
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        runtime_dir = sys._MEIPASS
    elif "__compiled__" in dir(__builtins__):
        if "app.app/Contents/MacOS" in os.path.abspath(sys.executable):
            runtime_dir = os.path.abspath(
                os.path.join(os.path.dirname(sys.executable), "..", "..", "..")
            )
        else:
            runtime_dir = os.path.dirname(os.path.abspath(sys.executable))
    elif "app.app/Contents/MacOS" in os.path.abspath(sys.executable):
        runtime_dir = os.path.abspath(
            os.path.join(os.path.dirname(sys.executable), "..", "..", "..")
        )
    elif not os.path.basename(sys.executable).lower().startswith("python"):
        runtime_dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        runtime_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(runtime_dir)
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("streamlit/Introduction.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
