import media
import fresh_tomatoes

# create the movie instances for each movie

guardians_of_the_galaxy = media.Movie(title="Guardians of the Galaxy",
                                      poster="https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                                      trailer="https://www.youtube.com/watch?v=B16Bo47KS2g")

star_wars = media.Movie(title="Star Wars: Episode IV: A New Hope",
                        poster="http://3g28wn33sno63ljjq514qr87.wpengine.netdna-cdn.com/"
                               "wp-content/uploads/2015/10/Star-Wars-Poster-700x1068.jpg",
                        trailer="https://www.youtube.com/watch?v=1g3_CFmnU7k")

zootopia = media.Movie(title="Zootopia",
                       poster="https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       trailer="https://www.youtube.com/watch?v=jWM0ct-OLsM")

lord_of_the_rings = media.Movie(title="Lord of the Rings: The Fellowship of the Ring",
                                poster="http://www.impawards.com/2001/posters/"
                                       "lord_of_the_rings_the_fellowship_of_the_ring_ver4.jpg",
                                trailer="https://www.youtube.com/watch?v=Pki6jbSbXIY")

arrival = media.Movie(title="Arrival",
                      poster="https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                      trailer="https://www.youtube.com/watch?v=tFMo3UJ4B4g")

the_lion_king = media.Movie(title="The Lion King",
                            poster="http://vignette3.wikia.nocookie.net/disney/images/c/cb/"
                                   "The_Lion_King_Textless_poster_1.jpg/revision/latest?cb=20140810104158",
                            trailer="https://www.youtube.com/watch?v=4sj1MT05lAA")

# put the movies into a list that can be passed to the fresh_tomatoes module

movies = [guardians_of_the_galaxy, star_wars, zootopia, arrival, the_lion_king, lord_of_the_rings]

# open the web page in the style specified by fresh_tomatoes

fresh_tomatoes.open_movies_page(movies=movies)
