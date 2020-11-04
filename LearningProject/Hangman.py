import random

class hangmanSeries:
    def pick_word(self, dir):
        words = []
        with open(dir, 'r') as dict:
            text = dict.readline().strip()
            while text:
                words.append(text)
                text = dict.readline()
        return random.choice(words)
    def guess_letter(self, word):
        print('Welcome to Hangman')
        word = list(word)
        print(len(word))
        act_word = '_'*(len(word)-1)
        act_word = list(act_word)
        print(len(act_word))
        gue_word = []
        letter = input('Guess Your Letter: ').upper()
        guess = 1
        while True:
            if letter in gue_word:
                letter = ''
                print('Already Guessed!!!!')
            elif letter in word:
                index = word.index(letter)
                act_word[index] = letter
                word[index] = '_'
            else:
                print(''.join(act_word))
                if letter != '':
                    gue_word.append(letter)
                letter = input('Guess Your Letter: ').upper()
                guess += 1
            if '_' not in act_word:
                print('Yay, You Win!!! with', guess, 'guesses')
                break

if __name__ == "__main__":
    hang = hangmanSeries()
    rand_word = hang.pick_word('/home/syed/Documents/PyDocs/sowpods.txt')
    hang.guess_letter(rand_word)