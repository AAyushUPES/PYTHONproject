# -*- coding: utf-8 -*-
"""
Created on Sat May  4 04:50:12 2024

@author: DELL
"""

import matplotlib.pyplot as plt

def conductsurvey(studentnum):
    print("\n┌─────────────────────────────────────────────────────────┐")
    print("\nStudent {}:".format(studentnum))
    print("Welcome to the Survey!")
    print("--------------------------------------")
    print("Please answer the following questions:")

    # Questions asked in survey
    while True:
        name = input("1. What is your name? ")
        if all(char.isalpha() or char.isspace() for char in name):
            break
        else:
            print("Please enter letters and spaces only. Try again.")

    while True:
        sapID = input("2. What is your sap id? ")
        if sapID.isdigit():
            break
        else:
            print("Please enter a valid SAP ID (only digits).")

    enrollID = input("3. What is your enrollment id? ")

    while True:
        emailID = input("4. Enter your college email id: ")
        if "@" in emailID and "." in emailID:
            break
        else:
            print("Please enter a valid email address.")

    while True:
        age = input("5. How old are you? ")
        if age.isdigit() and 16 <= int(age) <= 30:
            break
        else:
            print("Please enter a valid age (only digits and between 16 and 30).")

    while True:
        major = input("6. What is your major? ")
        if all(char.isalpha() or char.isspace() or char in "[](){}<>.,;:!?'\"-" for char in major):
            break
        else:
            print("Please enter letters, spaces, and allowed symbols only. Try again.")

    while True:
        print("Please choose your year from the following options:")
        print("A. Freshman")
        print("B. Sophomore")
        print("C. Junior")
        print("D. Senior")

        year_input = input("7. What year are you in? (A/B/C/D) ")

        if year_input.upper() in ["A", "B", "C", "D"]:
            if year_input.upper() == "A":
                year = "Freshman"
            elif year_input.upper() == "B":
                year = "Sophomore"
            elif year_input.upper() == "C":
                year = "Junior"
            elif year_input.upper() == "D":
                year = "Senior"
            break
        else:
            print("Please choose a valid option (A/B/C/D).")

    while True:
        sem = input("8. Which semester are you in? ")
        if sem.isdigit():
            sem_num = int(sem)
            if 1 <= sem_num <= 10:
                break
            else:
                print("Semester number must be between 1 and 10.")
        else:
            print("Please enter a valid semester number.")

    while True:
        batch = input("9. Enter your batch number: ")
        if batch.isdigit():
            break
        else:
            print("Please enter only digits.")

    clubs = input("10. Are you involved in any clubs or extracurricular activities? ")

    if clubs.lower() == "yes":
        clublist = input("Please list them: \n")
    else:
        clublist = ""

    print("\nFor the next questions, please choose from the following options:")
    print("A. Excellent")
    print("B. Good")
    print("C. Average")
    print("D. Poor")

    favsubject = input("11. What is your favorite subject or course so far? ")

    while True:
        favsubject_rating = input(f"12. How would you rate {favsubject}? (A/B/C/D) ")
        if favsubject_rating.upper() in ["A", "B", "C", "D"]:
            break
        else:
            print("Please choose a valid option (A/B/C/D).")

    leastfavsubject = input("13. What is your least favorite subject or course so far? ")
    while True:
        leastfavsubject_rating = input(f"14. How would you rate {leastfavsubject}? (A/B/C/D) ")
        if leastfavsubject_rating.upper() in ["A", "B", "C", "D"]:
            break
        else:
            print("Please choose a valid option (A/B/C/D).")

    print(f"Your favorite subject is {favsubject} and you rated it as {favsubject_rating}. Your least favorite subject is {leastfavsubject} and you rated it as {leastfavsubject_rating}.")

    while True:
        favmoment = input("15. What is your favorite moment so far in this college and why? (Share your moment in 100 words) ")
        word_count = len(favmoment.split())
        if word_count <= 100:
            break
        else:
            print("Please limit your response to 100 words or less.")

    print("\nThank you, {}! Your responses have been recorded.".format(name))
    print("└─────────────────────────────────────────────────────────┘")

    return year  # Return the year

def main():
    year_counts = {}

    for i in range(1, 11):
        year = conductsurvey(i)  # Call conductsurvey and get the year

        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1

    # Create a bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(year_counts.keys(), year_counts.values())
    plt.xlabel('Year')
    plt.ylabel('Number of Students')
    plt.title('Distribution of Students across Years')
    plt.show()

    # Create a histogram
    plt.figure(figsize=(8, 6))
    plt.hist(list(year_counts.values()), bins=range(min(year_counts.values()), max(year_counts.values()) + 2), edgecolor='black')
    plt.xlabel('Number of Students')
    plt.ylabel('Frequency')
    plt.title('Histogram of Student Distribution across Years')
    plt.show()
    

if __name__ == "__main__":
    main()