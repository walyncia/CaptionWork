#This program takes interacts with the approval database for our captions ideal.


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
        outfile = open('UserUnapprovedCaptions.txt','a')
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                outfile.write('\n' + current.caption + ',' + current.user )
                current= current.link
            return 
        outfile.close()
        
    def traverse_list(self):
        current = self.head
        while current is not None:
            print(current.caption, end= '-')
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
    print(UnalteredCaptions.write_to_file())
    UnalteredCaptions.traverse_list()
main()
