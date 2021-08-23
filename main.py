import re
import matplotlib.pyplot as plt

# Parsing dataset
with open('dataset.txt', 'r') as dataset:
    word_scores = {}
    lines = dataset.readlines()
    for line in lines:
        entries = line.split('\t')
        score = float(entries[2]) - float(entries[3])
        if score == 0:
            continue
        words = entries[4].split(' ')
        for word in words:
            word = word[:word.index('#')]
            word_scores[word] = score

# Parsing input
with open('input.txt', 'r') as text:
    input_words = re.split(r'[ \n]', text.read())

    i = 0
    while i < len(input_words):
        input_words[i] = input_words[i].lower().strip('[".!,?:;[{()}]\'')
        if input_words[i] == '':
            del input_words[i]
            i -= 1
        i += 1

# Scoring input according to the dataset
scores = [0], [0]
sentiment_score = 0
word_count = 0
for word in input_words:
    if word in word_scores.keys():
        sentiment_score += word_scores[word]
        scores[0].append(word_count)
        scores[1].append(sentiment_score)
    word_count += 1

# Results
print(f'The text is {"positive" if sentiment_score > 0 else "negative"} with a score of {sentiment_score}.')

# Plotting
plt.title('Sentiment Score Progression')
plt.xlabel('Words')
plt.ylabel('Net Sentiment Score')
plt.plot([0, scores[0][-1]], [0, 0], color='grey')  # Base line (y=0)
plt.plot(scores[0], scores[1])  # Words vs. Net Sentiment Score
plt.show()
