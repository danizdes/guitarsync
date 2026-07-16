# Import audio stuff
import sounddevice as sd
import soundfile as sf


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

    # Record sterio audio
    recording = sd.rec(
        int(duration * sample_rate),
        sample_rate=sample_rate,
        channels=2,
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