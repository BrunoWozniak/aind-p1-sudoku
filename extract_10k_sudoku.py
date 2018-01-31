import pandas as pd

input_file = 'sudoku.csv'
output_file = '10k_sudoku.csv'
numrows = 10000 #number of rows I want
df= pd.DataFrame(pd.read_csv(input_file, sep=','))
df.ix[:numrows,0].to_csv(output_file, mode='a', header=None, index=None)
