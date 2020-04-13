from google.cloud import translate
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import api_key
import io
import app_audio as audio

def sample_translate(text="test", project_id=api_key.project_id):
	client = translate.TranslationServiceClient()
	parent = client.location_path(project_id, "global")
	response = client.translate_text(
		parent=parent,
		contents=[text],
		mime_type="text/plain", #or text/html
		source_language_code="en-US",
		target_language_code="ja",
	)
	for translation in response.translations:
		print(translation)
	return response.translations

def jp_en(text="テスト", project_id=api_key.project_id):
	print(project_id)
	client = translate.TranslationServiceClient()
	parent = client.location_path(project_id, "global")
	response = client.translate_text(
		parent=parent,
		contents=[text],
		mime_type="text/plain", #or text/html
		source_language_code="ja",
		target_language_code="en-US",
	)
	return response.translations

def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """
    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "ja"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
    return str(response.results[0].alternatives[0].transcript)

def main():
	audio.Create()
	text = sample_recognize("output.wav")
	#typed = input("何かを打ってくれ: ")
	hi = jp_en(text)
	f = open("test.txt", "w")
	for translation in hi:
		print(translation.translated_text)
		f.write(translation.translated_text)
	f.close()

main()