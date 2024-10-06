#Ranking Selection

#Input List of Individuals and each individual is(Key, Value) [1 80 500] sum 581
#Output List of Individual (updating new fitness) -> just call routtlewhite

# [0:1,2:5,3:5,4:6,7:8] #individuals
def RankingSelection(individuals):#size 5

    #sorting by fitness [(Key-A, value-5), (),()
    sorted_individuals = sorted(individuals.items(), key=lambda ind: ind[1])
    #summation sum (range of length+1) ====>15 sum([1+1 for i in range(sortind)])
    summition = sum(range(1, len(sorted_individuals) + 1))
    #for (indvid for invid)
         #indi.fit=(rank/summation)*100
    updated_individuals = {key: (i + 1) / summition  for i, (key, value) in enumerate(sorted_individuals)}
    
    return updated_individuals

# Example usage:
individuals = {0: 5, 1: 2, 2: 0.5, 3: 1.5, 4: 1}
updated_individuals = RankingSelection(individuals)
print(sorted(updated_individuals.items(), key=lambda ind: ind[0]))
         
#def Any(x,y):
# return x+y

#x=2

#y-9

#z-Any(x,y)
