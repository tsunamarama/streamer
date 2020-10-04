from streamer.domain.movie import Movie


class WatchList:
    def __init__(self):
        self.__watchlist = []

    @property
    def watchlist(self) -> list:
        return self.__watchlist

    def add_movie(self, movie: Movie):
        if movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        if -1 <= index < len(self.__watchlist):
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self) -> Movie:
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]
