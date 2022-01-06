import requests


def work():
    word = str(requests.get("https://random-word-api.herokuapp.com/word?number=1").json()[0])
    ans = "_"*len(word)
    lives = 5
    while lives > 0 and '_' in ans:
        print("lives: ", lives)
        print(ans)
        n = str(input("Guess the character: "))
        if n in word:
            ind = [i for i, w in enumerate(word) if w == n]
            for i in ind:
                if ans[i] == "_":
                    ans = ans[:i] + n + ans[i+1:]
                    break
        else:
            lives -= 1
    if lives == 0:
        print("\nYou failed! :/\nCorrect word was: ", word)
    else:
        print("Congratulations, you won! :)")


if __name__ == '__main__':
    work()
