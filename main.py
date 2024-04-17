# This entrypoint file to be used in development. Start by reading README.mdfrom pytest import main
#
from arithmetic_arranger import arithmetic_arranger

print(
    'Welcome to the Arithmetic Arranger \n \
     You can enter up to 5 mathematical operations in a single line and the Arithmetic arranger function \
     will format them vertically \n \
     For instance\
     2 + 2\
\
     Will be arranged to\n\
       2\n\
     + 2\n\
     ---\n\
    \n\
    Just keep in mind the following, all operations in a single line separated by comma and each element of the operation \n\
    plus the +/- sing should be separated by and space\
    i.e\
    instead of 2+2 --> 2 + 2 '
)


print('Please enter the aritmethic operations to order: ')
operation = input()
print(arithmetic_arranger(operation.split(',')))
