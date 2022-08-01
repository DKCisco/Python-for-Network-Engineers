class Student:
    
    def __init__(self, name, studentnum):
        self._name = name
        self._studentnum = studentnum

    @property
    def name(self):
        return self._name

    @property
    def studentnum(self):
        return self._studentnum

    @name.setter
    def name(self, name):
        if len(name) < 2:
            raise ValueError("Name must be atleast 2 characters.")
        self._name = name

    @studentnum.setter
    def studentnum(self, studentnum):
        if not isinstance(studentnum, int):
            raise ValueError("Student number must be an integer")

        self._studentnum = studentnum