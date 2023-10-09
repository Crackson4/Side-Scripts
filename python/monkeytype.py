import re

file_input = open("input.txt", "r").read()

words_html = re.findall(r"(?<=<div class=\"word\">).*?(?=</div>)", file_input)
words = " ".join(map(lambda x: "".join(re.findall(r">(\w)<", x)), words_html))
print(words)
