import json
import os
import random

def load_file():
    if os.path.exists("vocab.json"):
        with open("vocab.json","r") as file:
            return json.load(file)

def write_file(cases):
    with open("vocab.json","w") as file:
        json.dump(cases,file)

def missing_word(vocab):
    if not vocab:
        print("not words found")
        return
    return vocab

def view_all_words(vocab):
    if missing_word(vocab):
        for word,word_details in vocab.items():
            print(f"Word: {word}")
            print(f"Meaning: {word_details['Meaning']}")
            print(f"Example: {word_details['Example']}")

def add_new_word(vocab):
    word = input()
    if word in vocab:
        print("already exist")
        return
    meaning = input()
    example = input()
    vocab[word] = {
        "Meaning" : meaning,
        "Example" : example
    }
    write_file(vocab)
    print("word added")

def update_word_meaning(vocab):
    word = input()
    if word not in vocab:
        print("not found")
        return
    new_meaning = input()
    vocab[word]["Meaning"] = new_meaning
    write_file(vocab)
    print("meaning updated")

def delete_word(vocab):
    word = input()
    if word not in vocab:
        print("not found")
        return
    del vocab[word]
    write_file(vocab)
    print("word deleted")

def search_word(vocab):
    word = input()
    if word not in vocab:
        print("not found")
        return
    view_all_words({word:vocab[word]})

def quiz(vocab):
    words = list(vocab.items())
    random.shuffle(words)
    score = 0
    for word,word_details in words:
        print(f"Meaning: {word_details['Meaning']}")
        answer = input("What is the word: ")
        if answer.lower().strip() == word.lower().strip():
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    print(f"Your score: {score}")

def export_to_text(vocab):
    with open("vocab.txt","w") as file:
        for word,word_details in vocab.items():
            file.write(f"Word: {word}\n")
            file.write(f"Meaning: {word_details['Meaning']}\n")
            file.write(f"Example: {word_details['Example']}\n\n")

def main():
    vocab = load_file()
    while True:
        choice = int(input())
        if choice == 1:
            view_all_words(vocab)
        elif choice == 2:
            export_to_text(vocab)
        elif choice == 5:
            break

if __name__ == "__main__":
    main()