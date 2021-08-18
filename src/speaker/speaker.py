from gtts import gTTS
from playsound import playsound


class Speaker():
    """Instantiate a google tts speaker

    Args:
        workfolder (str): the folder that will store all audios generated
        language (str, optional): The language that the tts will understand. Defaults to 'pt-br'.
    """

    def __init__(self, workfolder: str, language: str = 'pt-br'):
        self.language = language
        self.workfolder = workfolder

    def create_audio(self, content) -> gTTS:
        """Creates a google tts object

        Args:
            content (str): the string content that will be spoken

        Returns:
            gTTS: google tts audio object to be spoken
        """
        return gTTS(content, lang=self.language)

    def play_audio(self, tts: gTTS) -> None:
        """Plays any gtts audio generated

        Args:
            tts (gTTS): google tts audio object to be spoken
        """
        audio_file = self.workfolder + 'tmp.mp3'
        tts.save(audio_file)
        playsound(audio_file)
