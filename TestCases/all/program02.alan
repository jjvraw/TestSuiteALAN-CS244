source binary_search
function binary_search(array elements ,int key ,int high , int low ) to
begin
	relax
	if low <= high then
		leave
	end
	integer mid = low +(high -low)/2
	if elements[mid]==key then
		leave mid
	elsif elements[mid] < key then
		call binary_search(elements,key,high,mid+1)
		leave
	else 
		call binary_search(elements,key,mid-1,0)
		leave
	end
end
	
