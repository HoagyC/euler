def run():
    grid = []
    FILE = open("11grid.txt")
    for row in FILE: grid.append([int(i) for i in row.split(" ")])
    best = 0
    for i in range(16):
        for j in range(16):
            b = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            if b > best:
                best = b
                print(i,j,("r"))
            b = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if b > best:
                best = b
                print(i,j,("d"))
            b = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            if b > best:
                best = b
                print(i,j,("fd"))
            b = grid[i+3][j]*grid[i+2][j+1]*grid[i+1][j+2]*grid[i][j+3]
            if b > best:
                best = b
                print(i,j,("bd"))
    return(best)

if __name__ == "__main__":
    print(run())