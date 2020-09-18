class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if type(other) is Actor:
            return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):
        if type(other) is Actor:
            return self.__actor_full_name.lower() < other.__actor_full_name.lower()

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if colleague not in self.__colleagues:
            self.__colleagues.append(colleague)
        if self not in colleague.__colleagues:
            colleague.__colleagues.append(self)

    def check_if_this_actor_worked_with(self, colleague):
        return True if colleague in self.__colleagues else False


class TestActorMethods:
    def test_init(self):
        actor = Actor("Brad Pitt")
        actor1 = Actor("Angelina Jolie")
        actor1.add_actor_colleague(actor)
        assert actor1.check_if_this_actor_worked_with(actor) is True
        assert actor.check_if_this_actor_worked_with(actor1) is True
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None
