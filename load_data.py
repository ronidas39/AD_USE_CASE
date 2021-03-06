import io
import csv,sys
from create_ad_user import add_user
actual_header="First Name|Last Name|DOB|Gender|Email|Telephone|Membership"

#read file
with io.open("test.csv","r",encoding="utf")as f1:
    data=f1.read()
    f1.close()

#validate header count and header fields
#converting into a list which contains every line as single element
data=data.split("\n")
total_line=len(data)-1
print(f"file has {total_line} lines")

#read the output.csv 
with open("output.csv")as f3:
    data_from_output=csv.reader(f3,delimiter=",")
    for row in data_from_output:
        percentage=total_line
        #calculation based on the given percentage 
        if(percentage>(int(row[0])+int(row[0])*.5)):
            #print and exit
            print("huge number of changes coming")
            #exit from code
            sys.exit()

#get header from file
header=data[0]
print(header)
if(header==actual_header):
    print("file header is ok")
    #assign line number
    line_number=2
    #iterating through the loop
    #eliminating the header
    for row in data[1:]:
        #converting into a list which contains every line as single element separated by pipe character
        delimiter_count=row.split("|")
        #geeting the count of elemenmts inside the list
        delimiter_from_file=len(delimiter_count)
        #comparing with actual element count
        if(delimiter_from_file==7):
            #print with line number
            print(f"{line_number}, delimiters are ok")
            #getting attribute mail & last name
            mail=delimiter_count[4]
            sn=delimiter_count[1]
            #checking if the mail attribute has value or not
            if(mail and sn):
                #if has value
                print("value is presnt")
                add_user(row)

            else:
                #if has no value
                print("no value")
        

        else:
            #print with line number
            print(f"{line_number}, delimiters are not ok")

        line_number=line_number+1


else:
    print("header is not correct please validate")

#write the last execute row count into output csv    
with io.open("output.csv","w",encoding="utf-8")as f2:
    f2.write(str(total_line)+"\n")
    f2.close()



