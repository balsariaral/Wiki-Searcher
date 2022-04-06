import random
import keyboard
import wikipedia

print("Welcome to Easy Wikipedia Search Tool")
print("You can quickly find relevant pages about your interested topic in any language ")
print("Click 1 to see abbreviation for each language, if not press 2 to continue")

while True:
    if keyboard.is_pressed("1"):
        f = open("LanguageList")
        contents = f.read()
        print(contents)
        f.close()
        break
    elif keyboard.is_pressed("2"):
        break

inp = [input("\nWrite your key word: \n"), input("Write the abbreviation of the language you want to search in: \n"),
       int(input("Number of relevant pages you want to see about this topic: \n"))]

user_search = inp[0]
wikipedia.set_lang(inp[1])

print(wikipedia.search(user_search))  # prints out the potential results

max_search_result = len(wikipedia.search(user_search))

print("Scroll through pages with right arrow, if you want to exit the code press esc.")

for i in range(0, inp[2]):
    while True:
        if keyboard.is_pressed("right"):
            n = random.randint(1, max_search_result - 1)
            try:
                try:
                    b = wikipedia.search(user_search)[n]
                    user_search_format = wikipedia.page(b)  # arranges to get data inside the page
                    with open("WikipediaPages", "w") as p:
                        p.write(
                            user_search_format.title + "\n" + user_search_format.url + "\n" + user_search_format.summary
                            + "\n" + user_search_format.content)  # prints out all the content of the page
                    break
                except:
                    p.write(wikipedia.page(wikipedia.search(user_search)[n]).content)
                    break
            except BaseException:
                pass
            break

        elif keyboard.is_pressed("esc"):
            break
