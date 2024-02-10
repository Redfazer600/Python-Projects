####################
# Creator: Alex Bevan - UP2198095
# Date: 10/2/24
# Name: Module Grades Calculator
# Version: 4
# Changes: tweaked some stuff - adding returns mainly.
####################


class ModuleCalculator:

    def __init__(self):
        self.assessments = int(input('\nPlease enter the number of assessments to calculate your grade from:\t'))
        self.mark = 0
        self.weighting = 0

    def getAssessments(self):
        for i in range(self.assessments):
            mark = int(input(f'\nPlease enter your achieved % mark for your assessment {i + 1}:\t'))
            weighting = int(input(f'Please enter the % weighting for your assessment {i + 1}:\t'))
            assessment = Assessment(mark, weighting)

            if mark == 0:
                pass
            else:
                self.weighting += assessment.weighting
                self.mark += assessment.calculateOverall()

    def calculateGrade(self):
        totalMark = (self.mark / self.weighting) * 100
        totalWeighting = self.weighting / self.weighting * 100

        if self.weighting != 100:
            return f'\noverall, you have {self.mark}% out of {self.weighting}%\n' + \
                f'Scaled to 100% you have / are on track for {totalMark}% out of {totalWeighting}%'
        else:
            return f'\nYou have {totalMark}% so far out of {totalWeighting}%\n\n'


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


def calculateModule():
    moduleGrade = ModuleCalculator()
    moduleGrade.getAssessments()
    output = moduleGrade.calculateGrade()
    return output
