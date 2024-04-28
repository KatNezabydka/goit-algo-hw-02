from queue import Queue
import random


class ClientRequest:
    """
        Потрібно розробити програму, яка імітує приймання й обробку заявок:
        програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними),
        додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.
    """

    def __init__(self):
        self.requests = Queue()

    def generate_request(self, value):
        self.requests.put(value)

    def process_request(self):
        if not self.requests.empty():
            requests = self.requests.get()
            print(f"Обслуговуємо заявку {requests}")
        else:
            print(f"Черга пуста")


new_request = ClientRequest()

while True:
    number = int(input("Введіть число (введіть 0 для завершення): "))
    new_request.generate_request(number)
    new_request.process_request()
    if number == 0:
        print("Програма завершила свою роботу.")
        break
