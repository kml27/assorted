
built = {"test": [0, 4], "this": [1,6], "algo":[2,3, 5]}

permutations = []

buildingPermutations = True

#non uniform base position
#nbp = len(built.keys())

print built

#print nbp, "terms"

place = {k:{"total":0, "value":0} for k in built.keys()}

#total number of permutations
for key in built.keys():
	place[key]["total"]=len(built[key])

#print place
	
#must insure that the order of the keys will not change
	
while buildingPermutations:
	#build permutation
	permutation = []
	for key in built.keys():
		#a's place, b's place, c's place (e.g. a has 2 possible values, b has 1 possible value, c has 2 possible values)
		#index into the built locations dictionary lists by the current value of the "place" the term holds
		permutation.append(built[key][place[key]["value"]])
	
	permutations.append(permutation)
	#print permutation
	
	#increment
	carry = True
	for key in built.keys():
		#print "pre-inc", place[key]
		
		incrementedValue = place[key]["value"]+(1 if carry else 0)
		#print incrementedValue
		carry = incrementedValue/place[key]["total"] >= 1
		#print 1 if carry else 0,"from ", key
		place[key]["value"] = incrementedValue%place[key]["total"]
		#print "post-inc",place[key]
	#raw_input()
	
	#if carry a 1 from the highest place, all permutations iterated
	if carry:
		buildingPermutations = False

print permutations

minlen = None
ilow = None
for j,p in enumerate(permutations):
    #print p
    curlen= max(p)-min(p)
    
    if minlen is None or curlen < minlen:
        minlen=curlen
        ilow = j
        
print "cluster:",ilow, "length:",minlen
