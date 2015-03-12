import cPickle

days = [0,1,3,7,10] #change the days if necessary - only ADD days DO NOT remove days; extra pickle files can be deleted later
dump = dict()

for i in range(0,5): #if days were changed, change the upper bound of the range to the number of days present
    pick = open ('day' + str(days[i]) + '.pickle','w')
    cPickle.dump ( dump, pick)
    pick.close()
