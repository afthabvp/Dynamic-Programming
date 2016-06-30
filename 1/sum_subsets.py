
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
	
	
