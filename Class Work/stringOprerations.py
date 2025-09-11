text = "hello world"

lowercaseText = text.lower()
uppercaseText = text.upper()
titleText = text.title()

#trimming whitespace
strippedText = text.strip()
leftStrippedText = text.lstrip()
rightStrippedText = text.rstrip()

#splitting and joining
words = strippedText.split(",")
joinedText = "-".join(words)