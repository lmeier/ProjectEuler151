import random

visited = dict()

def solveWithDP(batchesRemaining, sheets):
    # Dynamic programming solution
    # Sheets is a list representing counts of paper in envelope [a1, a2, a3, a4, a5]
    if batchesRemaining == 0:
        return 0
    
    sheetsKey = tuple(sheets)
    if sheetsKey in visited:
        return visited[sheetsKey]
    else: 
        totalSheets = sum(sheets)
        if totalSheets == 1:
            numSoloSheets = 1
        else:
            numSoloSheets = 0
        # We're calculating the expected number of times that we
        # encounter a solo sheet. If we're given an envelope with
        # only one sheet, we have encountered a SoloSheet.

        for i in range(0, len(sheets)):
        # Here we iterate over the various ways we can proceed with
        # the sheets we have going into this iteration
            if sheets[i] != 0:
                weight = sheets[i] / totalSheets
                # We're more likely to iterate down paths
                # that have multiple ways of entering them. Weighting via average
                # factors this into our final calculation.
                newSheets = list(sheets)
                newSheets[i] -= 1
                for j in range(i + 1, len(newSheets)):
                    newSheets[j] += 1
                # This calculates the new set of sheets we have given the logic of the problem

                numSoloSheets += solveWithDP(batchesRemaining - 1, newSheets ) * weight
                # Finally we add to our answer future encounters of solo sheets, weighted as described above

        visited[sheetsKey] = numSoloSheets
        # Store subsolutions. Calculating this w/o DP would take significantly longer

        return visited[sheetsKey]



def monteCarolSolution(numIterations=10):
    iterCount, soloEncounters, totalEncounters = 0, 0, 0
    while iterCount < numIterations:

        values = [1, 0, 0, 0, 0]

        while sum(values) > 0:
            sumValues = sum(values)
            totalEncounters += 1
            if sumValues == 1:
                soloEncounters += 1

            paperPulled = random.randint(1, sumValues)
            papersPulledSoFar = 0
            pulled = False

            for num, i in enumerate(values):
                papersPulledSoFar += i
                if paperPulled <= papersPulledSoFar and pulled == False:
                    values[num] -= 1
                    pulled = True 
                    continue
                if pulled:
                    values[num] += 1

        #subtract the first and last encounters of the week, as specified in problem
        totalEncounters -= 2
        soloEncounters -=2
        print(soloEncounters/totalEncounters * 14) #multiply by solo/total gives chance per encounter, there's 14 possible a week
        iterCount += 1


def main():

    print(solveWithDP(16, [1, 0, 0, 0, 0]) - 2) 
    # Foreman starts with 16 batches, 1 A1 sheet.
    # Subtrac 2 at end because problem calls for excluding first and last batch,
    # both of which will have a solo sheet.

    monteCarolSolution()
    # 100k iterations only gets to 3 decimal precision. Problem asks for 6 decimals
    # Clearly, the simulation approach is infeasible


if __name__== "__main__":
  main()
