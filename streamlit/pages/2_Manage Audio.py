# import streamlit
import streamlit as st

# import json 
import json

# Read json data
with open("music/music.json", "r") as file:
    music_data = json.load(file)

st.write("""
# Track Catalogue
        """)

# Loop through each song in the music database
for song_name in list(music_data.keys()):
    # Set up 2 side by side columns, one for the song and another for delete
    col1, col2 = st.columns([4, 1])

    # Write song name
    with col1:
        st.write(f"{song_name}")
    
    # Show delete option
    with col2:
        # NOTE: 'key' was AI generated
        if st.button("🗑️", key=f"btn_delete_{song_name.lower().replace(' ', '_')}"):
            
            # Remove the song from the data structure
            music_data.pop(song_name)
            
            # Save to JSON file
            with open("music/music.json", "w") as file:
                json.dump(music_data, file, indent=4)
        
            # Refresh state when deleteion
            st.rerun()