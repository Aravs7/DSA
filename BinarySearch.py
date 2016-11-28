def bnsearch(aitem,alist):

    l = len(alist)
    print(alist)

    mp = l//2

    if mp == 0:
    	return aitem == alist[0]

    mid = alist[mp]

    if aitem == mid:
        return True
    elif aitem > mid:
        return bnsearch(aitem, alist[mp+1:])
    else:
        return bnsearch(aitem, alist[0:mp])

if __name__ == '__main__':
    alist = [2,3,4,5,6,7,7,8,8,9,10,16]
    aitem = 1
    print(bnsearch(aitem, alist))