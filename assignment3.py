import sys
        
def calculateRisk(core,incidence):
    numerator=int(incidence.split("/")[0])
    denumerator=int(incidence.split("/")[1])
    a1=numerator*float(core)
    b1= (denumerator-numerator) - (denumerator-numerator) * float(core)
    risk= b1/(a1+b1)
    return risk


def process(command_list,outputFile):
    interrogees = []
    for i in range(len(command_list)):
        str = command_list[i].split(" ")[0]
        line = command_list[i]
        if str == "create":
            create(interrogees,line,outputFile)
        elif command_list[i].split()[0] == "list":
            displayList(interrogees)
        elif str == "risk":
            displayRisk(interrogees,line)
        elif str == "recommendation":
            recommendation(interrogees,line)
        elif str == "remove":
            remove(interrogees,line)

def displayRisk(interrogees,line):
    name = line.split()[1]
    for i in interrogees:
        if i["Interrogee Name"] == name:
            print("Interrogee Deniz has a counsel risk of " + "%.2f" % i["Counsel Risk"] + "%.")
            break

    print("Risk for " + name + " cannot be calculated due to absence.")


def displayList(interrogees):
    print (93 * "-")
    for i in interrogees:
        print(i)
    print (93 * "-")

def create(interrogees,line,outputFile):
    info = line.split()
    name = info[1].split(",")[0]
    core = info[2].split(",")[0]
    counsel = info[3].split(",")[0]
    counselrisk = calculateRisk(core,info[4])
    if counsel == info[3].split(",")[0] == "0":
        dict={"Interrogee Name":name,"Core Accuracy":core,"Counsel":"Not Bomber","Local Bomber Incidence":info[4],"Counsel Risk":round(counselrisk,2)*100}
    else:
        dict={"Interrogee Name":name,"Core Accuracy":core,"Counsel":"Bomber","Local Bomber Incidence":info[4],"Counsel Risk":round(counselrisk,2)*100}
    interrogees.append(dict)
    print("Interrogee " + name + " is recorded.")
    outputFile.write("Interrogee " + name + " is recorded.\n")

def remove(interrogees,line):
    name = line.split()[1]
    for i in interrogees:
        if i["Interrogee Name"] == name:
            interrogees.remove(i)
            break
    print("Interrogee " + line.split()[1] + " is removed")   

def recommendation(interrogees,line):
    name = line.split()[1]
    for i in interrogees:
        if i["Interrogee Name"] == name:
            if i["Counsel"] == "Not Bomber" or i["Counsel Risk"]<=0.4:
                print("System suggests to release " + name + ".")
                break
            else:
                print("System suggests to arrest " + name + ".")
                break

    print("Recommendation for " + name + " cannot be calculated due to absence.")

def main():
    command_list=[]
    input = sys.argv[1]
    output = sys.argv[2]
    with open(input, "r") as inputFile:
        for line in inputFile:
            command_list.append(line)
    
    with open(output,"w") as outputFile:
        process(command_list,outputFile)
        outputFile.flush()
        outputFile.close()

if __name__ == "__main__":
    main()