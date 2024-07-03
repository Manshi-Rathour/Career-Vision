def calGraduationYear(createdYear, academicYear, currentAY):
    graduationY = (createdYear - currentAY) + academicYear
    return graduationY


if __name__ == "__main__":

    graduation_year = calGraduationYear(2024, 4, 2)
    print("Graduation Year:", graduation_year)
