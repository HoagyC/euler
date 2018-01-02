def run():
    rows = []
    FILE = open("18triangle.txt")
    for row in FILE: rows.append([int(i) for i in row.split(" ")])
    print(len(rows))
    for i in range(len(rows)-2,-1,-1):
        for j in range(i+1):
            rows[i][j] += max(rows[i+1][j],rows[i+1][j+1])
            
    return(rows[0])
    
if __name__ == "__main__":
    print(run())