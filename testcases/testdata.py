import csv
import random

# Generates a .csv with data to be used for website test cases

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN',
'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA',
'WA','WV','WI','WY']

procedures = ['Knee Replacement', 'Percutaneous Coronary Angioplasty (PTCA)', 'Laminectomy',
'Hip Replacement','Spinal Fusion','Cholecystectomy','Bone Excision','Hysterectomy',
'Colon Resection','Scar excision','Appendectomy','Hip/Femur Fracture','Coronary Artery Bypass Graft (CABG)',
'Lower extremity fracture', 'MRI', 'CT Scan']

cost = [15432.16181, 25550.07923, 28288.42665, 23885.19049, 19719.8712, 10989.9055, 18560.65432,
12574.90429, 18930.50093, 32236.16339, 9537.894685, 6309.512718, 32116.92964, 9998.73303, 1325, 3275]

times = int(input("How many times do you want this to be run: "))

with open('testcase.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Simple Name', 'Price', 'Data of Procedure', 'Age', 'Gender', 'Data Added', 'Unique ID'])
    
    gender = ['M', 'Y', 'X']
    for i in range(0, times):
        sprocedure = procedures[random.randint(0,len(procedures))]
        location = procedures.index(sprocedure)
        scost = cost[location]
        sage = random.randint(12,100)
    
        dateproyear = str(random.randint(2010,2022))
        datepromonth = str(random.randint(1,12))
        dateproday = str(random.randint(1,31))

        dateprohour = str(random.randint(0,24))
        datepromin = str(random.randint(0,59))
        dateprosec = str(random.randint(0,59))

        dateaddyear = str(random.randint(2010,2022))
        dateaddmonth = str(random.randint(1,12))
        dateaddday = str(random.randint(1,31))

        dateaddhour = str(random.randint(0,24))
        dateaddmin = str(random.randint(0,59))
        dateaddsec = str(random.randint(0,59))

        datepromatrix = [datepromonth, dateproday, dateprohour, datepromin, dateprosec]
        dateaddmatrix = [dateaddmonth, dateaddday, dateaddhour, dateaddmin, dateaddsec]

        for n in range(0, len(datepromatrix)):
            if (int(datepromatrix[n]) < 10):
                datepromatrix[n] = '0{}'.format(datepromatrix[n])

        for n in range(0, len(dateaddmatrix)):
            if (int(dateaddmatrix[n]) < 10):
                dateaddmatrix[n] = '0{}'.format(dateaddmatrix[n])

        dateadd = '{}-{}-{} {}:{}:{}.000'.format(dateaddyear, dateaddmatrix[0], dateaddmatrix[1], dateaddmatrix[2], dateaddmatrix[3], dateaddmatrix[4])
        datepro = '{}-{}-{} {}:{}:{}.000'.format(dateproyear, datepromatrix[0], datepromatrix[1], datepromatrix[2], datepromatrix[3], datepromatrix[4])

        partGender = gender[random.randint(0,2)]
        uniqueID = i

        output = [sprocedure, scost, datepro, sage, partGender, dateadd, uniqueID]
        writer.writerow(output)


        


        



        








