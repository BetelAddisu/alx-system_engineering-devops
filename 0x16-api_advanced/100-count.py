#!/usr/bin/python3
import requests

def count_words(subreddit, word_list):
    cleaned_word_list = [word.lower() for word in word_list]  # convert all words to lowercase
    counts = {}  # dictionary to store the count of each word
    
    # Query Reddit API and retrieve hot articles from the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        
        # Parse the title of each article and count the occurrences of words
        for article in articles:
            title = article['data']['title'].lower()
            for word in cleaned_word_list:
                if word in title:
                    counts[word] = counts.get(word, 0) + title.count(word) 
        
        # Print the sorted count of each word
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))  # sort by count (descending) and word (ascending)
        for count in sorted_counts:
            print(f"{count[0]}: {count[1]}")
    else:
        print("Invalid subreddit or no posts match.")
