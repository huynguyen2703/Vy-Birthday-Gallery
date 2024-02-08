from flask import Flask, render_template, redirect, url_for
from flask import request
import simpleaudio
import os
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
    try:
        # The WaveObject represents the audio file specified by the filename.
        # It is responsible for playing the sound.
        wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
        path = "/Vy-Gallery.com"
        if request.path == path:
            wave_obj.play()
    # catching exceptions while playing song
    except FileNotFoundError as e:
        print(f"file not found: {e}")
    except Exception as e:
        print(f"Error while playing {e}")


# home route - displaying front page with start button
@app.route("/")
def start_page():
    return render_template("vy.html")


# gallery route - display 3d gallery - wishes - song
@app.route("/Vy-Gallery.com")
def gallery_page():
    path = "/Vy-Gallery.com"
    if request.path == path:  # only play song if at this route
        play_sound(os.environ.get("SOUND_PATH"))
        return render_template("homepage.html")
    return render_template("homepage.html")


# story route - display story blog posts
@app.route("/Vy-Story.com")
def story_page():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)
