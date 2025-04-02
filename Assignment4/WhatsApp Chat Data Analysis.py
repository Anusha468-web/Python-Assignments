print("Welcome to the WhatsApp Application")
chat= [
    "Akki:Hey,Good morning..!",
    "Suji:Good morning..What's matter",
    "Akki:There is a release movie tommorow..",
    "Suji:Oh! Which movie.?",
    "Akki:It's OYE ✨",
    "Anus:That sounds good 🤩.Shall we go",
    "Akki:Yes that's why i messaged you",
    "Suji:Ok let's book tickets now 🎉",
]
message_count={}
while(True):
    print("=" * 30)
    print("Basic Message Analysis")
    print("=" * 30)
    print("1.Count the Total Messages in the Chat")
    print("2.Identify the Unique Users in the Chat")
    print("3.Count the Total Words in the Chat")
    print("4.Find the Average Words Per Message")
    print("5.Identify the Longest Message Sent")
    print("="*30)
    print("User-Specific Analysis")
    print("=" * 30)
    print("6.Find the Most Active User")
    print("7.Get Message Count for a Specific User")
    print("8.Find the Most Frequently Used Word by a User")
    print("9.Retrieve the First and Last Message Sent by a User")
    print("10.Check if a User is Present in the Chat")
    print("=" * 30)
    print("Time and Frequency Analysis")
    print("=" * 30)
    print("11.Find Commonly Repeated Words")
    print("12.Find Messages Containing a Specific Keyword")
    print("13.Identify the User with the Longest Average Message Length")
    print("14.Count How Many Messages Mention a Specific User")
    print("15.Display the First and Last Message in the Chat")
    print("=" * 30)
    print("Unique and Duplicate Data Handling")
    print("=" * 30)
    print("16.Remove Duplicate Messages")
    print("17.Find Commonly Used Phrases")
    print("18.Sort Messages Alphabetically")
    print("19.Display Messages in Reverse Order")
    print("20.Find Messages Containing Emojis")
    print("=" * 30)
    print("Complex Analysis and Insights")
    print("=" * 30)
    print("21.Find the Most Frequently Used Word in the Chat")
    print("22.Extract All Questions Asked in the Chat")
    print("23.Calculate the Reply Ratio Between Two Users")
    print("24.Check for Deleted Messages")
    print("25.Find Messages Sent After a Specific Keyword")
    print("=" * 30)
    print("=" * 30)

    option=input("Enter the option: ")
    if option=='1':
        total_messages = len(chat)
        print(f"Total messages in the chat: {total_messages}")
    elif option=='2':
        user=set()
        for msg in chat:
            users=msg.split(":")[0]
            user.add(users)
        print(f"unique user:{user}")
    elif option=='3':
        total=0
        for msg in chat:
            words=msg.split()
            total+=len(words)
        print(f"Total words:{total}")
    elif option=='4':
        print()
    elif option=='5':
        longest_msg = ""
        max_words = 0
        for msg in chat:
            word_count = len(msg.split())  # Counting words in the current message
            if word_count > max_words:
                max_words = word_count
                longest_message = msg

        print(f"The longest message sent: '{longest_msg}' with {max_words} words")
    elif option=='6':
        for message in chat:
            user = message[0]
            if user in message_count:
                message_count[user] += 1
            else:
                message_count[user] = 1
        most_active_user = max(message_count, key=message_count.get)
        print("Most Active User:", most_active_user)
    elif option=='7':
        user_name = input("Enter a user name to get message count: ")
        if user_name in message_count:
            print(f"{user_name} sent {message_count[user_name]} messages.")
        else:
            print(f"{user_name} has not sent any messages.")
    elif option=='8':
        user_name = input("Enter a user name to find most frequent word: ")
        word_count = {}
        for message in chat:
            if message[0] == user_name:
                words = message[1].split()
                for word in words:
                    word = word.lower()  # normalize to lowercase
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        if word_count:
            most_frequent_word = max(word_count, key=word_count.get)
            print(f"The most frequent word used by {user_name} is '{most_frequent_word}'")
        else:
            print(f"{user_name} has not sent any messages.")
    elif option=='9':
        user_name = input("Enter a user name to find most frequent word: ")
        word_count = {}
        for message in chat:
            if message[0] == user_name:
                words = message[0].split()
                for word in words:
                    word = word.lower()
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        if word_count:
            most_frequent_word = max(word_count, key=word_count.get)
            print(f"The most frequent word used by {user_name} is '{most_frequent_word}'")
        else:
            print(f"{user_name} has not sent any messages.")
    elif option=='10':
        user=input("Enter user name: ")
        if user in chat[0]:
            print(f"{user} present in chat")
        else:
            print("Not present")
    elif option=='11':
        fre={}
        for msg in chat:
            msgs=msg.split()
            for word in msgs:
                word=word.lower()
            if word in fre:
                fre[word]+=1
                print(fre)
    elif option=='12':
        keyword = input("Enter a keyword to search in messages: ")
        specific = [msg for msg in chat if keyword.lower() in msg.lower()]
        print("Messages containing the keyword:", specific)
    elif option=='13':
        user_avg_length = {}
        for user in set(message.split(":")[0].strip() for message in chat):
            user_messages = [message for message in chat if message.split(":")[0].strip() == user]
            avg_length = sum(len(msg.split()) for msg in user_messages) / len(user_messages)
            user_avg_length[user] = avg_length
        user_with_longest_avg = max(user_avg_length, key=user_avg_length.get)
        print(f"User with longest average message length: {user_with_longest_avg}")
    elif option=='14':
        user = input("Enter the user's name: ")
        mention_count = sum(user.lower() in message.lower() for message in chat)
        print(f"{user} is mentioned in {mention_count} messages.")
    elif option == '15':
        first = chat[1]
        last = chat[-1]
        print(first)
        print(last)
    elif option=='16':
        unique_msg=set(msg for msg in chat)
        print(unique_msg)
    elif option=='17':
        phrases = {}
        for message in chat:
            words = message.split()
            for i in range(len(words) - 1):
                phrase = f"{words[i]} {words[i + 1]}"
                phrases[phrase] = phrases.get(phrase, 0) + 1
        common_phrases = sorted(phrases.items(), key=lambda x: x[1], reverse=True)
        print(f"Common Phrases: {common_phrases[:5]}")
    elif option=='18':
        sort_msg=sorted(chat)
        print(sort_msg)
    elif option=='19':
        reverse_order=chat[::-1]
        print(reverse_order)
    elif option=='20':
        emoji_messages = [msg  for msg in chat if any(char in "😀😁😂🤣😃😄😅😆😉😊😋😎😜😝😛" for char in msg)]
        print("Messages containing emojis:", emoji_messages)
    elif option=='21':
        questions = [message for message in chat if '?' in message]
        print(f"Questions Asked: {questions}")
    elif option=='22':
        questions = []
        for msg in chat:
            if "?" in msg:
                questions.append(msg)
        print("Questions in the chat:")
        for msg in questions:
            print(msg)
    elif option == '23':
        user1 = input("Enter the first user's name: ")
        user2 = input("Enter the second user's name: ")
        replies = sum(1 for i in range(1, len(chat)) if chat[i - 1].split(":")[0].strip() == user1 and chat[i].split(":")[0].strip() == user2)
        total_user1_messages = sum(1 for message in chat if message.split(":")[0].strip() == user1)
        ratio = replies / total_user1_messages if total_user1_messages else 0
        print(f"Reply Ratio: {ratio:.2f}")
    elif option=='24':
        delete=[]
        for msg in chat:
            if 'This msg was deleatea' in msg:
                delete.append(msg)
        for msg in delete:
            print(delete)
        else:
            print("There is no deleted msgs")
    elif option == '25':
            # Find messages sent after a specific keyword
            keyword = input("Enter a keyword: ")
            index = next((i for i, message in enumerate(chat) if keyword.lower() in message.lower()), None)
            if index is not None:
                print("Messages after the keyword:")
                print(chat[index + 1:])
            else:
                print("Keyword not found.")

    elif option == 0:
        print("Exiting from application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 25.")





