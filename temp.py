import emoji
messages = ['😊🎉', 'Hi there! 😊', 'No emojis here!', '🔥🔥😊']
emoji_count=[]
for i in messages:
    emoji_count.append(emoji.emoji_count(i))
print(emoji_count)