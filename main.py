def saveQuestion(problem):
    dictProblem = {}
    dictProblem["name"] = input("Enter The Problem Name : ")
    dictProblem["difficulty"] = input("Enter The Difficulty Of The Problem : ")
    problem.append(dictProblem)
    print("Record Saved Successfully!")

    
def showStats(problem):
    easy =0
    medium = 0
    hard = 0

    if len(problem) ==0:
        print("No Problem Solved")
        return

    for p in problem:
        if (p["difficulty"]).lower() == "easy":
            easy +=1
        elif (p["difficulty"]).lower() == "medium":
            medium +=1
        elif (p["difficulty"]).lower() == "hard":
            hard +=1
        
    print(f"Total Solved : {len(problem)}")
    print(f"Easy : {easy}")
    print(f"Medium : {medium}")
    print(f"hard : {hard}")


def saveData(problem):
    with open("problems.txt","w") as file1:
        for p in problem:    
            file1.write(f'{p["name"]},{p["difficulty"]} \n')
        print("successfully saved :) ")


def loadData(problem):
    problem.clear()
    try:
        with open("problems.txt","r") as file1:
            lines = file1.readlines()
            for line in lines:
                part1,part2 = line.strip().split(",")
                print(f'"name" : {part1} ,"difficulty" : {part2}')
                problem.append({"name" :part1 ,"difficulty" : part2} )
    except FileNotFoundError:
        print("File not Found...")
        

def main():
    problem = []
    menu = """
===== LeetCode Tracker =====

1. Add Problem
2. Show Statistics
3. Save Data
4. Load Data
5. Exit
        """

    while(True):
        print(menu)
        try:
            choice = int(input("Enter Your Choice : "))
        except ValueError:
            print("Please Enter A Number...")
            continue


        if(choice == 1):
            saveQuestion(problem)
        elif(choice == 2):
            showStats(problem)
        elif(choice == 3):
            saveData(problem)
        elif(choice == 4):
            loadData(problem)
        elif(choice == 5):
            print("Goodbyee !")
            break
        else:
            print("Invalid Choice! Please Try Again.")



main()