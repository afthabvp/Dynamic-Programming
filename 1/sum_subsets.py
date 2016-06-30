""" 
Given an array of N elements, consider all subsets ( 2^^N ),
 now sort the subsets based upon the sum of elements in it, and then 
 find the K'th subset from the list of sorted subsets.


 Eg. array = {1,2,3}
Subsets sorted acc. to sum
{ Phi }
{1}
{2}
{1,2}
{3}
{1,3}
{2,3}
{1,2,3}

for K = 4, ans can be either {1,2} or {3}

""" 

def  findSortedUptoK(output_list,current_element):
	temp_list=[[]]
	current_list=[]
	current_list.append(current_element)
	for index,val in enumerate(output_list):
		
		union_set=set(current_list).union(set(val))
		temp_list.append(list(union_set))
		
	del temp_list[0]
	output_list=output_list+temp_list
	#print output_list

	output_list.sort(key=sum)
	#print output_list
	output_list=output_list[:k]
	return output_list




if __name__ == '__main__':
	N=[1,2,3,4] # input list
	k=10		#subset which is find from the sorted subsets
	output_list=[[]]
	N.sort()
	list1=[]
	list1.append(N[0])

	output_list.append(list1)


	for i in range(1,len(N)):
		output_list=findSortedUptoK(output_list,N[i])
			
	print output_list[k-1]
	
	
