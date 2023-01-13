import moviepy.editor as mp


def convert_video_to_audio(video_path, audio_path):
    # Insert Local Video File Path
    print(audio_path)
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile("audio/"+audio_path + ".wav")
