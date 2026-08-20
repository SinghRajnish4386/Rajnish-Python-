def reverse_file_content(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Reverse the content
        reversed_content = content[::-1]
        
        # Open the output file in write mode and save the reversed content
        with open(output_filename, 'w') as outfile:
            outfile.write(reversed_content)
        
        print(f"Content from '{input_filename}' has been reversed and saved to '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    
# Main program to take input and output file names
def main():
    input_filename = input("Enter the name of the input file: ")
    output_filename = input("Enter the name of the output file: ")
    
    # Reverse the content and save to another file
    reverse_file_content(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
