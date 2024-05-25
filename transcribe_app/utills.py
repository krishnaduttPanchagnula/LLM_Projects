import whisper
from variable import *


def transcribe(filename:str):
    """
    The transcribe function takes a .wav file and transcribes it into text.
    It then saves the text to a .txt file with the same name as the original audio file.
    
    
    :param filename:str: Specify the name of the file that is to be transcribed
    :return: A dictionary with the following keys:
    """
    model = whisper.load_model(whisper_model)
    result = model.transcribe(filename)
    print(result["text"])

    doc_name = filename.replace(".wav",".txt")
    

    with open(doc_name,"w") as f:
        f.write(result["text"])
