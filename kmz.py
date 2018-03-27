# kmz.py
import os
import re

# file directories
kmlfolder = "E:\\Furman\\summer_research\\TERRESTRIAL_MAMMALS\\kmz\\"

def records():
    infile = open(kmlfolder + "kml.kml", 'r') 
    recordNum = 0
    lines = infile.readlines()
    outfile = open(kmlfolder + "recordstemp.txt", 'w')
    for i in range(len(lines)):
        if "<td>binomial</td>" in lines[i]:
            recordNum += 1
            outfile.write(lines[i+2])    # binomial
    infile.close()
    outfile.close()
    infile1 = open(kmlfolder + "recordstemp.txt", 'r')
    outfile1 = open(kmlfolder + "records.txt", 'w')
    lines = infile1.readlines()
    for i in range(len(lines)):
        a = lines[i]
        outfile1.write(str(a)[4:len(a)-6] + "\n")
    infile1.close()
    outfile1.close()
    print ("number of record: ", recordNum)    # number or records by binomial
    


def binomial():
    infile = open(kmlfolder + "records.txt", 'r')
    outfile = open(kmlfolder + "binomialtemp.txt", 'w')
    lines = infile.readlines()
    binomialNum = 1
    outfile.write(lines[0])
    for i in range(0, len(lines), 1):
        for n in range(0, i, 1):
            if ((lines[1] == lines[i]) or
                (str(lines[i]) == str(lines[n]))):
                break
            elif ((n == i-1) and (lines[i] != lines[i-1])):
                outfile.write(lines[i])
                binomialNum += 1
    infile.close()
    outfile.close()
    infile1 = open(kmlfolder + "binomialtemp.txt", 'r')
    outfile1 = open (kmlfolder + "binomial.txt", 'w')
    lines = infile1.readlines()
    for i in range(len(lines)):
        a = lines[i]
        outfile1.write(str(a)[4:len(a)-6] + "\n")
    infile1.close()
    outfile1.close()
    print("number of binomial: ", binomialNum)


    
def split3():
    infile = open(kmlfolder + "three.txt", 'r')
    namefile = open(kmlfolder + "records.txt", 'r')
    lineIn = infile.readlines()
    lineName = namefile.readlines()
    state = "Waiting1stSpecies"
    i = 0         # infile line index
    n = -1        # namefile line index
    while i < 784 and n <= 2:  
        head = '<Placemark id='
        commonpath = kmlfolder + "temp\\"
        if state == "Waiting1stSpecies":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-2] + ".kml"
                outfile = open(filename, 'a')
                endindex = 0
                for j in range (i+1, 784):
                    if head in lineIn[j]:
                        try:
                            endindex = lineIn.index(lineIn[j], i+1)
                        except ValueError:
                            print("Error")
                            return
                for m in range(i, endindex -2, 1):
                    outfile.write(lineIn[m])
                    i += 1
                    print ("i= ", i)
                state = "NextOrEnd"
            else:
                outfile = open(commonpath + "begin.kml", 'a')
                outfile.write(lineIn[i])
                i += 1
                print ("i= ", i)
        elif state == "NextOrEnd":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-2] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                print ("i= ", i)
                endindex = 0
            elif "Folder" in lineIn[i]:
                outfile.close()
                outfile = open(commonpath + "end.kml", 'a')
                state = "ReadEnd"
            else:
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-2] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                print ("i= ", i)
        elif state == "ReadEnd":
            outfile.write(lineIn[i])
            i += 1
            print ("i= ", i)
    infile.close()
    namefile.close()
    outfile.close()
    print("done")



def split():
    infile = open(kmlfolder + "kml.kml", 'r')
    namefile = open(kmlfolder + "records.txt", 'r')
    lineIn = infile.readlines()
    lineName = namefile.readlines()
    state = "Begin"
    i = 0         # i = infile line index
    n = -1        # n = namefile line index
    while i < 3456422 and n < 12217:  
        head = '<Placemark id='
        commonpath = kmlfolder + "species original\\"
        if state == "Begin":
            x = 0
            while x <= 8:
                outfile = open(commonpath + "begin.kml", 'a')
                outfile.write(lineIn[x])
                x += 1
            i += 8
            state = "Waiting1stSpecies"
        if state == "Waiting1stSpecies":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                print ("n= ", n)
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                state = "NextOrEnd"
            else:
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
        elif state == "NextOrEnd":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                print("n= ", n)
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                endindex = 0
            elif "Folder" in lineIn[i]:
                outfile.close()
                outfile = open(commonpath + "end.kml", 'a')
                state = "ReadEnd"
            else:
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
        elif state == "ReadEnd":
            outfile.write(lineIn[i])
            i += 1
    infile.close()
    namefile.close()
    outfile.close()
    print("done")


    
def combine3():
    infileb = open(kmlfolder + "d\\begin.kml", 'r')
    infileca = open(kmlfolder + "d\\Cephalophus adersi.kml", 'r')
    infilee = open(kmlfolder + "d\\end.kml", 'r')
    outfile = open(kmlfolder + "d\\combineExample.kml", 'a')
    for line in infileb:
        outfile.write(line)
    for line in infileca:
        outfile.write(line)
    for line in infilee:
        outfile.write(line)
    infileb.close()
    infileca.close()
    infilee.close()
    outfile.close()
    print("done")



def combine():
    commonpath = kmlfolder + "species original\\"
    name = input("Enter the binomial of the species(Please capitalize the first letter): ")
    namelist = os.listdir(commonpath)
    found = False
    for n in range (0, 5304):            # n = index of list of filenames
        if name in namelist[n]:
            print("Do you mean...")
            l = []                      # l = list of species name for print
            found = True
            break
    for n in range (0, 5304):
        if name in namelist[n]:
            l.append(namelist[n])
            print (str(l.index(namelist[n])+1) + "  " + namelist[n])
    if found == False:
        print("Can't find this species.")
        return
    else:
        num = input("Enter the number corresponding to the species binomial: ")
        q = False
        while (q == False):
            try:
                finalname = str(l[int(num)-1])
                q = True
            except:
                print("This number is invalid.")
                num = input("Enter the number corresponding to the species binomial: ")
        confirm = input("Do you want " + str(num) + " " + str(l[int(num)-1]) + "? Please enter y or n: ")
        p = False
        while (p == False):
            if (confirm == "n"):
                p = True
                num = input("Enter the number corresponding to the species binomial: ")
                while (p == False):
                    try:
                        finalname = l[num-1]
                        p = True
                    except:
                        print("This number is invalid.")
            elif (confirm == "y"):
                p = True
            else:
                confirm= input("Do you want " + num + " " + l[num-1] + "? Please enter y or n: ")
        
    infileB = open(commonpath + "begin.kml", 'r')
    infileE = open(commonpath + "end.kml", 'r')
    infile = open(commonpath + finalname, 'r')
    outfile = open(kmlfolder + "open me.kml", 'a')
    for line in infileB:
        outfile.write(line)
    for line in infile:
        outfile.write(line)
    for line in infileE:
        outfile.write(line)
    infileB.close()
    infile.close()
    infileE.close()
    outfile.close()
    print("done")






def genus():
    infile = open(kmlfolder + "kml.kml", 'r')
    recordNum = 0
    lines = infile.readlines()
    outfile = open(kmlfolder + "genusrecordstemp.txt", 'w')
    for i in range(len(lines)):
        if "<td>genus_name</td>" in lines[i]:
            recordNum += 1
            outfile.write(lines[i+2])    
    infile.close()
    outfile.close()
    infile1 = open(kmlfolder + "genusrecordstemp.txt", 'r')
    outfile1 = open(kmlfolder + "genusrecords.txt", 'w')
    lines = infile1.readlines()
    for i in range(len(lines)):
        a = lines[i]
        outfile1.write(str(a)[4:len(a)-6] + "\n")
    infile1.close()
    outfile1.close()
    print ("number of record: ", recordNum)    # number of records by genus

    infile = open(kmlfolder + "genusrecords.txt", 'r')
    outfile = open(kmlfolder + "genus.txt", 'w')
    lines = infile.readlines()
    genusNum = 1
    outfile.write(lines[0])                     # get rid of repeated items
    for i in range(0, len(lines), 1):             # decide the fate of line[i]
        for n in range(0, i, 1):
            if ((lines[1] == lines[i]) or
                (str(lines[i]) == str(lines[n]))):  # if line[i] matches line[n], stop current loop body
                break
            elif ((n == i-1) and (lines[i] != lines[i-1])):   # if line[i] doesn't match line[n] even to the end,
                outfile.write(lines[i])                       # write line[i]
                genusNum += 1
    infile.close()
    outfile.close()
    print("number of genus: ", genusNum)
    print("done")



def revisedSplit3():
    infile = open(kmlfolder + "three.txt", 'r')
    namefile = open(kmlfolder + "records.txt", 'r')
    lineIn = infile.readlines()
    lineName = namefile.readlines()
    state = "Begin"
    i = 0         # infile line index
    n = -1        # namefile line index
    while i < 784 and n <= 2:  
        head = '<Placemark id='
        commonpath = kmlfolder + "d\\"
        if state == "Begin":
            x = 0
            while x <= 8:
                outfile = open(commonpath + "begin.kml", 'a')
                outfile.write(lineIn[x])
                x += 1
            i += 9
            state = "Waiting1stSpecies"
        if state == "Waiting1stSpecies":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                print ("n= ", n)
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                state = "NextOrEnd"
            else:
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                # NEW CODE BEGINS
                if ("<outerBoundaryIs><LinearRing><coordinates>" in lineIn[i]):
                    outfile.write("          <outerBoundaryIs><LinearRing><coordinates>")
                    tok = re.compile(",")
                    tok = re.compile(",0 ")
                    tokenlist = tok.split(lineIn[i][52:-46])
                    for token in tokenlist:
                        tok1 = re.compile(",")
                        tokenlist1 = tok1.split(token)
                        if (tokenlist1 != ['']):
                            tokenlist1[0] = "%8.5f"%(float(tokenlist1[0]))
                            tokenlist1[1] = "%8.5f"%(float(tokenlist1[1]))
                            outfile.write(tokenlist1[0] + "," + tokenlist1[1] + ",0 ")
                    i += 1
                    outfile.write("</coordinates></LinearRing></outerBoundaryIs> \n")
                else:
                    outfile.write(lineIn[i])
                    i += 1
                # REVISED PORTION ENDS
        elif state == "NextOrEnd":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                print("n= ", n)
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                endindex = 0
            elif "Folder" in lineIn[i]:
                outfile.close()
                outfile = open(commonpath + "end.kml", 'a')
                state = "ReadEnd"
            else:
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                # NEW CODE BEGINS
                if ("<outerBoundaryIs><LinearRing><coordinates>" in lineIn[i]):
                    outfile.write("          <outerBoundaryIs><LinearRing><coordinates>")
                    tok = re.compile(",")
                    tok = re.compile(",0 ")
                    tokenlist = tok.split(lineIn[i][52:-46])
                    for token in tokenlist:
                        tok1 = re.compile(",")
                        tokenlist1 = tok1.split(token)
                        if (tokenlist1 != ['']):
                            tokenlist1[0] = "%8.5f"%(float(tokenlist1[0]))
                            tokenlist1[1] = "%8.5f"%(float(tokenlist1[1]))
                            outfile.write(tokenlist1[0] + "," + tokenlist1[1] + ",0 ")
                    i += 1
                    outfile.write("</coordinates></LinearRing></outerBoundaryIs> \n")
                else:
                    outfile.write(lineIn[i])
                    i += 1
                # REVISED PORTION ENDS
        elif state == "ReadEnd":
            outfile.write(lineIn[i])
            i += 1
    infile.close()
    namefile.close()
    outfile.close()
    print("done")


    
def revisedSplit():
    infile = open(kmlfolder + "kml.kml", 'r')
    namefile = open(kmlfolder + "records.txt", 'r')
    lineIn = infile.readlines()
    lineName = namefile.readlines()
    state = "Begin"
    i = 0         # i = infile line index
    n = -1        # n = namefile line index
    while i < 3456422 and n < 12217:  
        head = '<Placemark id='
        commonpath = kmlfolder + "species compressed\\"
        if state == "Begin":
            x = 0
            while x <= 8:
                outfile = open(commonpath + "begin.kml", 'a')
                outfile.write(lineIn[x])
                x += 1
            i += 9
            state = "Waiting1stSpecies"
        if state == "Waiting1stSpecies":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                print ("n= ", n)
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                state = "NextOrEnd"
            else:
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                # NEW CODE BEGINS
                if ("<outerBoundaryIs><LinearRing><coordinates>" in lineIn[i]):
                    outfile.write("          <outerBoundaryIs><LinearRing><coordinates>")
                    tok = re.compile(",")
                    tok = re.compile(",0 ")
                    tokenlist = tok.split(lineIn[i][52:-46])
                    for token in tokenlist:
                        tok1 = re.compile(",")
                        tokenlist1 = tok1.split(token)
                        if (tokenlist1 != ['']):
                            tokenlist1[0] = "%8.5f"%(float(tokenlist1[0]))
                            tokenlist1[1] = "%8.5f"%(float(tokenlist1[1]))
                            outfile.write(tokenlist1[0] + "," + tokenlist1[1] + ",0 ")
                    i += 1
                    outfile.write("</coordinates></LinearRing></outerBoundaryIs> \n")
                else:
                    outfile.write(lineIn[i])
                    i += 1
                # REVISED PORTION ENDS
        elif state == "NextOrEnd":
            if head in lineIn[i]:
                outfile.close()
                n += 1
                print("n= ", n)
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                outfile.write(lineIn[i])
                i += 1
                endindex = 0
            elif "Folder" in lineIn[i]:
                outfile.close()
                outfile = open(commonpath + "end.kml", 'a')
                state = "ReadEnd"
            else:
                a = lineName[n]
                filename = commonpath + str(a)[:len(a)-1] + ".kml"
                outfile = open(filename, 'a')
                # NEW CODE BEGINS
                if ("<outerBoundaryIs><LinearRing><coordinates>" in lineIn[i]):
                    outfile.write("          <outerBoundaryIs><LinearRing><coordinates>")
                    tok = re.compile(",")
                    tok = re.compile(",0 ")
                    tokenlist = tok.split(lineIn[i][52:-46])
                    for token in tokenlist:
                        tok1 = re.compile(",")
                        tokenlist1 = tok1.split(token)
                        if ((tokenlist1 != ['']) & (tokenlist1[0] != '') & (tokenlist1[1] != '')):
                            tokenlist1[0] = "%8.5f"%(float(tokenlist1[0]))
                            tokenlist1[1] = "%8.5f"%(float(tokenlist1[1]))
                            outfile.write(tokenlist1[0] + "," + tokenlist1[1] + ",0 ")
                    i += 1
                    outfile.write("</coordinates></LinearRing></outerBoundaryIs> \n")
                else:
                    outfile.write(lineIn[i])
                    i += 1
                # REVISED PORTION ENDS
        elif state == "ReadEnd":
            outfile.write(lineIn[i])
            i += 1
    infile.close()
    namefile.close()
    outfile.close()
    print("done")



def tokenizeExample():
#example
    file = open("C:\\Users\\aliu\\Desktop\\1.txt", 'r')
    for line in file:
        tok = re.compile(",")
        tok = re.compile(",0")
        tokenlist = tok.split(line)
        for token in tokenlist:
            tok1 = re.compile(",")
            tokenlist1 = tok1.split(token)
            if (tokenlist1 != ['']):
                tokenlist1[0] = "%8.5f"%(float(tokenlist1[0]))
                tokenlist1[1] = "%8.5f"%(float(tokenlist1[1]))
                print(tokenlist1[0] + "," + tokenlist1[1] + ",0 ", end = "")
                


def sortfile():
    name = input("file address: ")
    file = open(name, 'r')
    l = file.readlines()
    out = open(kmlfolder + "sorted.txt", 'w')
    l.sort()
    for i in range(0, len(l)):
        out.write(l[i])
    file.close()
    out.close()
    print("done")




def somehelp():
    infile = open(kmlfolder + "genus sorted.txt", 'r')
    file = infile.readlines()
    print("Here are the genus names we have.")
    n = 0
    for line in infile:
        n += 1
#        print(str(n) + "  " + line)
    print("Choose something to start with :) ")
    validNum = False
    while (validNum == False):
        try:
            chooseGenus = int(input("Please enter a number corresponding to the genus you want to explore: "))
            validNum = True
            if (chooseGenus > 0 and chooseGenus <= 1175):
                line = str(file[chooseGenus-1])
                print("The genus you chose is: "+ line)
        except:
            print("Please enter a valid number. Try again.")

                



def multicombine():
    commonpath = "E:\\Furman\\summer_research\\TERRESTRIAL_MAMMALS\\kmz\\species compressed\\"
    namelist = os.listdir(commonpath)
    outfile = open(kmlfolder + "open me.kml", 'a')
    speciesNum = int(input("Enter the number of species you want to compare: "))
    for index in range (0, speciesNum):
        if (index == 0):
            color = "aaff0080" # purple
            print("Species " + str(index+1) + " is assigned color PURPLE.")
        elif (index == 1):
            color = "aa0000ff" # red
            print("Species " + str(index+1) + " is assigned color RED.")
        elif (index == 2):
            color = "aa00ffff" # yellow
            print("Species " + str(index+1) + " is assigned color YELLOW.")
        elif (index == 3):
            color = "aadfdf00" # blue
            print("Species " + str(index+1) + " is assigned color BLUE.")
        elif (index == 4):
            color = "aa80ff80" # green
            print("Species " + str(index+1) + " is assigned color GREEN.")
        elif (index == 5):
            color = "aac080ff" # pink
            print("Species " + str(index+1) + " is assigned color PINK.")
        elif (index == 6):
            color = "aa0080ff" # orange
            print("Species " + str(index+1) + " is assigned color ORANGE.")
        elif (index == 7):
            color = "aad71e20" # navy blue
            print("Species " + str(index+1) + " is assigned color NAVY BLUE.")
        else:
            print("You are comparing too many species at the same time!")
            return

        print("Enter the binomial of species number " + str(index+1))
        name = input("Please capitalize the first letter: ")
        found = False
        for n in range (0, 5304):            # n = index of list of filenames
            if name in namelist[n]:
                print("Do you mean...")
                l = []                      # l = list of species name for print
                found = True
                break
        for n in range (0, 5304):
            if name in namelist[n]:
                l.append(namelist[n])
                print (str(l.index(namelist[n])+1) + "  " + namelist[n])
        if found == False:
            print("Can't find this species.")
            return
        else:
            # q = False
            # while (q == False):
                try:
                    num = input("Enter the number corresponding to the species binomial: ")
                    finalname = str(l[int(num)-1])
                    # q = True
                except:
                    print("This number is invalid.")
            # confirm = input("Do you want " + str(num) + " " + str(l[int(num)-1]) + "? Please enter y or n: ")
            # p = False
            # while (p == False):
                # if (confirm == "n"):
                    # p = True
                    # num = input("Enter the number corresponding to the species binomial: ")
                    # r = False
                    # while (r == False):
                        # try:
                            # finalname = l[num-1]
                            # r = True
                        # except:
                            # print("This number is invalid.")
                # elif (confirm == "y"):
                    # p = True
                # else:
                    # confirm= input("Do you want " + num + " " + l[num-1] + "? Please enter y or n: ")
        if (index == 0):
            infileB = open(commonpath + "begin.kml", 'r')
            for line in infileB:
                outfile.write(line)
            infileB.close()
        infile = open(commonpath + finalname, 'r')
        infileline = infile.readlines()
        for i in range (len(infileline)):
            if ("<Placemark" in infileline[i]):
                outfile.write(infileline[i])
                outfile.write("<Style><PolyStyle><color>" + color + "</color></PolyStyle></Style>") 
            else:
                    outfile.write(infileline[i])
        infile.close()

    infileE = open(commonpath + "end.kml", 'r')
    for line in infileE:
        outfile.write(line)
    infileE.close()
    outfile.close()
    print("done")


    

################## main #########################


givehelp = input("Do you need some help about which species to start with? Enter y or n: ")
if (givehelp == "y"):
    somehelp()


#records()
#binomial()
#split3()
#split()
#combine3()
#combine()
multicombine()
#genus()
#revisedSplit3()
#revisedSplit()
#tokenizeExample()
#sortfile()

