# Making an API Request:

# Use Python's requests library to fetch data from a sample API.
# Use this free placeholder API for testing:
# https://jsonplaceholder.typicode.com/posts/1
# Write a function get_post() that:
# Fetches the post data from the above API.
# Prints the title and body of the post.

# Parsing JSON Data:

# Extend get_post() to parse the JSON response and extract the following:
# title
# body
# Format the output to look like:
# ```
# Post Title: <title>
# Post Body: <body>
# ```


# Bonus Task (Optional):

# Write a function get_all_posts() that fetches all posts from the API (https://jsonplaceholder.typicode.com/posts).
# Save the titles of all posts to a file named posts_titles.txt, with one title per line.

# Tips:
# Use the requests.get() method to make the API request.
# Use the .json() method on the response to parse the JSON data.
# For the bonus task, use a loop to iterate over the JSON data and write to the file.

import requests

def get_post(url):
    response = requests.get(url)
    if response.status_code == 200:  
        post_data = response.json()
        title = post_data.get("title")
        body = post_data.get("body")
        print(f"Post Title: {title}")
        print(f"Post Body: {body}")
    else:
        print("Failed to retrieve data:", response.status_code)


get_post("https://jsonplaceholder.typicode.com/posts/1")



def get_all_posts(url):
    response = requests.get(url)  
    if response.status_code == 200:  
        posts_data = response.json()  
        with open("posts_titles.txt", "w") as file:  
            for post in posts_data:
                title = post.get("title")  
                file.write(title + "\n")   
    else:
        print("Failed to retrieve data:", response.status_code)


get_all_posts("https://jsonplaceholder.typicode.com/posts")
