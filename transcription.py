from faster_whisper import WhisperModel
from faster_whisper.transcribe import Segment

model_size = "large-v3"

def transcribe(file):
    global model_size

    model = WhisperModel(model_size, device="cpu", compute_type="int8_float32")


    segments, info = model.transcribe("output.wav",
                                      beam_size=5,
                                      compression_ratio_threshold=2.4,
                                      log_prob_threshold=-1.0,
                                      temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    segmentsTemp = []
    for segment in segments:
        segmentsTemp.append(segment)
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    segments = segmentsTemp
    write_transcription(segments)

def write_transcription(segments):
    print(segments)
    with open("transcription.txt", "w") as output:
        data= []
        for segment in segments:
            data.append([segment.start, segment.end, segment.text])
        output.write(str(data))

if __name__ == "__main__":
    transcribe("output.wav")