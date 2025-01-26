import random
import os
import termcolor

questions = dict()


def get_questions():

    print("Введи название файла:", end=" ")
    file_name = input()
    print("Сколько решеток у вопроса?", end=" ")
    lattices_count = int(input())

    try:
        with open(file_name, "r", encoding="utf-8") as file:

            answer = ""
            question = ""

            for line in file:
                if lattices_count * "#" in line and not (lattices_count + 1) * "#" in line:
                    if answer != "":
                        if question == "":
                            question = line
                        questions[question] = answer
                        answer = ""

                        question = line

                else:
                    answer += line

            questions[question] = answer

            print(f"Загружено {len(questions)} вопросов")

    except FileNotFoundError:
        print("Файл не найден. Попробуйте еще раз.")
        get_questions()

def random_question():
    try:
        return random.choice(list(questions.keys()))
    except:
        return None


def start_asking():
    question_number = 1
    while True:
        os.system("clear")
        question = random_question()

        if question is None:
            print("Вопросы закончились! Чтобы начать новый круг вопросов, запустите программу заново.")
            return

        try:
            print(termcolor.colored(f"\nВопрос №{question_number}:", color="light_green"))
            print(termcolor.colored(question, color="light_green"), end="")
            input()
            print(questions[question], end="")
            questions.pop(question)
            question_number += 1
            input(termcolor.colored(f"Осталось {len(questions)} вопросов. Чтобы получить следующий вопрос, нажмите <enter>", color="light_green"))

        except KeyboardInterrupt:
            print("\nПрограмма завершена.")
            return


if __name__ == "__main__":
    print("Привет! Это скрипт для получения рандомных вопросов с ответами из .md файлов.")
    print("После того как ты увидишь вопрос, чтобы получить ответ, нужно нажать <enter>.\n")
    get_questions()
    start_asking()