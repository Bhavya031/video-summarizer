# Python code to convert video to audio
import moviepy.editor as mp

# Insert Local Video File Path
clip = mp.VideoFileClip(r"Neuroscientist： You Will Never Lack Focus Again! [ezT8kGzYOng].webm")

# Insert Local Audio File Path
clip.audio.write_audiofile(r"Neuroscientist： You Will Never Lack Focus Again! [ezT8kGzYOng].wav")
