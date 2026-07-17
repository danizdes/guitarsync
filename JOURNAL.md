# 10th July, 2026

* *9:15* Init Commit! Inititialized the repository with all the basic details

* *9:25* I'm trying to think of the base features of the app, I think the way it should work is:

    1. User has 2 lists, one for "learning" songs and one for "learnt" songs.
    2. A record button for recording the songs
    3. Save those recordings to a "song"
    4. Save everything in JSON

* *9:33* I've built a rough flow of the site, `flow.excalidraw.png`

# 16 July 

Okay so I removed the excalidraw flow thing cause I want to start over. 

Okay so what I want to do is simple. From the Users POV I want to easily record audio, and then
cateogirze them. I'll start small first and make the app easily store and record tracks. 

Okay so I've made a file ```utils.py``` hosting re usable code. I added re usable components specifically
for audio

Okay no I need to create the UI. I'll use pyqt6. I honeslty don't have much idea about how PyQT works
so i'll use AI to look up the documentation.

Okay wow this GUI stuff is way above my pay grade 😭. What if I try and make TUI apps?

# 17th July

OKAY IDEA, what if I built a mac app that launched a local streamlit instance!

[Speech to text]
Okay, so I built out the basic structure for the record audio. There's still a lot of bugs, but yeah, I think it's pretty good so far. And I also replaced all of the, what do you call it? The app.py into a proper streamlet directory.

This is so cluncy like.. It's not working half the time. There has got to be an alternative

I realized theres a streamlit packages for that... and they actually work quite well 😭😭😭. I used that instead to record audio.