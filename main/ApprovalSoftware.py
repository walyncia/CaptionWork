class Node:
    def __init__(self, caption, user):
        self.caption = caption
        self.user = user
        self.link =None

class CaptionListA:
    def __init__(self):
        self.head = None

    def insert_at_start(self, caption,user):
        temp = Node(caption, user)
        temp.link = self.head
        self.head = temp
        
    def insert_at_end(self, caption, user):
        temp = Node(caption, user)
        if self.head is None:
            return
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = temp
            
    def Straverse_list(self):
        current = self.head
        while current is not None:
            print(current.caption,current.user, end= '-')
            current= current.link

            
    def write_to_file(self):
        #open the approved, rejected and collective captions files
        outfileA = open('ApprovedCaptions.txt','a')
        outfileB = open('RejectedCaptions.txt','a')
        outfileC = open('CollectiveCaptions.txt','a')
        if self.head is None:
            return 'Nothing to write'
        else:
            current = self.head
            #running total of
            count =1
            while current is not None:
                factor = int(input('\n' + current.caption + '\n\t Approve (1) Reject (0):'))
                if factor == 1:
                    outfileA.write(current.caption + ',' + current.user + '\n')
                    outfileC.write(current.caption + ',' + current.user + ',APPROVED\n')
                    count +=1
                else:
                    outfileB.write(current.caption + ',' + current.user + '\n')
                    outfileC.write(current.caption + ',' + current.user + ',REJECTED\n')
                    count +=1
                current= current.link
            return '\nApproval Completed for ' + str(count) +' Caption(s)!'
        outfileA.close()
        outfileB.close()
        outfileC.close()

        
    def read_infile(self):
        OriginalList = CaptionListA()
        #open the unapproved captions file in read mode
        infile = open('User-UnapprovedCaptions.txt','r')
        
        #insert the first caption and corresponding user as the head of linked list
        captionsOne = infile.readline()
        captionsOne = captionsOne.rstrip('\n')
        captionsOne = captionsOne.split(',')
        OriginalList.insert_at_start(captionsOne[0], captionsOne[1])
        
        #use a while loop to insert the captions into a linked list
        captionsOne = infile.readline()
        while captionsOne != '':
            captionsOne = captionsOne.rstrip('\n')
            captionsOne = captionsOne.split(',')
            OriginalList.insert_at_end(captionsOne[0], captionsOne[1])
            print(captionsOne, '\n')
            captionsOne = infile.readline()
            
        #print list to check structure
        #OriginalList.Straverse_list()
        
        print(OriginalList.write_to_file())
        infile.close()
        
        #clear the unapproved text file
        infile = open('UserUnapprovedCaptions.txt','w').close()



    
def main():
    OriginalList = CaptionListA()
    OriginalList = OriginalList.read_infile()

main()
