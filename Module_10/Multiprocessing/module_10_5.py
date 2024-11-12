import time
import multiprocessing


def read_info(name):
    all_data = list()
    with open(name, 'r', encoding="utf-8") as file:
        for line in file:
            all_data.append(line)


file_names = [f"file {num}.txt" for num in range(1, 5)]

if __name__ == "__main__":
    first_timer = time.time()
    for file_name in file_names:
        read_info(file_name)
    first_timer_result = time.time() - first_timer

    second_timer = time.time()
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, file_names)
    second_timer_result = time.time() - second_timer

    print(f"Линейный: {first_timer_result}\n"
          f"Многопроцессный: {second_timer_result}")
