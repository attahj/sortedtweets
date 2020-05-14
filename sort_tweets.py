from datetime import datetime
import sys

#This class is used to create a way to store the information from the files
class Tweets:
	def __init__(self,user,tweet,time):
		self.user = user
		self.tweet = tweet
		self.time = time.strip(" ")
		time = time.strip(" ")

		
#this is the main method
def main():
    x = []
    file1= sys.argv[1]
    print(file1)
    file2 = sys.argv[2]
    print(file2)
    s = read_records(file1)
    x = create_record(s)
    s = read_records(file2)
    z = create_record(s)
    len1 = len(x)
    len2 = len(z)
    print("\n\n\n")
    print("Reading files...")
    if (len1>len2):
        print(file1+" contained the most tweets with " + str(len1))
    elif (len2>len1):
        print(file2 +" contained the most tweets with " + str(len2))
    else:
        print("both files contained the same amount of tweets")
    x.extend(z)
    sorted_list = merge_and_sort_tweets(x)
    print("Merging files...")
    print("Writing file...")
    write_records(sorted_list)
    print("File written. Displaying 5 earliest tweeters and tweets")
    for i in range(0,5) :
        print(sorted_list[i].user,sorted_list[i].tweet,sorted_list[i].time)
        
#This is used to input the files into the method then it kicks out every new
#line as a list        
def read_records(file):
	f = open(file, "r")
	l = []
	for i in f.readlines():
		l.append(i)
	return l

#creating list of records from texts read from the txt files
def create_record(s):
	final_l = []
	for i in s:
		dic = {}
        #indexes
		at_sign = i.find("@")
		quot_1 = i.find('"')
		quot_2 = i.rfind('"')
        
    #building objects
		dic["handle"] =  i[at_sign+1: quot_1-1]
		dic["tweet"] = i[quot_1:quot_2]
		dic["timestamp"] = i[quot_2+2:].strip("\n")
		t = Tweets(dic["handle"], dic["tweet"], dic["timestamp"])
        #add to list of objects
		final_l.append(t)
	return final_l

#tweets get sorted here but not merged (done in create_record)
def merge_and_sort_tweets(l):
	l.sort(key=lambda date: datetime.strptime(date.time, "%Y %m %d %H:%M:%S"))
	return l
  
#in this method we then write the list of tweet objects into a txt file
def write_records(sorted_list): 
    with open('sorted_demo.txt', 'w') as g:
        for i in sorted_list:
            g.write(i.user + " " + i.tweet+ " " + i.time + "\n")

main()

   

