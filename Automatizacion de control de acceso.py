# Assign `import_file' to the name of the file
import_file = "allow_list.txt"

# Define `remove_list` with IPs to be removed
remove_list = ["192.168.X.X", "10.0.X.X"]

# Build `with' statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `. read()` to read the imported file and store it in a variable named
    ip_addresses = file.read()

# Use `. split()` to convert `ip_addresses' from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
# Name loop variable `element
# Loop through `remove_list'
for element in remove_list:

    # Create conditional statement to evaluate if `element' is in `ip_addresses
    if element in ip_addresses:

        # use the `. remove( )` method to remove
        # elements from `ip_addresses'
        ip_addresses.remove(element)

# Convert `ip_addresses' back to a string so that it can be written into the text file
ip_addresses = "\n".join(ip_addresses)

# Build `with' statement to rewrite the original file
with open(import_file, "w") as file:
    # Rewrite the file, replacing its contents with `ip_addresses '
    file.write(ip_addresses)

