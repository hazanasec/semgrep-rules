
# todoruleid:missing-hash-with-eq
class A:
    def __eq__(self, someother):
        pass


class A2:
    def __eq__(self, someother):
        pass

    def __hash__(self):
        pass