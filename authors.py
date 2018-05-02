from database import CursorFromConnectionFromPool

class Authors:
    def __init__(self, name, bio, id):
        self.name = name
        self.bio = bio
        self.id = id

    def __repr__(self):
        return "Name ---> {}".format(self.name)

    @classmethod
    def get_author(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('select name from authors')
            author_data = cursor.fetchall()
            return author_data
            # return cls(name=author_data[0],
            #            bio=author_data[1],
            #            id=author_data[2])
