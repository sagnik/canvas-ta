import requests
import pickle
import sys
from pprint import pprint

COURSEID='1804827'
ASSIGNMENTID='8743811'
TOKEN_LOC='/home/szr163/canvas_access_token'

def getStudents(courseID,assignmentID):
    token=open(TOKEN_LOC).read().split("\n")[0]
    header={'Authorization': 'Bearer %s' %token}
    assignmentStudentsURL = 'https://psu.instructure.com/api/v1/courses/'+courseID+'/assignments/'+assignmentID+'/gradeable_students?per_page=1000' 
    #assuming less than 1000 students in a course 
    userProfileURL='https://psu.instructure.com/api/v1/users/%s/profile'
    rAS={}
    try:
        response = requests.get(assignmentStudentsURL, headers=header)
        if response.status_code == 200:
            rAS=response.json()
        else:
            print "couldn't get response from instructure API, http error %s" %response.status_code                  
    except Exception,e:
        print "Couldn't reach instructure API: %s" % e
    print "student info for assignment {0} in course {1} obtained, gathering student ids".format(assignmentID,courseID)
    students=[]  
    for rA in rAS:
        try: 
            response = requests.get((userProfileURL % rA['id']), headers=header)
            if response.status_code == 200:
                userID=response.json()['primary_email']
                students.append({userID:(rA['display_name'],rA['id'])})
            else:
                print "couldn't get response from instructure API, http error {0}, student display name {1}, student id {1}"\
                .format(response.status_code, rA['display_name'], rA['id'])                    
        except Exception,e:
            print "Couldn't reach instructure API: %s" % e
    return students 

def main():
    #courseId=sys.argv[1]
    #assignmentID=sys.argv[2]
    courseID=COURSEID
    assignmentID=ASSIGNMENTID
    pprint(getStudents(courseID,assignmentID))         

if __name__ == "__main__":
    main()         
