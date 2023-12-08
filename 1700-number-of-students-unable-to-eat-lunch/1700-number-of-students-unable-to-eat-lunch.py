class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count=Counter(students)
        for sandwich in sandwiches:
            if student_count[sandwich]>0:
                student_count[sandwich]-=1
            else:
                return student_count[not sandwich]
        return 0