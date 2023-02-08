
from hanspell import spell_checker
from googletrans import Translator
from tqdm import tqdm

path = './textFolder'


#sentence corrections
def read_text_file(file_path,  new_file_path ):
    translator = Translator(raise_exception=True)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines() #read file by list
        print(f'start {new_file_path}')
        result = spell_checker.check(lines)

        w = open(new_file_path, 'w')
        for line in result:
            w.write(line.checked)
            w.write('\n')
            try: #if google api shows error, pass
                translated_sentence = translator.translate(line.checked)
                w.write(translated_sentence.text)
            except:
                pass
            w.write('\n\n')
        w.close()
        print(f'finish! for {new_file_path}')


for file in os.listdir(path):
    if file.endswith('.txt'):
        file_path = os.path.join(path, file)
        new_file_path = os.path.join(path,f"translated_{file}")
        read_text_file(file_path,  new_file_path )




