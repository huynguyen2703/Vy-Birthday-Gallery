from flask import Flask, render_template, redirect, url_for
from flask import request
import os
import threading
from pydub import AudioSegment
from pydub.playback import play


# create flask application to manage routes
app = Flask(__name__)


def play_sound(filename):
    """
            Play an audio file using the simpleaudio library.

            This function takes a `filename` parameter representing the path to an audio file
            and uses the simpleaudio library to play the sound.

            Parameters:
                filename (str): The path to the audio file to be played.

            Raises:
                FileNotFoundError: If the specified audio file is not found.

            Returns:
                True when it is playing.
            """
    # try:
    #     playsound(filename)
    # except Exception as e:
    #     print(f"Error while playing {filename}: {e}")
    AudioSegment.converter = "/usr/local/bin/ffmpeg"

    song = AudioSegment.from_mp3(filename)
    play(song)


# home route - displaying front page with start button
@app.route("/")
def start_page():
    return render_template("vy.html")


# gallery route - display 3d gallery - wishes - song
@app.route("/Vy-Gallery.com")
def gallery_page():
    path = "/Vy-Gallery.com"
    sound_file = os.environ.get("SOUND_PATH")
    if request.path == path:
        threading.Thread(target=play_sound, args=(sound_file,), daemon=True).start()
    return render_template("homepage.html")


# story route - display story blog posts
@app.route("/Vy-Story.com")
def story_page():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=False)
