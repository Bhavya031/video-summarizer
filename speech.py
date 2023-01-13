import os
import time
import shutil


def speech_to_text(filepath):
    start = time.time()
    os.system('whisper "' + filepath + '" --model base')
    shutil.move(filepath[6:] + ".srt", 'audio/')
    os.remove(filepath[6:] + ".txt")
    os.remove(filepath[6:] + ".vtt")
    executiontime = (time.time() - start)
    print('Execution time in seconds: ' + str(executiontime))

