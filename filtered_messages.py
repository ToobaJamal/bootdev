'''
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. 
It takes a list of chat messages as input and returns 2 new lists:

A list of the same messages but with all instances of the word dang removed.
A list containing the number of dang words that were removed from the message at that particular index.
'''

def filter_messages(messages):
    filetered_messages = []
    counters = []
    for i in messages:
        words_in_message = i.split()
        non_bad_words = []
        counter = 0
        for i in words_in_message:
            if i == "dang":
                counter += 1
            else:
                non_bad_words.append(i)
        clean_message = " ".join(non_bad_words)
        filetered_messages.append(clean_message)
        counters.append(counter)
    return filetered_messages, counters
        


# Don't edit below this line


def main():
    messages = [
        "well dang it",
        "dang the whole dang thing",
        "kill that knight, dang it",
        "get him!",
        "donkey kong",
        "oh come on, get them",
        "run away from the dang baddies",
    ]
    filtered_messages, words_removed = filter_messages(messages)
    if len(filtered_messages) != len(words_removed):
        print("filtered_messages and words_removed lists should be the same size")
        return
    for i in range(0, len(filtered_messages)):
        print(
            f"Removed {words_removed[i]} words. Censored text: '{filtered_messages[i]}'"
        )


main()
