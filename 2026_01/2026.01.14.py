# Markdown Link Parser
# Given the string of a link in Markdown, return the equivalent HTML string.
# 
# A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.
# 
# For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';
# 
# Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.

def parse_link(markdown):

    markdown_split = markdown.split("]")
    link_text = markdown_split[0][1::]
    link_url = markdown_split[1][1:-1]
    markdown_final = f'<a href="{link_url}">{link_text}</a>'

    return markdown_final

print(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)"))