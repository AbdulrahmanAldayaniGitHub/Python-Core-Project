class Student:
    def __init__(self, name, student_id, scores=None):
        if scores is None:
            scores = []
        self.name = name
        self.student_id = student_id
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def calculate_grade(self):
        avg_score = sum(self.scores) / len(self.scores)
        if avg_score >= 90:
            return 'A'
        elif avg_score >= 75:
            return 'B'
        elif avg_score >= 50:
            return 'C'
        else:
            return 'F'

def main():
    student1 = Student("John Doe", 101)
    student1.add_score(85)
    student1.add_score(92)
    print(f"{student1.name}'s Grade: {student1.calculate_grade()}") 