
# Write your code below:
from contextlib import contextmanager


@contextmanager
def generic(card_type, sender_name, recipient):
    print("Opening generic card.... ")
    card_file = open(card_type)
    new_card_order = open(f"{sender_name}_generic.txt", "w")
    try:
        new_card_order.write(f"Dear {recipient}, \n")
        new_card_order.write(card_file.read() + "\n")
        new_card_order.write(f"Sincerely, {sender_name} \n")
        yield new_card_order
    finally:
        card_file.close()
        new_card_order.close()


print("Task 1:")

with generic("thankyou_card.txt", "Mwenda", "Amanda") as new_card:
    print("Card Generated! \n")

with open("Mwenda_generic.txt", "r") as new_card1:
    print(new_card1.read())


class personalized:
    def __init__(self, sender_name, recipient_name):
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.opened_file = open(f"{sender_name}_personalized.txt", "w")

    def __enter__(self):
        self.opened_file.write(f"Dear {self.recipient_name}, \n")
        return self.opened_file

    def __exit__(self, *exc):
        self.opened_file.write(f"Sincerely, {self.sender_name}, \n")
        self.opened_file.close()


with personalized("John", "Michael") as personalized_card:
    personalized_card.write(
        "I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don't say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with open("John_personalized.txt", "r") as john_card:
    print(john_card.read())

with generic("happy_bday.txt", "Josiah", "Remy") as generic_card:
    with personalized("Josiah", "Esther") as personalized_card:
        personalized_card.write(
            "Happy Birthday! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can’t live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")

with open("Josiah_generic.txt", "r") as generic_card_readable:
    with open("Josiah_personalized.txt", "r") as personalized_readable:
        print(personalized_readable.read())
        print(generic_card_readable.read())



