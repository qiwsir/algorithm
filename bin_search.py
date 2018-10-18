def binarySearch(alist, item):
2	    first = 0
3	    last = len(alist)-1
4	    found = False
5	
6	    while first<=last and not found:
7	        midpoint = (first + last)//2
8	        if alist[midpoint] == item:
9	            found = True
10	        else:
11	            if item < alist[midpoint]:
12	                last = midpoint-1
13	            else:
14	                first = midpoint+1
15	
16	    return found
17	
18	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
19	print(binarySearch(testlist, 3))
20	print(binarySearch(testlist, 13))
