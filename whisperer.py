from pathlib import Path
import os
import whisper
from whisper.utils import get_writer

whisper_model = input("\nWChoose your model:\ntiny\nbase\nsmall\nmedium\nlarge\nturbo\n")
model = whisper.load_model(whisper_model)
file = str(Path(input("\nEnter path to file:")))
file_name = os.path.basename(file)
print(file)

def get_transcribe(audio: str, language: str = 'en'):
    return model.transcribe(audio=audio, language=language, verbose=True)


def save_file(results, format='tsv'):
    writer = get_writer(format, './output/')
    writer(results, f'{file_name}.{format}')


if __name__ == "__main__":
    result = get_transcribe(audio=file)
    print('-'*50)
    print('-'*50)
    print(result.get('text', ''))
    save_file(result)
    save_file(result, 'txt')
    save_file(result, 'srt')
