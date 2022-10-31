'''
Process both files line-by-line in order to replace the words from the first file in the short story with the string "____" (four underscores).
Then, print the resulting story, each line of the story on its own line.
'''

words_file_name = "words.txt"
story_file_name = "story.txt"
'''
words_file = open(words_file_name)
words_list = words_file.read().split()
words_file.close()

story_file = open(story_file_name)

story_text = story_file.read().strip()

for word in words_list:
    story_text = story_text.replace(word, "____")

print(story_text)


story_file.close()
'''

words_file = open(words_file_name)
words_list = []
for word in words_file:
    word = word.strip()
    words_list.append(word)
    
words_file.close()

story_file = open(story_file_name)

for line in story_file:
    line = line.strip()
    for word in words_list:
        line = line.replace(word, "____")
    print(line)

story_file.close()