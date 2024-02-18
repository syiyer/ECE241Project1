from song import Song
from binary_search_tree import BinarySearchTree
from stack import Stack


class MyPlayer:
    def __init__(self):
        self.songList = []
        self.is_sorted = False
        self.yearMemory = dict()
        self.playHistory = Stack()

    def loadLibrary(self, filename: str):
        file = open(filename, "r")  # Opening filename arg in read mode
        lines = file.readlines()    # Creating list of lines from text
        for line in lines:
            attr = line.split("|")
            item = Song(attr[0], attr[1], attr[2], float(attr[3]), int(attr[4]))
            # Instantiate song instance for each line
            self.songList.append(item)  # append each instance to song list
        file.close()  # close file
        pass

    def quickSort(self):
        self.quickSortHelper(self.songList, 0, len(self.songList) - 1)
        # Call quick sort helper to run quick sort
        self.is_sorted = True
        # Change boolean to inform list has been sorted

    def quickSortHelper(self,songlist, first, last):
        if first < last:
            splitpoint = self.partition(songlist, first, last)
            # Get split point by running partition method
            self.quickSortHelper(songlist, first, splitpoint - 1)
            self.quickSortHelper(songlist, splitpoint + 1, last)
            # Recurse method for both after and before split point
    def partition(self,songlist,first,last):
        pivotvalue = songlist[first].year
        # set pivot value as first item of list year
        leftmark = first + 1
        # set leftmark as second position
        rightmark = last
        done = False
        while not done:
            while leftmark <= rightmark and self.songList[leftmark].year <= pivotvalue:
                leftmark = leftmark + 1
                # Increase left mark by one
            while self.songList[rightmark].year >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1
                # Decrease right mark by one
            if rightmark < leftmark:
                done = True
            else:
                temp = self.songList[leftmark]
                self.songList[leftmark] = self.songList[rightmark]
                self.songList[rightmark] = temp
                # assign temp value to item at rightmark
        temp = self.songList[first]
        self.songList[first] = self.songList[rightmark]
        self.songList[rightmark] = temp
        return rightmark
        # return rightmark from partition to be used in quick sort helper

    def playSong(self, title: str):
        for song in self.songList:  # go through each item in song list
            if song.song_title == title:  # if the corresponding title exists in the list
                self.playHistory.push(song)  # add song played to stack structure
                song.play()  # call play function on corresponding item
                break
        pass

    def getLastPlayed(self):
        item = None
        if self.playHistory.size() != 0:  # check if stack has items in it
            item = self.playHistory.peek()  # assign last played song in history or top of stack as item
        return item
        pass

    @staticmethod
    def hashfunction(song):
        return song.year  # returns year of song as hashvalue
    def buildYearMemory(self):

        # self.yearMemory = {}
        for song in self.songList:  # go through each item in list of songs
            year = self.hashfunction(song)  # assign hashvalue to year
            keys = song.song_title  # assign key as title of song
            if year in self.yearMemory:  # if year already exists in hashtable
                tree = self.yearMemory[year]
                tree.put(keys, song)  # put new song into hashtable at same hashvalue
            else:
                tree = BinarySearchTree()  # create new search tree item
                tree.put(keys, song)  # insert key and song item into tree
                self.yearMemory[year] = tree  # place the tree at the corresponding hashvalue

    def getYearMemory(self, year, title):
        steps = 0  # Number of steps used to search for the song
        the_song = None  # The song
        if year in self.yearMemory:  # Check if the year found in input exists
            if self.yearMemory[year].get(title) is not None:  # find if corresponding title exists
                the_song, steps = self.yearMemory[year].get(title)  # assign song value and amount of steps
        return {"steps": steps, "song": the_song}

    def getSong(self, year, title):

        steps = 0  # Number of steps used to search for the song
        the_song = None  # The song
        for song in self.songList:
            steps += 1  # increase step by one for each iteration
            if song.song_title == title:  # check if input is same as title in list
                the_song = song  # assign value to corresponding title
                break
        # Do not modify the return line, assign proper values for
        # steps and song above
        return {"steps": steps, "song": the_song}


# NO MORE TESTING CODE BELOW!
# TO TEST YOUR CODE, MODIFY test_my_player.py
