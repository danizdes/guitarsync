# Import streamlit
import streamlit as st
from audio_recorder_streamlit import audio_recorder

# Import audio stuff
import sounddevice as sd
import soundfile as sf

# import json for song catalogue
import json

### AUDIO STUFF ###

# Gets all the possible microphones
def get_microphones():
    # Get all devices
    devices = sd.query_devices()
    # Blank list for IDs
    ids = []
    names = []

    # Only get the devices that support input (exclude output)
    for index, device in enumerate(devices):
        if device["max_input_channels"] > 0:
            names.append(f"{device['name']} (Channels: {device['max_input_channels']}, Default Rate: {device['default_samplerate']}Hz)")
            ids.append(index)
    
    return ids, names

# Record audio
def record_audio(id, duration, sample_rate=44100):

    # Checks devices capabilites
    device_info = sd.query_devices(id, 'input')
    max_channels = int(device_info['max_input_channels'])
    # Use 2 if possible, and 1 if not supported
    channels = min(max_channels, 2)

    # Record sterio audio
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=channels,
        device=id
    )

    # Block python exec until the recording is complete
    sd.wait()
    return recording

# Save the audio recording to a file
def save_file(recording, filename, sample_rate=44100):
    # Write audio data
    with open(filename, "wb") as file:
        file.write(recording)

### AUDIO SUFF ###

# get JSON data
with open("music/music.json", "r") as file:
    # Get json music data
    music_data = json.load(file)

# Ask user to enter song name
with st.form(key="search_form"):
    # Get song name
    song_query = st.text_input("Enter Song Name", placeholder="Hotel California")
    # Continue button
    submit_button = st.form_submit_button(label="Continue")

## Reord audio

audio_bytes = audio_recorder()

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
        
    save_file(audio_bytes, f'music/{song_query.lower().replace(" ", "-")}.wav')

# If the name is new, save it in the json file and save
if song_query not in music_data:
    music_data[song_query] = f'music/{song_query.lower().replace(" ", "-")}.wav'

    with open("music/music.json", "w") as file:
        json.dump(music_data, file, indent=4)