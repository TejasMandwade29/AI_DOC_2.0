# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

from gtts import gTTS


# --- This is the only function you need for gTTS ---
def text_to_speech_with_gtts(input_text, output_filepath):
    """Creates an audio file from text using gTTS and saves it."""
    try:
        audio_obj = gTTS(text=input_text, lang="en", slow=False)
        audio_obj.save(output_filepath)
        print(f"gTTS audio saved to {output_filepath}")
        return output_filepath
    except Exception as e:
        print(f"Error with gTTS: {e}")
        return None

