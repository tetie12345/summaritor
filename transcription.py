import ctypes, glob, os
import nvidia.cublas.lib, nvidia.cudnn.lib

for pkg in (nvidia.cublas.lib, nvidia.cudnn.lib):
    lib_dir = list(pkg.__path__)[0]
    for so in sorted(glob.glob(os.path.join(lib_dir, "*.so*"))):
        try:
            ctypes.CDLL(so, mode=ctypes.RTLD_GLOBAL)
        except OSError:
            pass  # some libs depend on others that load later; ignore

from faster_whisper import WhisperModel

model_size = "large-v3"

def transcribe(file):
    global model_size

    model = WhisperModel(model_size, device="cuda", compute_type="int8")


    segments, info = model.transcribe(file,
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
    pass