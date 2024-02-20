from accessify import private
from collections import defaultdict


class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Respondent(name='{self.name}', age={self.age})"


class AgeGroup:
    @staticmethod
    def create_age_groups():
        bounds = input("Enter age bounds: ")
        age_bounds = [int(bound) for bound in bounds.split()]
        return [[0, age_bounds[0]]] + [[age_bounds[i] + 1, age_bounds[i + 1]] for i in range(len(age_bounds) - 1)] + [
            [age_bounds[-1] + 1, 123]]


class Survey:
    def __init__(self):
        self._respondents = self.add_respondents()
        self._age_bounds = AgeGroup.create_age_groups()
        self.__age_group = []

    @property
    def respondents(self):
        return self._respondents

    @property
    def age_bounds(self):
        return self._age_bounds

    @private
    def add_respondents(self):
        respondents = []
        while True:
            respondent_input = input("Enter name, age (or 'END' to finish): ")
            if respondent_input.upper() == "END":
                break
            respondent_data = respondent_input.split(",")
            name = respondent_data[0].strip()
            age = int(respondent_data[1].strip())
            respondent = Respondent(name, age)
            respondents.append(respondent)
        return respondents

    def display_respondents(self):
        grouped_respondents = defaultdict(list)

        for respondent in self._respondents:
            for age_group in self._age_bounds:
                if age_group[0] <= respondent.age <= age_group[1]:
                    grouped_respondents[tuple(age_group)].append(respondent)

        for age_group, group_respondents in sorted(grouped_respondents.items()):
            print(f"{age_group[0]}-{age_group[1]}: ", end="")
            for respondent in sorted(group_respondents, key=lambda x: x.age):
                print(f"{respondent.name} ({respondent.age}), ", end="")
            print()


survey_instance = Survey()
survey_instance.display_respondents()
