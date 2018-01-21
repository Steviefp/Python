import random
def test():
    char_list='a b c d e f g h i k l m n o p q r s t u v w x y z A B C D E F G H I J K M L M N O P Q R S T U V W X Y Z ! @ # $ % ^'.split()
    new_word=''
    for x in range(5):
        new_word += random.choice(char_list)
    return new_word

new=test()
print(new)
