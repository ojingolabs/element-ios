def process_file(file_path):
    try:
        # Чтение исходного файла
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Обработка строк
        new_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.endswith(".h") and '/' in stripped_line:
                filename = stripped_line.split('/')[-1]
                new_line = f'#import "{filename}"\n'
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        # Запись измененного содержимого обратно в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)
        
        print("Файл успешно обработан.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
input_file = 'input.txt'
process_file(input_file)
