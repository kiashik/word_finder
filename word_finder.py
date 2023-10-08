from funcs import *

def print_result(word, direction, row, col):
   """
   word:(string)a single word
   direction: (string) the direction the word was found
   row:(int) the row number the word's first letter is found on
   col: (int) the column number the word's first letter is found on 
   """
   print(word+': '+'('+direction+')'+' '+'row: '+str(row)+' column: '+str(col))

def main():
   get_puzzle =input()
   words = input()
   puzzle = get_puzzle[0:100]
   #words = get_puzzle[100:]

   struc_puzz = structure_puzzle(puzzle)
   struc_words = words.split()

   up_words = find_up(struc_puzz, struc_words)
   down_words = find_down(struc_puzz, struc_words)
   forward_words = find_forward(struc_puzz, struc_words)
   backward_words = find_backward(puzzle, struc_words)

   raw_diagonal_words = [find_diagonal_dr(struc_puzz, word) for word in struc_words]
   tup_diagonal_words = [tup for tup in raw_diagonal_words if tup!='None']###############
   diagonal_words = []

   for tup in tup_diagonal_words:
      if tup!=None:
         for i in range(len(tup)):
            diagonal_words.append(tup[i])

   #words found list variatioins below
   words_found = [up_words, down_words, forward_words, backward_words, diagonal_words]
   
   just_words_found = []
   for lst in words_found:
      for i in range(0, len(lst), 3):
         just_words_found.append(lst[i])

   for word in struc_words:
      if word not in just_words_found:
         words_found.append([word, -1, -1])

   dir_words_found = [up_words, 'chg_dir', down_words, 'chg_dir', forward_words, 'chg_dir', backward_words, 'chg_dir', diagonal_words]

   ord_words_found=[]
   for word in struc_words:
      for i in range(len(words_found)):
         for j in range(len(words_found[i])):
            if word==words_found[i][j]:
               ord_words_found.append(words_found[i][j])
               ord_words_found.append(words_found[i][j+1])
               ord_words_found.append(words_found[i][j+2])
   #words found list variatioins above

   # print('words_found:', words_found, "\n")
   # print('just_words_found:', just_words_found, "\n")
   # print('dir_words_found:', dir_words_found, "\n")
   # print('ord_words_found:', ord_words_found, "\n")

   print("Puzzle:\n")
   for line_lst in struc_puzz: 
      print(line_lst)
   print()
   directon=None
   for i in range(0, len(ord_words_found), 3): #DO NOT DELETE
      if ord_words_found[i] in up_words:
         directon = 'UP'
      elif ord_words_found[i] in down_words:
         directon = 'DOWN'
      elif ord_words_found[i] in forward_words:
         directon = 'FORWARD'
      elif ord_words_found[i] in backward_words:
         directon = 'BACKWARD'
      elif ord_words_found[i] in diagonal_words:
         directon = 'DIAGONAL'  

      if ord_words_found[i+1]!=-1:
         print_result(ord_words_found[i], directon, ord_words_found[i+1], ord_words_found[i+2])    # def print_result(word, direction, row, col):
      else:
         print(ord_words_found[i]+': '+'word not found')




if __name__ == '__main__':
   main()