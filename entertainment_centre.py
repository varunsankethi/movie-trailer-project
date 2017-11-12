import media
import fresh_tomatoes

toy_story = media.Movie("Toy_Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

inception = media.Movie("Inception",
                         "Mind over matter",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=8hP9D6kZseM")

beautiful_mind = media.Movie("A Beautiful Mind",
                         "Biopic of John Nash",
                         "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                         "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

the_dark_knight  = media.Movie("The Dark Knight",
                         "Batman versus Joker",
                         "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                         "https://www.youtube.com/watch?v=yQ5U8suTUw0")

the_dark_knight_rises  = media.Movie("The Dark Knight Rises",
                         "Batman versus Bane",
                         "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                         "https://www.youtube.com/watch?v=g8evyE9TuYk")

movies = [toy_story, avatar, inception, beautiful_mind, the_dark_knight, the_dark_knight_rises]
fresh_tomatoes.open_movies_page(movies)
