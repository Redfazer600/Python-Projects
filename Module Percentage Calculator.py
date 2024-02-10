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
            pass
        else:
            totalWeighting += assessment.weighting
            totalMark += assessment.calculateOverall()

        # print(f'You have {totalMark}% so far out of {totalWeighting}%\n\n')

    if totalWeighting != 100:
        totalMarkOf100 = (totalMark / totalWeighting) * 100
        totalWeightingOf100 = totalWeighting / totalWeighting * 100
        print(f'overall, you have {totalMark}% out of {totalWeighting}%')
        print(f'Scaled to 100% you have / are on track for {totalMarkOf100}% out of {totalWeightingOf100}%')
    else:
        print(f'You have {totalMark}% so far out of {totalWeighting}%\n\n')


main()
