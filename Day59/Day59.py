import requests
from flask import Flask, render_template

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    """
    Fetches all blog posts and renders the homepage.

    Returns:
        str: Rendered HTML template for the homepage with all blog posts.
    """
    return render_template(template_name_or_list="index.html", all_posts=posts)


@app.route("/about")
def about():
    """
    Renders the "About" page.

    Returns:
        str: Rendered HTML template for the "About" page.
    """
    return render_template(template_name_or_list="about.html")


@app.route("/contact")
def contact():
    """
    Renders the "Contact" page.

    Returns:
        str: Rendered HTML template for the "Contact" page.
    """
    return render_template(template_name_or_list="contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    """
    Renders a specific blog post based on its ID.

    Args:
        index (int): The ID of the blog post to display.

    Returns:
        str: Rendered HTML template for the specific blog post.
    """
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template(template_name_or_list="post.html", post=requested_post)


if __name__ == "__main__":
    app.run(port=5000)
