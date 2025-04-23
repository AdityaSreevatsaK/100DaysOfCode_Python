import requests
from flask import Flask, render_template

app = Flask(__name__)

blogs_api_url = "https://api.npoint.io/c790b4d5cab58020d391"

print("Day 57 - 100 Days of Code.")
print("Welcome to Blog Website.")


@app.route('/')
def home():
    """
    Renders the home page with a list of blogs.

    Returns:
        str: Rendered HTML template for the home page with the blog data passed as context.
    """
    return render_template(template_name_or_list='index.html', blogs_response=blogs_response)


@app.route('/post/<int:blog_number>')
def get_blog(blog_number):
    """
    Renders a specific blog post based on the blog number.

    Args:
        blog_number (int): The number of the blog to display.

    Returns:
        str: Rendered HTML template for the blog post with the blog data and blog number passed as context.
    """
    return render_template(template_name_or_list='post.html', blogs_response=blogs_response, blog_number=blog_number)


if __name__ == "__main__":
    blogs_response = requests.get(url=blogs_api_url).json()
    app.run(debug=True)  # add argument debug=True when you want to see the change upon saving.
