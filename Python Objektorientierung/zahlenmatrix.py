class Field:
    def __init__(self):
        self.__matrix = [[0,0,0] for x in range(3)]

    def set_element(self, row, col, value):
        self.__matrix[row][col] = value

    def print_matrix(self):
        print(self.__matrix)

    def is_element_in_row(self, row, value):
        return value in self.__matrix[row]

    def is_element_in_col(self, col, value):
        return value in [self.__matrix[0][col], self.__matrix[1][col], self.__matrix[2][col]]

    def is_element_in_col_for(self, col, value):
        liste = []
        for i in range(3):
            liste.append(self.__matrix[i][col])
        return value in liste


mat = Field()
mat.set_element(1,1,1)
mat.print_matrix()
print(mat.is_element_in_col(1,1))
print(mat.is_element_in_row(1,1))
print(mat.is_element_in_col_for(1,1))