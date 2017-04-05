import requests
import json

#url="http://www.omdbapi.com/?t=Prison+Break&y=2017&plot=full"
#request User To Enter Movie To Search And The Year Of The Movie
url="http://www.omdbapi.com"
movieName=raw_input("Enter Name Of The Movie To Search \n")
year_of_act=raw_input("Enter The Year In which The Movie Was Acted \n")

if movieName and year_of_act:#Ensure User Enters Movie Name and Year
    if year_of_act.isdigit():
        
        if (int(year_of_act)<=2017 and int(year_of_act)>=1950):
            
            payload={'t':movieName,'y':year_of_act,'plot':'full'}
            request=requests.get(url,params=payload)

            res=request.json()
            #print request.status_code
            
            print res['Title']+"\n..............................................."

            print "Description.\n"+res['Plot']+"\nYear Of Release: "+res['Year']+"\n"+"Actors\n"+res['Actors']+"\nWritten By \n"+res['Writer']

        else:
            print "We Only Have Movies From 1950-2017"
    else:
        print "That Year Does Not Exist"

else:
    print "Supply The Name Of The Movie And The Year You Want to Search it From"
