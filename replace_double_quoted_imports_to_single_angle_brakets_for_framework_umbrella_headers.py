import re

def replace_imports(file_path):
    # Откроем файл для чтения
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Регулярное выражение для поиска строк вида #import "somename.h"
    pattern = re.compile(r'#import\s+"([^"]+)"')

    # Функция замены
    def replacement(match):
        return f'#import <ElementRiot/{match.group(1)}>'

    # Заменяем все вхождения
    new_content = re.sub(pattern, replacement, content)

    # Откроем файл для записи и сохраним изменения
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")
    # Запускаем функцию замены
    replace_imports(file_path)
    print("Файл успешно обновлен!")
