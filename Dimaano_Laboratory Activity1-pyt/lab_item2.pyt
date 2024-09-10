def main():
    print("Getting the Greater Value")
    
def main():
    print("Getting the Greater Value")
    
    # Input two space-separated characters
    input_chars = input("Enter two space-separated characters: ").split()
    
    if len(input_chars) != 2:
        print("Error: You must enter exactly two characters.")
        return
    
    char1, char2 = input_chars
    
    if len(char1) != 1 or len(char2) != 1:
        print("Error: Each input must be a single character.")
        return
    
    if char1 == char2:
        print("\n-------------------------------------------------------------")
        print(f"Both characters are the same: {char1}")
        print("-------------------------------------------------------------")
    else:
        # Get the greater character
        greater_char = max(char1, char2)
        
        print("\n-------------------------------------------------------------")
        print(f"The character with greater value is: {greater_char}")
        print("-------------------------------------------------------------")
    
    print("Showing the ASCII Codes")
    print(f"{char1} : {ord(char1)}")
    print(f"{char2} : {ord(char2)}")

if __name__ == "__main__":
    main()