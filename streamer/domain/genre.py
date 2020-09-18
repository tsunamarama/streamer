class Genre:
    def __init__(self, genre_type: str):
        if genre_type == "" or type(genre_type) is not str:
            self.__genre_type = None
        else:
            self.__genre_type = genre_type.strip()

    @property
    def genre_type(self) -> str:
        return self.__genre_type

    def __repr__(self):
        return f"<Genre {self.__genre_type}>"

    def __eq__(self, other):
        if type(other) is Genre:
            return self.__genre_type == other.__genre_type

    def __lt__(self, other):
        if type(other) is Genre:
            return self.__genre_type.lower() < other.__genre_type.lower()

    def __hash__(self):
        return hash(self.__genre_type)


class TestGenreMethods:
    def test_init(self):
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"
        genre2 = Genre("")
        assert genre2.genre_type is None
        genre3 = Genre(42)
        assert genre3.genre_type is None