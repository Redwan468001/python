# Initial dictionary
x = {('ABCD', 'ABCD'):1,( 'AB','AB'): 2, ('BC','BC'): 0, ('ACBD','ACDD'):2, ('ABCDED','ABCDDS'):2}
# Create a copy of the original dictionary
x_copy = x.copy()

# Iterate through the keys and values of the original dictionary
for key, value in x.items():
    # Check if the first element of the current key is present in the first element of any other key
    if any(key != k and key[0] in k[0] and value < v for k, v in x.items()):
        #print(key[0], k[0], value, v)
        del x_copy[key]



# Replace the original dictionary with the modified copy
x = x_copy

# Print the updated dictionary
print(x)
