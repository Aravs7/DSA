def partition(alist):
	l = len(alist)
	if l<=1:
		return alist
	pivot = alist[l-1]

	r = q = 0

	while r < l-1:
		if alist[r] < pivot:
			alist[q],alist[r] = alist[r],alist[q]
			q = q+1

		r = r+1

	alist[q],alist[l-1] = alist[l-1],alist[q]

	alist_left = partition(alist[0:q])
	alist_right = partition(alist[q+1:])

	return alist_left+[alist[q]]+alist_right



if __name__ == '__main__':
	ll = [5,2,1,4,6,3,9]
	print(partition(ll))



