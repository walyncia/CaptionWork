#This program inserts caption(s) into the continous data structure of linked
#lists for purpose of retrieval.

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
        self. head = temp
    def insert_at_end(self, caption, user):
        temp = Node(caption, user)
        if self.head is None:
            return
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = temp

            
    def write_to_file(self):
        #write to file of unapproved captions with user
        outfile = open('User-UnapprovedCaptions.txt','a')

        #traversal method to write to the files
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                outfile.write('\n' + current.caption + ',' + current.user )
                current= current.link
            return
        #Close the unapproved and user file
        outfile.close()

        
    def traverse_list(self):
        current = self.head
        count =0
        while current is not None:
            count +=1
            print(count, current.caption, end= ' ')
            current= current.link
def main():
    UnalteredCaptions = CaptionListA()
    user = input("Choose a username!")
    print ('\t\tYou have chosen to input a caption!\n\t\t\t','Welcome ', user)
    caption = input('Enter caption:')
    UnalteredCaptions.insert_at_start(caption, user)
    caption = input('Enter another? If so input a comma between yes and your caption!:\n')
    caption= caption.split(',')
    while caption[0] != 'no' and caption[0]!= 'No':
        UnalteredCaptions.insert_at_end(caption[1], user)
        caption = input('Enter another? If so input a comma between yes and your caption!:\n')
        caption= caption.split(',')
    done= UnalteredCaptions.write_to_file()
    print('Your captions:')
    UnalteredCaptions.traverse_list()
    print('\nHave been entered for evaluation! Have a good day!')
main()
