# ACM Research Coding Challenge (Fall 2021) - Jack Myrick

## Overview
My method of sentiment analysis rated the given text overall as positive with a score of 9.75. This means the passage had a positive sentiment as a whole.

## Method
I used a knowledge-based approach to rate the sentiment of the passage. I used the [SentiWordNet](https://github.com/aesuli/SentiWordNet/blob/master/data/SentiWordNet_3.0.0.txt) dataset, which contains the positivity and negativity of many words in the English language. My program parses through the dataset and stores the net score for every word with a non-zero net score. Next, the program parses through the input passage and adds each word's net score to the overall sentiment score. As such, this method is a [bag-of-words model](https://en.wikipedia.org/wiki/Bag-of-words_model), since the order of the passage does not affect the final score. As a result, my method does not handle context or negation, some important limitations. If the final sentiment score is greater than 0, the passage has a positive sentiment. Else, it has a negative sentiment.

## Details
In addition to the final score, my method gives a graph from [Matplotlib](https://matplotlib.org/) of the net sentiment score as the passage progresses through each word. The graph is shown below.

![image](https://user-images.githubusercontent.com/63320517/130508052-ee4e4fdc-0896-44f5-95b6-aa0a9148000a.png)

## Reflection
Reading through the passage myself, I expected a positive score overall, which aligns with my model's evaluation. Additionally, I did notice that the passage starts out somewhat negatively in its description of the dream and the conflict that was the argument. The graph above reflects my observation in the model's evaluation. Once the argument ends and the description of the person's character begins, the graph noticeably increases at around word 300. This aligns well with my interpretation of the sentiment of the character description as I saw it as positive and laudatory. 

Despite the somewhat naive approach taken, the model seems to judge the sentiment of the passage reasonably well. I suspect that positive and negative inacurracies due to context and negation balance out in a sufficiently long text, leading to a relatively accurate sentiment score.
