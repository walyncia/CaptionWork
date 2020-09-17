#inserting caption into incontinous data structure for purpose of retrieval

class Node:
    def __init__(self, caption):
        self.caption = caption
        self.link =None

class CaptionList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, caption):
        temp = Node(caption)
        temp.link = self.head
        self. head = temp
    def insert_at_end(self, caption):
        temp = Node(caption)
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                current = current.link
            current.link = temp
        
    def approval(self, caption):
        #OrginalList = CaptionList()
        factor = int(input(caption + '\n\t Approve (1) Reject (0):'))
        if factor == 1:
            rank = True
            OrginalList.insert_at_end(caption)
        else:
            rank = False

            
    def write_to_file(self):
        outfile = open('CaptionsDatabase.txt','w')

        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                outfile.write('\n' + current.caption)
                current= current.link

            return count
        outfile.close()
        
    def traverse_list(self):
        current = self.head
        while current is not None:
            print(current.caption, end= '-')
            current= current.link
            
    def read_infile(self):
        OrginalList = CaptionList()
        infile = open('CaptionsDatabase.txt','r')
        captionsOne = infile.readlines()
        for x in range (len(captionsOne)):
            captionsOne[x] = captionsOne[x].rstrip('\n')
            OrginalList.approval(captionsOne[x])
            if not OrginalList:
                OrginalList.insert_at_start(captionsOne[x])
            else:
                OrginalList.insert_at_end(captionsOne[x])
        OrginalList.traverse_list()
        infile.close()

OrginalList = CaptionList()
OrginalList.read_infile()
OrginalList.approval('f')
OrginalList.write_to_file()
#OrginalList.read_infile()
OrginalList.traverse_list()
