####################
# Creator: Alex Bevan - UP2198095
# Date: 8/2/24
# Name: Module Grades Calculator
# Version: 2
# Changes: Created an Assessment class to calculate overall score of the current assessment - simplifying the loop
####################


class Assessment:

    def __init__(self, mark, weighting):
        self.mark = mark
        self.weighting = weighting

    def calculateOverall(self):
        self.weighting = self.weighting / 100
        overall = self.mark * self.weighting
        return overall

    def __str__(self):
        return f'Assessment object'


def main():
    totalWeighting = 0
    totalMark = 0

    numberOfAssessments = int(input('Please enter the number of assessments to calculate from:\t'))
    for i in range(numberOfAssessments):

        mark = int(input(f'\nPlease enter your % mark for your assessment {i + 1}:\t'))
        weighting = int(input(f'Please enter the % weighting for your assessment {i + 1}:\t'))
        assessment = Assessment(mark, weighting)

        if mark == 0:
            pass            # Excludes any assessments where the mark is 0 - assuming they have not been taken
        else:
            totalWeighting += assessment.weighting
            totalMark += assessment.calculateOverall()

    if totalWeighting != 100:
        totalMarkOf100 = (totalMark / totalWeighting) * 100
        totalWeightingOf100 = totalWeighting / totalWeighting * 100
        print(f'overall, you have {totalMark}% out of {totalWeighting}%')
        print(f'Scaled to 100% you have / are on track for {totalMarkOf100}% out of {totalWeightingOf100}%')
    else:
        print(f'You have {totalMark}% so far out of {totalWeighting}%\n\n')


main()
