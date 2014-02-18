#!python

class AscendancyDatastore():

    pass


class Ascendancy():

    def __init__(self, datastore=AscendancyDatastore):
        self.datastore = datastore

    def index(self):
        return "Ascendancy Chess System", { }

    def get_player(self, id):

        return [], []
