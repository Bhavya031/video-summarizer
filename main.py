import video
import convert
import speech

# download video using ytdl
url = 'https://www.youtube.com/watch?v=eZ74x6dVYes'
# filepath is array that contain path {video-path, audio-name}
filepath = video.download_video(url)
# convert video to audio
convert.convert_video_to_audio(filepath[0], filepath[1])
# speech to text
speech.speech_to_text("audio/" + filepath[1] + ".wav")
