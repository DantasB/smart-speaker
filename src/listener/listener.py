import speech_recognition as sr


class Listener():
    """Responsible by listen everything that the user says

    Args:
        device_index (int, optional): the microphone index in the OS. Defaults to None.
        noiseless (bool, optional): audio recognition should be noiseless or not. Defaults to True.
    """

    def __init__(self, device_index: int = None, noiseless: bool = True):

        self.device_index = device_index
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone(self.device_index)
        self.noiseless = noiseless

    def remove_noise(self, audio_source: sr.Microphone) -> None:
        """ Adjusts the ambient noise

        Args:
            audio_source (sr.Microphone): The microphone source
        """
        if self.noiseless:
            self.recognizer.adjust_for_ambient_noise(audio_source)

    def listen(self) -> str:
        """Listen for any audio inputed by the user

        Returns:
            str: the content listened by the google recognizer
        """
        with self.microphone as source:
            self.remove_noise(source)
            audio = self.recognizer.listen(source)
        try:
            content = self.recognizer.recognize_google(audio, language='pt-BR')
        except sr.UnknownValueError:
            content = ""

        return content
