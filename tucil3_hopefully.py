#function to read some file into a matrix

def fileIntoMatrix (filename):
    with open(filename,'r') as f:
        m = [[int(num) for num in line.split(' ')] for line in f]
    return m;




myMatrix = fileIntoMatrix('input.txt');

print(myMatrix);
