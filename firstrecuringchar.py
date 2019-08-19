def rptchtr(string):
       
       
	strlen=len(string)
       flag=0
       for i in range(0,strlen):
          if flag==1:
	     break
          else:		
	     for j in range (i+1,strlen):
		 if string[i]==string[j]:
		       print("First recuring character is", string[i])
                       flag=1
                       break
		 else:
		       j+=1	
inputstr=raw_input("Enter the string")
rptchtr(inputstr)
