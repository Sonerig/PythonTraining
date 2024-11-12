import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding="utf-8") as file:
        for counter in range(word_count):
            file.write(f"Какое-то слово № {counter + 1}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


funcs_time_start = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

print(f"На выполнение работы функций ушло: {int(time.time() - funcs_time_start)} сек.")

threads = [threading.Thread(target=write_words, args=(10, "example5.txt")),
           threading.Thread(target=write_words, args=(30, "example6.txt")),
           threading.Thread(target=write_words, args=(200, "example7.txt")),
           threading.Thread(target=write_words, args=(100, "example8.txt"))]

threads_time_start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"На выполнение работы потоков ушло: {int(time.time() - threads_time_start)} сек.")
