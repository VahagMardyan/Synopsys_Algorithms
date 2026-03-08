char = input("Input string: ")

for ch in char:
    print(f"The ASCII code of '{ch}' is {ord(ch)}")

response = input("Do you want to get decoded character by ASCII code? ")

if response[0] in ['y', 'Y']:
    ascii_code = int(input("Input an integer: "))
    print(f"The char from ASCII code {ascii_code} is: '{chr(ascii_code)}'")

