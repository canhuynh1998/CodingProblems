"""
You work at a research lab where the genetic data of the virus 2019-nCoV, better known as COVID, is being sequenced. Using sequencing the structure of its DNA is being analyzed. The DNA sequence of the virus is a string of length 
 containing only the letters G, T, A and C.

The method your research lab uses can only sequence a small section of the DNA sequence at a time. As an example, if the DNA sequence of the virus is of length 
, the method could be used to sequence the section starting with letter number 
 and ending with letter number 
 in its DNA and then sequence the section starting with letter number 
 and ending with letter number 
. If the first sequencing returned GCAT and the second returned ATTC, then it could be deduced that the DNA sequence of the virus is GCATTC.

Using this method various pieces of the DNA sequence of the virus have been sequenced and all that is left to do is piece them together.

Given the pieces that have been sequenced and where each of those pieces start, write a program that pieces them together to find out as much as possible about the DNA sequence of the virus.

Input
The first line of the input contains two integers 
 and 
 (
), the length of the DNA sequence and the number of sections that have been sequenced.

Then there are 
 lines, one for each section that has been sequenced. Each of these lines starts with an integer 
 (
), the position at which this section starts, followed by the section itself which is a string of length 
 (
) which contains only the letters G, T, A and C.

Output
Print a single line containing the letters of the DNA sequence of the virus. If there are many possibilities for some particular letter in the sequence, denote it by ‘?’. If some data is contradictory, like a letter having different values in different sections, instead simply print a single line containing Villa.
Notes: Assigning char to string
"""
def main():
    length, sections = list(map(int, input().split(" ")))
    sequences = ["?"] * length
    contradict = False
    for _ in range(sections):
        if contradict:
            break
        line = input().split(" ")
        start = int(line[0]) - 1
        section = line[1]
        
        for i in range(len(section)):
            if sequences[start + i] != "?" and sequences[start + i] != section[i]:
                contradict = True
                break
            sequences[start + i] = section[i]
    result = "Villa" if contradict else "".join(sequences)
    print(result)

if __name__ == "__main__":
    main()