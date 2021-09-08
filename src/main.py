import os
from shared_library.shared_library import generate_workfolder, delete_workfolder
from listener.listener import Listener
from speaker.speaker import Speaker
import dotenv

dotenv.load_dotenv()

ACTIVATION_WORD = os.environ.get("ACTIVATION_WORD")

print("ACTIVATION WORD:", ACTIVATION_WORD)

if __name__ == "__main__":
    workfolder = generate_workfolder()
    speaker = Speaker(workfolder.name)
    listener = Listener()

    while True:
        content = listener.listen()
        print('>', content)
        if content.startswith(ACTIVATION_WORD):
            speaker.play_audio(speaker.create_audio("como posso ajudar?"))
            speaker.play_audio(speaker.create_audio(content))
            break
    delete_workfolder(workfolder)
        
