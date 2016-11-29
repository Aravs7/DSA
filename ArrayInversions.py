invCount = 0

def msort(alist):

	l = len(alist)
	if l<=1:
		return alist

	mp = l//2
	leftSort = msort(alist[0:mp])
	rightSort = msort(alist[mp:])
	return merge(leftSort,rightSort)


def merge(ls,rs):

	global invCount

	i = j = 0

	merged = []

	while i < len(ls) and j < len(rs):
		if ls[i] <= rs[j]:
			merged.append(ls[i])
			i = i+1
		else:
			invCount =invCount+1
			merged.append(rs[j])
			j = j+1

	return merged+ls[i:]+rs[j:]


if __name__ == '__main__':
	alist =[5,4,3,2,1]
	print(msort(alist),'  ',invCount)

