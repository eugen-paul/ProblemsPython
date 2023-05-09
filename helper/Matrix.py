def rotate_90_degree_anticlckwise( matrix:List[List[int]] ) -> List[List[int]] :
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

def rotate_90_degree_clckwise(matrix:List[List[int]]) -> List[List[int]] :
    return list(list(x)[::-1] for x in zip(*matrix))