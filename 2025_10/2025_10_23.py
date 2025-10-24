# Favorite Songs
# Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.
# 
# Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.
# 
# Each object will have a "title" property (string), and a "plays" property (integer).

def favorite_songs(playlist):

        big: int = 0
        less_big: int = 0

        top_dog:str = ""
        lesser_dog:str = ""

        for dictionary in playlist:

                if dictionary["plays"] > big:

                        less_big = big
                        lesser_dog = top_dog

                        big = dictionary["plays"]
                        top_dog = dictionary["title"]

                elif dictionary["plays"] > less_big:
                        
                        less_big = dictionary["plays"]
                        lesser_dog = dictionary["title"]

        result = [top_dog, lesser_dog]

        return result


print(favorite_songs([{"title": "Skip Track", "plays": 98},
                       {"title": "99 Downloads", "plays": 99},
                         {"title": "Clickwheel Love", "plays": 100} ]))