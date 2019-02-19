# exercise 1
type_emotions = {'happy': '3', 'stress': '1', 'fear': '2'}

# exercise 2


class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        self.emotions = kwargs

    # exercise 3
    def what_emotions(self):
        for emotion, level in self.emotions.items():
            emotion_type = None
            if level == 1:
                emotion_type = 'low'
            if level == 2:
                emotion_type = 'medium'
            elif level == 3:
                emotion_type = 'high'
            else:
                emotion_type = ''

            print("{} is feeling very {} of the emotion {}.".format(
                self.name, emotion_type, emotion))


vithuyan = Person('vithuyan', happiness=3, stress=2, chill=5, serious=12)
vithuyan.what_emotions()
