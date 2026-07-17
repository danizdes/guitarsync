# Import streamlit
import streamlit as st

# Import audio stuff
import sounddevice as sd
import soundfile as sf

# import json for song catalogue
import json

# input numpy for audio
import numpy as np

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
    sf.write(filename, recording, sample_rate)

### AUDIO SUFF ###

# Read json file data
with open("music/music.json", "r") as file:
    music_data = json.load(file)

# fix initiliazaiton erorrs
if "current_song" not in st.session_state:
    st.session_state.current_song = None

if "needs_override" not in st.session_state:
    st.session_state.needs_override = False

# Introduction
st.write("# Record Audio")

# Make streamlit form for song name
with st.form(key="search_form"):
    # Select microphone
    mic_ids, mic_names = get_microphones()
    selected_mic_name = st.selectbox("Select Input Microphone", mic_names)
    selected_mic_id = mic_ids[mic_names.index(selected_mic_name)]
    # Text input - Song Name
    song_query = st.text_input("Enter Song Name", placeholder="Hotel California")

    # Submit button
    submit_button = st.form_submit_button(label="Continue")

# When user presses continue
if submit_button and song_query:
    st.session_state.current_song = song_query
    if song_query in music_data:
        st.session_state.needs_override = True
    else:
        st.session_state.needs_override = False

# Now we need to record the actual audio, I was honestly a little confused how to do do this as the user needs to press stop whenever the
# recording is done. I asked AI and got a solution, to record in 1 second chunks and bind them together

## AI ##

if st.session_state.current_song and not getattr(st.session_state, "needs_override", False):
    if selected_mic_id is not None:
        chunks = []
        
        st.warning("Recording... Press the 'Stop' button below when you are finished.")
        stop_placeholder = st.empty()
        
        if "recording_active" not in st.session_state:
            st.session_state.recording_active = True

        # Run the loop until stopped
        while st.session_state.recording_active:
            # Check if user clicked the stop button
            if stop_placeholder.button("Stop Recording", key=f"stop_{len(chunks)}"):
                st.session_state.recording_active = False
                break

            # Call your original function to record a 1-second slice
            chunk = record_audio(selected_mic_id, duration=1.0)
            chunks.append(chunk)
            
        stop_placeholder.empty()
        
        # Combine chunks into one continuous audio vector
        if chunks:
            audio_data = np.concatenate(chunks, axis=0)
            filename = f"music/{st.session_state.current_song.lower().replace(' ', '_')}.wav"
            save_file(audio_data, filename)
            st.success(f"Successfully recorded and saved to `{filename}`!")
            
            # Reset setup state
            st.session_state.current_song = None
    else:
        st.error("Cannot record without a valid input source.")