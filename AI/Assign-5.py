import nltk 
#nltk.download("all")
from nltk.chat.util import Chat,reflections
pairs = [
    [
        r"Hi|Hello|Hey|Hola",
        ["Hello , How can i help you?",]
    ],
    [
        r"recommendations|suggest|suggestions|help|bestsellers",
        [" American cheese supreme , Triple cheese, Maharaj Mac",]
    ],
    [
        r"hungry",
        ["We have the best burgers which may help you satisfy your hunger.",]
    ],
    [
        r"menu",
        ["1.American Cheese Supreme 2.Maharaja Mac 3.Triple American 4.Cheese Metldown 5.Boss Whopper ",]
    ],
    [
        r"order",
        ["You can place you order online thorugh our website or you can download our app.",]
    ],
    [
        r"dine|take-away",
        ["Yes we have dine in and take away as options.",]
    ],
    [
        r"outlets|branches|franchise",
        ["We have our outlets at 1.Satara road 2.JM road 3.Senapati Bapat road 4.Paud road",]
    ],
    [
        r"thanks|thank you|okay|bye|goodbye",
        ["We hope that this conversation was helpful.",]
    ],
]

def chat():
  print("Hey there!! My name is BugerMonster how may i help you?")
  chat = Chat(pairs)
  chat.converse()

if __name__ == "_main_":
  chat()