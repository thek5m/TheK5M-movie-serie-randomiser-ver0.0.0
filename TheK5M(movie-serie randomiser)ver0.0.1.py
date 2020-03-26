import random
import time
import json




sorm = input("What do you wanna watch a Serie or a Movie: ")

def Movie():
    app = input("Enter automatic or manual: ")
    def manual():
        cat = input("enter category or top_15 or top_30_2020: ")
        if cat.lower() == "top_30_2020":
            top3019 = ["Booksmart", "The Farewell", "Parasite", "1917 ", "Avengers Endgame", "Blow the Man Down",
                       "Toy Story 4 ", "The Invisible Man", "Knives Out", "The Irishman", "The Farewell",
                       "Little Women", "Marriage Story", "A Beautiful Day in the Neighborhood",
                       "Spider-Man Far From Home", "If Beale Street Could Talk", "Once Upon a Time In Hollywood",
                       "Pain and Glory", "Shazam", "Ford v Ferrari", "Apollo 11", "Dolemite Is My Name", "Uncut Gems",
                       "They Shall Not Grow Old", "The Lighthouse", "Rocketman", "Amazing Grace", "Ash Is Purest White",
                       "John Wick Chapter 3 Parabellum", "The Peanut Butter Falcon", "Honeyland",
                       "Knock Down the House", "Honey Boy"]
            ch2019 = random.choice(top3019)
            if ch2019 == "If Beale Street Could Talk":
                print("[+]" + ch2019 + "[+]")
                print("[+]" + "link to watch:" + "https://cave.egybest.asia/movie/if-beale-street-could-talk-2018")
            elif ch2019 == "Apollo 11":
                print("[+]" + ch2019 + "[+]")
                print("[+]" + "link to watch:" + "https://cave.egybest.asia/movie/apollo-11-2019/")
            elif ch2019 == "They Shall Not Grow Old":
                print("[+]" + ch2019 + "[+]")
                print("[+]" + "link to watch:" + "http://live.cima4u.tv/Video/They+Shall+Not+Grow+Old+2018-28771.html")
            elif ch2019 == "Ash Is Purest White":
                print("[+]" + ch2019 + "[+]")
                print(
                    "[+]" + "link to watch:" + "https://best.egbest2.com/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-ash-is-purest-white-2018-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/")
            elif ch2019 == "Honeyland":
                print("[+]" + ch2019 + "[+]")
                print(
                    "[+]" + "link to watch:" + "https://my.egybest1.com/movies/%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D8%A9-%D9%81%D9%8A%D9%84%D9%85-honeyland-2019-%D9%85%D8%AA%D8%B1%D8%AC%D9%85/")
            elif ch2019 == "Knock Down the House":
                print("[+]" + ch2019 + "[+]")
                print("[+]" + "link to watch:" + "https://cave.egybest.asia/movie/knock-down-the-house-2019")
            elif ch2019 == "1917 ":
                print("[+]" + ch2019 + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + ch2019.replace(" ", "-") + "مترجم")
            else:
                print("[+]" + ch2019 + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + ch2019.replace(" ", "-"))

        elif cat.lower() == "category":
            print("choose a category:")
            print("1 - Action & Adventure.")
            print("2 - Animation.")
            print("3 - Comedy.")
            print("4 - Documentary.")
            print("5 - Drama.")
            print("6 - Horror.")
            print("7 - Kids & Family.")
            print("8 - Romance.")
            print("9 - Science fiction & Fantasy.")
            num = input("enter a number :")
            if num == "1":
                Action = ["Black Panther", "Avengers Endgame", "Mission Impossible Fallout",
                          "Spider Man Into The Spider Verse", "Mad Max Fury Road", "Wonder Woman",
                          "Wonder Woman Bloodlines", "Dunkirk"]
                action_ran = random.choice(Action)
                print("[+]" + action_ran + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + action_ran.replace(" ", "-"))
            elif num == "2":
                Anime = ["Toy Story 4", "Inside Out", "Coco", "Incredibles 2", "How to Train Your Dragon Homecoming",
                         "I Lost My Body", "Klaus"]
                anime_ran = random.choice(Anime)
                print("[+]" + anime_ran + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + anime_ran.replace(" ", "-"))
            elif num == "3":
                Comedy = ["The Farewell", "Fighting with My Family", "Booksmart", "Once Upon a Time In Hollywood",
                          " Good Boys", "The Dead Don’t Die", "Jojo Rabbit"]
                com_ran = random.choice(Comedy)
                print("[+]" + com_ran + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + com_ran.replace(" ", "-"))
            elif num == "4":
                doc = ["cats_the_mewvie", "For Sama", "Last Breath", "The Magic Pill", "The Great Hack"]
                doc_ran = random.choice(doc)
                print("[+]" + doc_ran + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + doc_ran.replace(" ", "-"))
            elif num == "5":
                drama = ["The Rhythm Section", "The Song of Names", "Clemency", "A Hidden Life", "Only", "Becoming",
                         "Swallow"]
                dra_ran = random.choice(drama)
                print("[+]" + dra_ran + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + dra_ran.replace(" ", "-"))
            elif num == "6":
                hor = ["Siccin 2", "Us", " Get Gone", "Ready or Not", "Midsommar", "Harpoon"]
                hor_ran = random.choice(hor)
                if hor_ran == "Siccin 2":
                    print("[+]" + hor_ran + "[+]")
                    print("[+]" + "link to watch:" + "https://cave.egybest.asia/movie/siccin-2-2015/")
                else:
                    print("[+]" + hor_ran + "[+]")
                    print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + hor_ran.replace(" ", "-"))
            elif num == "7":
                fam = ["Cats", "My Spy", "Go", "Epiphany", "Maleficent Mistress of Evil", "Troop Zero",
                       "Anastasia: Once Upon a Time"]
                fam_ran = random.choice(fam)
                print("[+] " + fam_ran + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + fam_ran.replace(" ", "-"))
            elif num == "8":
                romance = ["A Hidden Life", "Just One More Kiss", "Baby Jane", "Little Women", "All The Bright Places",
                           "Eat Brains Love"]
                rom_ran = random.choice(romance)
                print("[+]" + rom_ran + "[+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + rom_ran.replace(" ", "-"))
            elif num == "9":
                fant = ["The Room", "The Alpha Test", "The Blood Alligator", "Ready Player One", "Dark Encounter",
                        "In the Shadow of the Moon"]
                fan_ran = random.choice(fant)
                print("[+]" + fan_ran + " [+]")
                print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + fan_ran.replace(" ", "-"))

        elif cat.lower() == "top_15":
            top15 = ["Miss Fisher and the crypt of tears", "the shawshank redemption", "The Godfather",
                     "Batman the dark knight", "Pulp Fiction", "Human capital", 'Inception', "Fight club", "Joker",
                     "Harakiri 1962", "Parasite", "Interstellar", "1917", "Se7en", " the silence of the lambs"]
            top15_ran = random.choice(top15)
            print("[+]" + top15_ran + "[+]")
            print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + top15_ran.replace(" ", "-"))


        else:
            print("Please Rerun the Script!")

    def auto():
        automa = ["Booksmart", "The Farewell", "Parasite", "1917 ", "Avengers Endgame", "Blow the Man Down",
                  "Toy Story 4 ", "The Invisible Man", "Knives Out", "The Irishman", "The Farewell", "Little Women",
                  "Marriage Story", "A Beautiful Day in the Neighborhood", "Spider-Man Far From Home",
                  "If Beale Street Could Talk", "Once Upon a Time In Hollywood", "Pain and Glory", "Shazam",
                  "Ford v Ferrari", "Apollo 11", "Dolemite Is My Name", "Uncut Gems", "They Shall Not Grow Old",
                  "The Lighthouse", "Rocketman", "Amazing Grace", "Ash Is Purest White",
                  "John Wick Chapter 3 Parabellum", "The Peanut Butter Falcon", "Honeyland", "Knock Down the House",
                  "Honey Boy", "Miss Fisher and the crypt of tears", "the shawshank redemption", "The Godfather",
                  "Batman the dark knight", "Pulp Fiction", "Human capital", 'Inception', "Fight club", "Joker",
                  "Harakiri 1962", "Parasite", "Interstellar", "1917", "Se7en", " the silence of the lambs"]
        hey = random.choice(automa)
        if hey == "If Beale Street Could Talk":
            print("[+]" + hey + "[+]")
            print("[+]" + "link to watch:" + "https://cave.egybest.asia/movie/if-beale-street-could-talk-2018")
        elif hey == "Apollo 11":
            print("[+]" + hey + "[+]")
            print("[+]" + "link to watch:" + "https://cave.egybest.asia/movie/apollo-11-2019/")
        elif hey == "They Shall Not Grow Old":
            print("[+]" + hey + "[+]")
            print("[+]" + "link to watch:" + "http://live.cima4u.tv/Video/They+Shall+Not+Grow+Old+2018-28771.html")
        elif hey == "Ash Is Purest White":
            print("[+]" + hey + "[+]")
            print(
                "[+]" + "link to watch:" + "https://best.egbest2.com/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-ash-is-purest-white-2018-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/")
        elif hey == "Honeyland":
            print("[+]" + hey + "[+]")
            print(
                "[+]" + "link to watch:" + "https://my.egybest1.com/movies/%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D8%A9-%D9%81%D9%8A%D9%84%D9%85-honeyland-2019-%D9%85%D8%AA%D8%B1%D8%AC%D9%85/")
        elif hey == "Knock Down the House":
            print("[+]" + hey + "[+]")
            print("[+]" + "link to watch:" + "https://cave.egybest.asia/movie/knock-down-the-house-2019")
        elif hey == "1917 ":
            print("[+]" + hey + "[+]")
            print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + hey.replace(" ", "-") + "مترجم")
        else:
            print("[+]" + hey + "[+]")
            print("[+]" + "link to watch:" + "https://www.شبح.com/en/" + hey.replace(" ", "-"))




    if app.lower() == "manual":
        manual()
    elif app.lower() == "automatic":
        auto()


def Serie():
    sseri = ["Dark 2017" , "Sex Education ", "rick and morty" , "Mr Robot","Lucifer", "Elite" , "for life", "I Am Not Okay with This","The End of the Fucking World" , "vikings" , "peaky-blinders", " Breaking Bad"]
    ss_ran = random.choice(sseri)
    if ss_ran == "Dark 2017":
        print("[+]" + ss_ran + "[+]")
        print("[+]" + "link to watch:" + "https://www.شبح.com/en/series/peaky-blinders/")
    elif ss_ran == "The End of the Fucking World":
        print("[+]" + ss_ran + "[+]")
        print("[+]" + "link to watch:" + "https://www.شبح.com/en/series/the-end-of-the-fing-world/")
    elif ss_ran == "peaky-blinders":
        print("[+]" + ss_ran + "[+]")
        print("[+]" + "link to watch:" + "https://www.شبح.com/en/series/peaky-blinders-season-5-2019/")
    else:
        print("[+]" + ss_ran + "[+]")
        print("[+]" + "link to watch:" + "https://www.شبح.com/en/series/" + ss_ran.replace(" ", "-"))

if sorm.lower() == "movie":
    Movie()
elif sorm.lower() == "serie":
    Serie()
else:
    exit()