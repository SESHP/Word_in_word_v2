from utils import load_random_word, worder
from Basic import Player, BasicWord

word = load_random_word()
name = input('Введите Ваше имя: ')
print(f'Привет, {name}')
print(f'Составьте {word.count_subwords()} слов из слова {word.word}')
print('Слова должны быть не короче 3 букв')
print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
print('Поехали, ваше первое слово?')

player = Player(name)
counter = word.count_subwords()
while counter > 0:
    answer = input('Введите ответ: ').lower()
    if answer == 'стоп' or answer == 'stop':
        if len(player.wordsin) > 0:
            print(f'Игра завершена, вы угадали {len(player.wordsin)} {worder(len(player.wordsin))}')
        else:
            print('Игра окончена')
        break
    
    if len(answer) < 3:
        print('Слишком короткое слово')
    elif word.valid(answer) == False:
        print('неверно')
    elif player.uset_word(answer) == True:
        print('уже использовано')
    else:
        print('Верно')
        player.append_words(answer)
        counter -= 1
if counter == 0:
    print(f'Игра окончена, вы угадали все {len(player.wordsin)} {worder(len(player.wordsin))}')
        

    
    