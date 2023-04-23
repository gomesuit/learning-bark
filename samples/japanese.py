from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

import logging
logging.basicConfig(level=logging.DEBUG)

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
WOMAN: こんにちは、私の名前はスノーです。そして、うーん、私はピザが好きです。 [laughs]
"""

from scipy.io.wavfile import write as write_wav

for i in range(10):
    history_prompt = "ja_speaker_" + str(i)
    audio_array = generate_audio(
        text_prompt,
        history_prompt=history_prompt,
    )
    write_wav("audio_" + str(i) + ".wav", SAMPLE_RATE, audio_array)
