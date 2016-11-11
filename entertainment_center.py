import media
import fresh_tomatoes

'''
This class creates a list of Movie objects and uses fresh_tomatoes.py
to auto-generate content
'''

avatar = media.Movie(
    "Avatar",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

spotlight = media.Movie(
    "Spotlight",
    "https://www.youtube.com/watch?v=rfm_wJFerfA"
    )

deadpool = media.Movie(
    "Deadpool",
    "https://www.youtube.com/watch?v=ONHBaC-pfsk"
    )

strange = media.Movie(
    "Doctor Strange",
    "https://www.youtube.com/watch?v=HSzx-zryEgM"
    )

dory = media.Movie(
    "Finding Dory",
    "https://www.youtube.com/watch?v=TAXZRz_j5AQ"
    )

accountant = media.Movie(
    "The Accountant",
    "https://www.youtube.com/watch?v=DBfsgcswlYQ"
    )


movies = [avatar, spotlight, deadpool, strange, dory, accountant]

fresh_tomatoes.open_movies_page(movies)
