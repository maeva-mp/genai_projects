#Daily challenge: Solve the Matrix

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

#Step 1: Transforming the String into a 2D List
rows = MATRIX_STR.strip().split('\n')
matrix = [list(row) for row in rows]

#Step 2: Processing Columns
message = []

for col in range(len(matrix[0])):
     for row in range(len(matrix)):
          message.append(matrix[row][col])

print("Column message:", message)

# Step 3: Filtering Alpha Characters
filtered = []

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]
        if char.isalpha():
             filtered.append(char)

# print("Filtered message:", filtered)

#Step 4: Replacing Symbols with Spaces
cleaned = []
symbols = []

for char in message:
    if char.isalpha():
        if symbols:
            cleaned.append(" ")
            symbols = []
        cleaned.append(char)
    else:
        symbols.append(char)

#Step 5: Constructing the Secret Message
print("Decoded message:", ' '.join(cleaned))


