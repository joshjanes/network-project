from collections import Counter
# Third-party libraries
import numpy as np

def main():
    file = ["eng1.txt"]
    
    char_max = 1200
    loop_count = 0
    correct_count = 0
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    char_count_list = []
    input_list = []
    
    for i in range(len(letters)):
        char_count_list.append([0]*26)
        input_list.append([0]*26)
    
    for filestring in file:
        with open(filestring,encoding="utf8") as f:
            c = Counter()
            for x in f:
                for i in range(len(x)-1):
                    c[x[i:i+2]] += 1
                    
            for i in letters:
                for j in letters:
                    char_count_list[letters.index(i)][letters.index(j)] = c[i+j] + c[i.upper()+j]
            
            max = 0
            for i in range(len(letters)):
                for j in range(len(letters)):
                    if char_count_list[i][j] > max:
                        max = char_count_list[i][j]   
           
            for i in range(len(letters)):
                for j in range(len(letters)):
                    input_list[i][j] = char_count_list[i][j]/max
                    print(letters[i]+letters[j]+ ': %.5f,' % (char_count_list[i][j]/max), end=" ")  
                    
            #print(char_count_list)
            #print(max)
                    
main()