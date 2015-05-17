
class OldStyleClass:
    def __init__(self):
        pass


class NewStyleClass(object):
    def __init__(self):
        pass


osc = OldStyleClass()
print dir(osc)

nsc = NewStyleClass()
print dir(nsc)

