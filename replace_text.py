import os

def replace_text_in_file(file_path, old_text, new_text):
    """Заменяет текст в файле."""
    with open(file_path, 'r', encoding='utf-8') as file:
        filedata = file.read()
    
    if old_text in filedata:
        filedata = filedata.replace(old_text, new_text)
    
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(filedata)

def process_directory(root_dir):
    """Проходит по директории и меняет текст во всех файлах с расширением .m."""
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.m'):
                file_path = os.path.join(subdir, file)
                replace_text_in_file(file_path, '#import "GeneratedInterface-Swift.h"', '#import "VERO-Swift.h"')

if __name__ == "__main__":
    root_directory = input("Введите путь к директории: ")
    process_directory(root_directory)
    print("Завершено!")
