import json
import operator as op

with open("question_bank.json") as f:
    data = json.load(f)

gryffindor, hufflepuff, slytherin, ravenclaw = 0, 0, 0, 0

def option_letter(x, l):
    global gryffindor, hufflepuff, slytherin, ravenclaw
    o = l[["a", "b", "c", "d"].index(x)]
    if  o== "h":
        hufflepuff += 1
    elif o == "g":
        gryffindor +=1
    elif o == "s":
        slytherin+=1
    else:
        ravenclaw +=1
    pass


def askQuestion(q, options, order):
    global gryffindor, hufflepuff, slytherin, ravenclaw
    running = True
    while running:
        print(q)
        for i in range(len(options)):
            print("%s: %s" %("abcd"[i], options[i]))
        question = input("Enter your answer: ")
        print("")
        if question not in "abcd":
            print("Please type the option that you choose in lower case and nothing else, this ensures that we know what choice you have chosen")
        else:
            option_letter(question, order)
            running = False
        
    return gryffindor, hufflepuff, ravenclaw, slytherin

def create_questions(dic):
    for i in dic:
        askQuestion(i, dic[i][0], dic[i][1])

def choose_house():
    global gryffindor, slytherin, hufflepuff, ravenclaw
    print("You are %i%s %s"%(round(gryffindor/11*100, 2), "%", "Gryffindor"))
    print("You are %i%s %s"%(round(slytherin/11*100, 2), "%", "Slytherin"))
    print("You are %i%s %s"%(round(hufflepuff/11*100, 2), "%", "Hufflepuff"))
    print("You are %i%s %s"%(round(ravenclaw/11*100, 2), "%", "Ravenclaw"))
    x = [gryffindor, slytherin, hufflepuff, ravenclaw]
    a=max(x)
    if op.countOf(x, a) > 1:
        print("There has been a tie between the houses that you are eligible for. Hence, we are choosing the house based on house hierarchy, this is to encourage sparsely populated houses to get more members")
    else:
        pass
    if a == slytherin:
        print("You are chosen into Slytherin")
    elif a == gryffindor:
        print("You are chosen into Gryffindor")
    elif a == hufflepuff:
        print("You are chosen into Hufflepuff")
    else:
        print("You are chosen into Ravenclaw")
            
def main():
    global data
    create_questions(data)
    choose_house()
    pass

main()
print(ravenclaw, slytherin, hufflepuff, gryffindor)