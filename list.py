

class Nlist:
    '''represents numbers within a certain range'''
    
    def __init__(self) -> None:
        self.items = []

    def append(self, item) -> None:
        '''
        Adds an item to the list.

        Parameters: 
        item: value (int, float, str, boolean, object ... etc)

        Return:
        None
        ''' #TODO
        
    def remove(self, item) -> None:
        '''
        removes item from the list

        Parameters:
        item: value (int, float, str, boolean, object ... etc)

        Return:
        None
        ''' #TODO  

    def get(self, index):
        '''
        returns the item at the specified index

        Parameters:
        index (int) : the index of item in the list

        Return:
        item: value (int, float, str, boolean, object ... etc)
        ''' #TODO     

    def size(self) -> int:
        '''
        returns the number of items in the list

        Parameters:
        None

        Return:
        size (int) : the size of the list
        '''  #TODO

    def is_empty(self) -> bool:
        '''
        return true if list has zero items

        Parameters:
        None

        Return:
        bool : true if number of items = 0
        ''' #TODO