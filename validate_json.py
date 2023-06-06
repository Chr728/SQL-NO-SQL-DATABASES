import json

def validate(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        i = 0
        while line := file.readline():
            i += 1
            try:
                json.loads(line.rstrip())
            except json.decoder.JSONDecodeError:
                print("Line number " + str(i) + " is invalid")

if __name__ == "__main__":
    print('In Reddit.json')
    validate("results\\reddit.json")
    print('\nIn Tweets.json')
    validate("results\\tweets.json")