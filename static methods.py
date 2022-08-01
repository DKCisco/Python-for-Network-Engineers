import random
skills = ['networking', 'linux', 'cloud', 'python', 'golang', 'MySQL']

class NewTrainer:
    def __init__(self, skill):
        self._skill = skill

    @property
    def skill(self):
        return self._skill

    @staticmethod
    def random_skill():
        return NewTrainer(random.choice(skills))

new_cbtn_person = NewTrainer.random_skill()

print(new_cbtn_person._skill)