import random
import keyboard
import wikipedia


class Interface:

    def intro(self):
        # Introduce the program to the user
        print("Welcome to Easy Wikipedia Search Tool")
        # Introduce the difference between Wikipedia and this program
        print("You can quickly find relevant pages about your interested topic in any language")
        print("Click 1 to see abbreviation for each language, if not press 2 to continue")

    def keyboard(self):
        # Use keyboard library to make an interactive interface to the user
        while True:
            # When 1 is pressed open the language list
            if keyboard.is_pressed("1"):
                f = open("LanguageList")
                contents = f.read()
                print(contents)
                f.close()
                break
            # When 2 is pressed do not display the language list
            elif keyboard.is_pressed("2"):
                break

    def output(self):
        # Output the functions
        self.intro()
        self.keyboard()


class Scroll:
    def wiki(self):
        """
        This function writes all the information to WikipediaPages text file
        Organizes all the information
        """

        # input keyword, language and number of relevant pages
        inp = [input("\nWrite your key word: \n"),
               input("Write the abbreviation of the language you want to search in: \n"),
               int(input("Number of relevant pages you want to see about this topic: \n"))]

        user_search = inp[0]
        wikipedia.set_lang(inp[1])

        # Check if there are any relating words in the wikipedia's library in the selected language
        try:
            print(wikipedia.search(user_search))  # prints out the potential results
        except:
            print("The word you input is not present in your selected language.")
            print("Exiting from program, please rerun the program and try again with a meaningful word.")
            exit()

        max_search_result = len(wikipedia.search(user_search))

        # Double check if there is no item in the list
        if len(wikipedia.search(user_search)) != 0:
            print("Scroll through pages with right arrow, if you want to exit the code press esc.")
        else:
            print("The word you input is not present in your selected language.")
            print("Exiting from program, please rerun the program and try again with a meaningful word.")
            exit()

        # run through items in the list and select one word
        for i in range(0, inp[2]):
            while True:
                # trigger the outputting by pressing right arrow
                if keyboard.is_pressed("right"):
                    n = random.randint(1, max_search_result - 1)
                    try:
                        try:
                            # arranges to get data inside the page
                            b = wikipedia.search(user_search)[n]
                            user_search_format = wikipedia.page(b)

                            #
                            with open("WikipediaPages", "w") as p:
                                try:
                                    # prints out all the content of the page if format is right
                                    p.write(
                                        "Title:\n" + user_search_format.title + "\nURL:\n" + user_search_format.url + "\nSummary:\n" + user_search_format.summary
                                        + "\nContent\n" + user_search_format.content)
                                except:
                                    try:
                                        # prints out title, url and summary if the format is right
                                        p.write(
                                            "Title:\n" + user_search_format.title + "\nURL:\n" + user_search_format.url + "\nSummary:\n" + user_search_format.summary)
                                    except:
                                        # prints out title and url only
                                        p.write(
                                            "Title:\n" + user_search_format.title + "\nURL:\n" + user_search_format.url +
                                            "\n Only title and url of the page can be found please click to the "
                                            "link for further information")
                            break
                        except:
                            # prints out only the content
                            p.write(wikipedia.page(wikipedia.search(user_search)[n]).content)
                            break
                    except BaseException:
                        print("This page's format isn't properly designed, moving to next page...")
                        pass
                    break
                    # When escape is pressed exit the program
                elif keyboard.is_pressed("esc"):
                    break

    def output2(self):
        # Output the functions
        self.wiki()
