""""При старте приложения запускаются три потока.
Первый поток заполняет список случайными числами.
Два других потока ожидают заполнения. Когда список
заполнен оба потока запускаются. Первый поток находит
сумму элементов списка, второй поток среднеарифметическое значение в списке. Полученный список, сумма и
среднеарифметическое выводятся на экран.

import threading
import random


numbers = []
ready = threading.Event()

def fill_numbers():
    global numbers
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Список заполнен: {numbers}")
    ready.set()  # Сигнал, что список готов

def calc_sum():
    ready.wait()  # Ждем, пока список будет заполнен
    s = sum(numbers)
    print(f"Сумма элементов списка: {s}")

def calc_average():
    ready.wait()  # Ждем, пока список будет заполнен
    avg = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое: {avg:.2f}")

if __name__ == "__main__":
    t1 = threading.Thread(target=fill_numbers)
    t2 = threading.Thread(target=calc_sum)
    t3 = threading.Thread(target=calc_average)

    t2.start()
    t3.start()
    t1.start()

    t1.join()
    t2.join()
    t3.join()
 """

"""
Задание 2
Пользователь с клавиатуры вводит путь к файлу.
После чего запускаются три потока. Первый поток заполняет файл случайными числами. Два других потока
ожидают заполнения. Когда файл заполнен оба потока
стартуют. Первый поток находит все простые числа, второй поток факториал каждого числа в файле. Результаты
поиска каждый поток должен записать в новый файл. На
экран необходимо отобразить статистику выполненных
операций.
import threading
import random
import math

import os

# Событие для синхронизации
file_ready = threading.Event()

# Статистика
stats = {
    "prime_count": 0,
    "factorial_count": 0
}

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def fill_file(filename, N=10):
    "Заполнение файла N случайными числами"
    numbers = [random.randint(1, 20) for _ in range(N)]
    with open(filename, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")
    print(f"Файл {filename} заполнен числами: {numbers}")
    file_ready.set()  # Сигнал о готовности

def find_primes(infile, outfile):
    file_ready.wait()  # Ждать заполнения файла
    with open(infile) as fin, open(outfile, "w") as fout:
        count = 0
        for line in fin:
            num = int(line.strip())
            if is_prime(num):
                fout.write(f"{num}\n")
                count += 1
        stats["prime_count"] = count

def calc_factorials(infile, outfile):
    file_ready.wait()
    with open(infile) as fin, open(outfile, "w") as fout:
        count = 0
        for line in fin:
            num = int(line.strip())
            fact = math.factorial(num)
            fout.write(f"{num}! = {fact}\n")
            count += 1
        stats["factorial_count"] = count

if __name__ == "__main__":
    filename = input("Введите путь к файлу: ").strip()
    primes_out = os.path.splitext(filename)[0] + "_primes.txt"
    factorials_out = os.path.splitext(filename)[0] + "_factorials.txt"

    threads = [
        threading.Thread(target=fill_file, args=(filename,)),
        threading.Thread(target=find_primes, args=(filename, primes_out)),
        threading.Thread(target=calc_factorials, args=(filename, factorials_out))
    ]

    # Запуск потоков 2 и 3 сразу (они будут ждать file_ready)
    threads[1].start()
    threads[2].start()
    threads[0].start()

    for t in threads:
        t.join()

    print(f"Выполнено операций поиска простых чисел: {stats['prime_count']}")
    print(f"Выполнено операций вычисления факториалов: {stats['factorial_count']}")
    print(f"Файл с простыми числами: {primes_out}")
    print(f"Файл с факториалами: {factorials_out}")
"""

"""
Задание 3
Пользователь с клавиатуры вводит путь к существующей директории и к новой директории. После чего
запускается поток, который должен скопировать содержимое директории в новое место. Необходимо сохранить
структуру директории. На экран необходимо отобразить
статистику выполненных операций.

import os
import shutil
import threading
import time
import sys

def copy_tree_worker(src, dst, stats):
    start = time.perf_counter()
    try:
        for root, dirs, files in os.walk(src):
            rel = os.path.relpath(root, src)
            dest_root = dst if rel == '.' else os.path.join(dst, rel)

            # Создаем целевую подпапку, если её нет
            if not os.path.exists(dest_root):
                try:
                    os.makedirs(dest_root, exist_ok=True)
                    stats['dirs_created'] += 1
                except Exception as e:
                    stats['errors'] += 1
                    stats['errors_list'].append(f"mkdir {dest_root}: {e}")
                    # Пропускаем вложенное содержимое этой папки
                    continue

            # Копируем файлы
            for name in files:
                src_path = os.path.join(root, name)
                dest_path = os.path.join(dest_root, name)
                try:
                    # Если это не обычный файл, можно пропустить (например, FIFO/сокеты)
                    if not os.path.isfile(src_path):
                        stats['files_skipped'] += 1
                        continue
                    size = os.path.getsize(src_path)
                    shutil.copy2(src_path, dest_path)  # сохраняем метаданные (время/права)
                    stats['files_copied'] += 1
                    stats['bytes_copied'] += size
                except Exception as e:
                    stats['errors'] += 1
                    stats['errors_list'].append(f"copy {src_path} -> {dest_path}: {e}")
    finally:
        stats['elapsed_sec'] = time.perf_counter() - start


def validate_paths(src, dst):
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)

    if not os.path.isdir(src):
        raise ValueError(f"Исходная директория не найдена или не является директорией: {src}")

    # Запрещаем копирование внутрь самой себя или внутрь подпапки
    try:
        if os.path.samefile(src, dst):
            raise ValueError("Путь назначения совпадает с исходным.")
    except Exception:
        pass

    # Проверка, что dst не находится внутри src
    src_common = os.path.commonpath([src])
    try:
        common = os.path.commonpath([src, dst])
        if common == src_common and dst.startswith(src):
            raise ValueError("Директория назначения не должна находиться внутри исходной.")
    except Exception:
        # На случай разных дисков/платформных особенностей просто продолжаем
        pass

    # Если dst существует и это не директория — ошибка
    if os.path.exists(dst) and not os.path.isdir(dst):
        raise ValueError(f"Путь назначения существует и это не директория: {dst}")

    # Создаем корневую директорию назначения при необходимости
    if not os.path.exists(dst):
        os.makedirs(dst, exist_ok=True)

    return src, dst


def human_bytes(n):
    # Удобочитаемый размер
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PB"


if __name__ == "__main__":
    try:
        src_input = input("Введите путь к существующей директории: ").strip().strip('"')
        dst_input = input("Введите путь к новой директории (будет создана, если нет): ").strip().strip('"')

        src, dst = validate_paths(src_input, dst_input)

        stats = {
            "dirs_created": 0,
            "files_copied": 0,
            "files_skipped": 0,
            "bytes_copied": 0,
            "errors": 0,
            "errors_list": [],
            "elapsed_sec": 0.0,
        }

        worker = threading.Thread(target=copy_tree_worker, args=(src, dst, stats), daemon=False)
        worker.start()

        print("Копирование запущено в отдельном потоке. Ожидаем завершения...")
        worker.join()

        print("\nСтатистика:")
        print(f"- Создано директорий: {stats['dirs_created']}")
        print(f"- Скопировано файлов: {stats['files_copied']}")
        print(f"- Пропущено (не обычные файлы): {stats['files_skipped']}")
        print(f"- Объем данных: {human_bytes(stats['bytes_copied'])}")
        print(f"- Ошибок: {stats['errors']}")
        print(f"- Время: {stats['elapsed_sec']:.2f} c")

        if stats["errors_list"]:
            print("\nСписок ошибок:")
            for msg in stats["errors_list"]:
                print(f"  {msg}")

        print(f"\nГотово. Данные скопированы в: {dst}")

    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
"""

"""
Задание 4
Пользователь склавиатурывводитпутьксуществующей
директории и слово для поиска. После чего запускаются
два потока. Первый должен найти файлы, содержащие
искомое слово и слить их содержимое в один файл. Второй поток ожидает завершения работы первого потока.
После чего проводит вырезание всех запрещенных слов
(список этих слов нужно считать из файла с запрещенными словами) из полученного файла. На экран необходимо
отобразить статистику выполненных операций.
"""
import os
import re
import sys
import time
import threading

def human_bytes(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PB"

def read_text_file(path, encoding='utf-8'):
    with open(path, 'r', encoding=encoding, errors='ignore') as f:
        return f.read()

def write_text_file(path, data, encoding='utf-8'):
    with open(path, 'w', encoding=encoding) as f:
        f.write(data)

def append_text_file(path, data, encoding='utf-8'):
    with open(path, 'a', encoding=encoding) as f:
        f.write(data)

def read_forbidden_words(path):
    words = []
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith('#'):
                continue
            words.append(s)
    return words

def merge_worker(src_dir, search_word, out_path, stats, lock):
    t0 = time.perf_counter()
    files_scanned = 0
    files_matched = 0
    bytes_merged = 0
    errors = []

    search_lower = search_word.lower()
    out_abs = os.path.abspath(out_path)

    # Очищаем/создаём целевой файл
    try:
        write_text_file(out_abs, "")
    except Exception as e:
        with lock:
            stats['errors'] += 1
            stats['errors_list'].append(f"Создание выходного файла: {e}")
        return

    try:
        for root, _, files in os.walk(src_dir):
            for name in files:
                path = os.path.abspath(os.path.join(root, name))
                if path == out_abs:
                    continue  # не включаем сам результирующий файл

                files_scanned += 1
                try:
                    text = read_text_file(path)
                except Exception as e:
                    errors.append(f"Чтение {path}: {e}")
                    continue

                if search_lower in text.lower():
                    files_matched += 1
                    # Для читаемости добавим разделитель (можно убрать)
                    chunk = f"\n===== BEGIN {path} =====\n{text}\n===== END {path} =====\n"
                    try:
                        append_text_file(out_abs, chunk)
                        bytes_merged += len(chunk.encode('utf-8'))
                    except Exception as e:
                        errors.append(f"Запись в {out_abs} при добавлении {path}: {e}")
    finally:
        elapsed = time.perf_counter() - t0
        with lock:
            stats['merge_time_sec'] = elapsed
            stats['files_scanned'] += files_scanned
            stats['files_matched'] += files_matched
            stats['bytes_merged'] += bytes_merged
            stats['merged_output'] = out_abs
            stats['errors'] += len(errors)
            stats['errors_list'].extend(errors)

def filter_worker(merge_thread, out_path, forbidden_path, stats, lock):
    # Ждём завершения первого потока
    merge_thread.join()

    t0 = time.perf_counter()
    removed_total = 0
    bytes_after = 0
    errors = []

    try:
        words = read_forbidden_words(forbidden_path)
        with lock:
            stats['forbidden_words'] = len(words)
        if not words:
            with lock:
                stats['filter_time_sec'] = time.perf_counter() - t0
            return

        # Регистронезависимая фильтрация целых слов
        escaped = [re.escape(w) for w in words]
        pattern = re.compile(r'\b(' + '|'.join(escaped) + r')\b', flags=re.IGNORECASE | re.UNICODE)

        try:
            text = read_text_file(out_path)
        except Exception as e:
            errors.append(f"Чтение результирующего файла {out_path}: {e}")
            with lock:
                stats['errors'] += len(errors)
                stats['errors_list'].extend(errors)
                stats['filter_time_sec'] = time.perf_counter() - t0
            return

        filtered, removed = pattern.subn('', text)
        removed_total += removed

        try:
            write_text_file(out_path, filtered)
            bytes_after = len(filtered.encode('utf-8'))
        except Exception as e:
            errors.append(f"Запись результирующего файла {out_path}: {e}")

    finally:
        elapsed = time.perf_counter() - t0
        with lock:
            stats['filter_time_sec'] = elapsed
            stats['removed_count'] += removed_total
            stats['bytes_after_filter'] += bytes_after
            stats['errors'] += len(errors)
            stats['errors_list'].extend(errors)

def main():
    try:
        src_dir = input("Введите путь к существующей директории: ").strip().strip('"')
        if not os.path.isdir(src_dir):
            print("Ошибка: директория не найдена.")
            sys.exit(1)

        search_word = input("Введите слово для поиска: ").strip()
        if not search_word:
            print("Ошибка: пустое слово для поиска.")
            sys.exit(1)

        forbidden_path = input("Введите путь к файлу с запрещёнными словами: ").strip().strip('"')
        if not os.path.isfile(forbidden_path):
            print("Ошибка: файл с запрещёнными словами не найден.")
            sys.exit(1)

        out_path = input("Введите путь выходного файла (по умолчанию merged.txt): ").strip().strip('"')
        if not out_path:
            out_path = "merged.txt"

        stats = {
            'files_scanned': 0,
            'files_matched': 0,
            'bytes_merged': 0,
            'merged_output': "",
            'forbidden_words': 0,
            'removed_count': 0,
            'bytes_after_filter': 0,
            'merge_time_sec': 0.0,
            'filter_time_sec': 0.0,
            'errors': 0,
            'errors_list': []
        }
        lock = threading.Lock()

        merge_thread = threading.Thread(
            target=merge_worker,
            args=(src_dir, search_word, out_path, stats, lock),
            daemon=False
        )
        filter_thread = threading.Thread(
            target=filter_worker,
            args=(merge_thread, out_path, forbidden_path, stats, lock),
            daemon=False
        )

        merge_thread.start()
        filter_thread.start()

        # Ждём завершения обоих потоков (второй сам ждёт первый)
        filter_thread.join()
        merge_thread.join()

        print("\nСтатистика:")
        print(f"- Просканировано файлов: {stats['files_scanned']}")
        print(f"- Файлов, содержащих слово '{search_word}': {stats['files_matched']}")
        print(f"- Слитый файл: {stats['merged_output']}")
        print(f"- Объём слитых данных: {human_bytes(stats['bytes_merged'])}")
        print(f"- Загружено запрещённых слов: {stats['forbidden_words']}")
        print(f"- Удалений (совпадений) запрещённых слов: {stats['removed_count']}")
        print(f"- Размер файла после фильтрации: {human_bytes(stats['bytes_after_filter'])}")
        print(f"- Время слияния: {stats['merge_time_sec']:.2f} c")
        print(f"- Время фильтрации: {stats['filter_time_sec']:.2f} c")
        print(f"- Ошибок: {stats['errors']}")
        if stats['errors_list']:
            print("\nСписок ошибок:")
            for e in stats['errors_list']:
                print(f"  {e}")

    except KeyboardInterrupt:
        print("\nПрервано пользователем.")
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
