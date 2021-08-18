from shared_library.shared_library import generate_workfolder, delete_workfolder
from listener.listener import Listener
from speaker.speaker import Speaker


if __name__ == "__main__":
    workfolder = generate_workfolder()
    speaker = Speaker(workfolder)
    listener = Listener(1)

    while True:
        content = Listener.listen()
        if content:
            speaker.play_audio(speaker.create_audio(content))
            break
    delete_workfolder(workfolder)
