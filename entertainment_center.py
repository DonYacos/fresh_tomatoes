import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

dumb_and_dumber = media.Movie("Dumb and Dumber", "Hilarious story of two friends traveling to Aspen to return a briefcase full of money",
                              "http://img.moviepostershop.com/dumb-and-dumber-movie-poster-1994-1020191993.jpg",
                              "https://www.youtube.com/watch?v=l13yPhimE3o")

school_of_rock = media.Movie("School of Rock", "A down and out musician starts the school of rock",
                             "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

act_of_valor = media.Movie("Act of Valor", "Navy SEALS and their missions",
                           "http://cafmp.com/wp-content/uploads/2012/12/Act-of-Valor.jpg",
                           "https://www.youtube.com/watch?v=ZnlPgo9TaGo")

the_internship = media.Movie("The Internship", "Two forty somethings become interns at Google", 
                             "http://www.impawards.com/2013/posters/internship_ver8.jpg",
                             "https://www.youtube.com/watch?v=z6N27us5cWY")



movies = [toy_story, avatar, dumb_and_dumber, school_of_rock, act_of_valor, the_internship]
fresh_tomatoes.open_movies_page(movies)








