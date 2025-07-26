class Array:
    """
    Array Data Structure
        - Fixed Size
        - Homogeneous Elements: an array stores elements of the same data type
        - Contiguous Memory Allocation (Not implemented here)
    """

    array_type = None # Supported type is int, float, bool, and str
    size = 0
    array = []

    def __init__(self, array_type, size):

        self.array_type = array_type

        self.size = size

        self.array = [ None for i in range(size) ]

    def set(self, index, element):
        assert type(element) is self.array_type, f"Error: type must be {self.array_type}"
        self.array[index] = element

    def get(self, index):
        return self.array[index]

    def __len__(self):
        return self.size;