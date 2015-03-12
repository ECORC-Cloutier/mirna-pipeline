import cPickle

days = [0,1,3,7,10] #change the days if necessary
dump = dict()

for i in range(0,5): #if days were changed, change the upper bound of the range to the number of days present
    pick = open ('day' + str(days[i]) + '.pickle','w')
    cPickle.dump ( dump, pick)
    pick.close()
