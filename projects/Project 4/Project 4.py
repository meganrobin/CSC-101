#Imports#
import os
import json
import unittest

#Defining the global variables that will hold the total combined stats for all of the data files combined#
global total_accounts_missing_data
total_accounts_missing_data = 0
global total_weak_passwords
total_weak_passwords = 0
global total_potential_duplicates
total_potential_duplicates = 0
global accounts_amount
accounts_amount = 0

# Setup and File Exploration
def get_file_paths(root_dir):
    # Implement the directory traversal and file collection logic
    try:
        filepaths = []  #List to store file paths
        for root, dirs, files in os.walk(root_dir): # Walks the directory
            for file in files:
                if file.endswith(".txt"): #Joins the two strings to form the full filepath
                    filepath = os.path.join(root, file)
                    filepaths.append(filepath)  #Adds it to the list
        return filepaths
    except FileNotFoundError:
        print("One of the files does not exist.")
    except PermissionError:
        print("You do not have permission to open one of the files.")

# Loading and Handling Wordlist - NOT USED
def load_wordlist(wordlist_path):
    # Implement the logic to read the wordlist file
    with open(wordlist_path, 'r') as file:
        wordlist = file.read()
    return wordlist #returns the read file which is a string#

# Decryption Functions - NOT USED
def generate_key_combinations(wordlist):
    # Implement the combination generation logic
    keywords = list(wordlist.split(" ")) #creates a list of all the three letter keys from the string#
    key_combinations = []
    for i in range(len(keywords)):
        for j in range(len(keywords)):
            key_combinations.append(keywords[i] + keywords[j])
    
    return key_combinations #returns the list of all the combinations#

def decrypt_file(file_path, key):
    # Implement the decryption logic

    decrypted_string = ''
    with open(file_path, 'r') as file: 
        content = file.read() #Reads the file and assigns it to the string var content#
        for char in content: #Iterates through all the characters in the content#
            ascii = ord(char) #ascii rep
            decrypted = (ascii - key) % 128
            converted_to_char = chr(decrypted)
            decrypted_string += converted_to_char
        
    return decrypted_string
# Data Parsing and Validation
def parse_decrypted_data(decrypted_content):
    # Implement the parsing logic
    if 'Username' in decrypted_content:
        dictionary = json.loads(decrypted_content)
        return dictionary

def validate_data_format(parsed_data):
    if isinstance(parsed_data, list): #Checks to see if parsed data is a list#
        for dic in parsed_data:
            if isinstance(dic, dict) == False: #Checks to see if parsed data is a list of dictionaries#
                return False #Returns False if its not a list of dictionaries#
        return True #Returns True to notify that the parsed_data was correctly converted into a python dictionary#
    else:
        return False

# Security Analysis Functions
def detect_missing_data(data_entry):
    #Define all needed variables#
    total_accounts = 0
    usernames_missing = 0
    passwords_missing = 0
    emails_missing = 0
    creation_dates_missing = 0
    login_dates_missing = 0
    balances_missing = 0
    account_numbers_missing = 0

    null_values = 0
    empty_values = 0
    placeholder_values = 0

    for dic in data_entry: #Iterates through all the dictionaries in the data file#
        global total_accounts_missing_data
        total_accounts += 1 #Increments the total account counter var#

        #Checks to see if there are any missing keys in the dictionary#
        if 'Username' not in dic:
            usernames_missing += 1
        if 'Password' not in dic:
            passwords_missing += 1
        if 'Email' not in dic:
            emails_missing += 1
        if 'Date Created' not in dic:
            creation_dates_missing += 1
        if 'Last Login' not in dic:
            login_dates_missing += 1
        if 'Account Balance' not in dic:
            balances_missing += 1
        if 'Account Number' not in dic:
            account_numbers_missing += 1

        if ('Username' not in dic) or ('Password' not in dic) or ('Email' not in dic) or ('Date Created' not in dic) or ('Last Login' not in dic) or ('Account Balance' not in dic) or ('Account Number' not in dic):
            total_accounts_missing_data += 1 #Increments the total amount of files that have missing data by checking whether the file is missing any of its keys#

        for v in dic.values(): #Iterates through all the values in the dictionary#
            if v == "null":
                null_values += 1 #Checks if there's any null values#
            if v == "" or v == " ":
                empty_values +=1 #Checks if there's any empty values#
            if v == "not_provided":
                placeholder_values += 1 #Checks if there's any placeholder values#

    #Return a bunch of data about what was potentially missing from the keys and potential empty, null, or placeholder strings in the values#
    return [total_accounts, usernames_missing, passwords_missing, emails_missing, creation_dates_missing, login_dates_missing, balances_missing, account_numbers_missing, null_values, empty_values, placeholder_values]

def detect_duplicate_accounts(data):
    # Implement the duplicate account detection logic
    usernames = []
    emails = []
    account_numbers = []
    duplicates = 0

    for dic in data: #Iterate through all the dictionaries in the data#
        for key in dic:
            if key == 'Username': #Finds correct key#
                usernames += dic['Username']
            if key == 'Email': #Finds correct key#
                emails += dic['Email']
            if key == 'Account Number': #Finds correct key#
                account_numbers += dic['Account Number']

    for dic in data:
        if (usernames.count(dic['Username']) > 1) or (emails.count(['Email']) > 1) or (account_numbers.count(['Account Number']) > 1): #Checks and sees if the value for Username, Email, or Account Number is in the corresponding list of all Usernames, Emails, or Account Numbers more than once#
            global total_potential_duplicates
            total_potential_duplicates += 1 #Increments the global variable containing the total amount potential duplicate accounts across all decryptable files#
            duplicates += 1 #Increments if potential duplicate is found#
            
    return duplicates #Returns an int value that is the total amount of potential duplicates in the data file#

def is_password_weak(password):
    special_list = "!@#|?><.,~`:;$%^&*()_+=-][}{"#String containing special characters#
    lower = 0
    upper = 0
    number = 0
    special = 0
    #Checks that password is at least 8 characters long#
    if len(password) > 7: 
        for char in password:
            if char.islower(): #Counts how many lower case letters are in password#
                lower += 1
            if char.isupper():#Counts how many upper case letters are in password#
                upper += 1
            if char.isdigit(): #Counts how many numbers are in password#
                number += 1
            if char in special_list:  #Counts how many special characters are in password#
                special += 1

    if (lower >= 1 and upper >= 1 and number >= 1 and special >= 1):
        return 0 #Returns 0 if the password meets all the criteria#
    else:
        global total_weak_passwords
        total_weak_passwords += 1 #Increments the global variable containing the total amount of weak passwords across all decryptable files#
        return 1 #Returns 1 if the password doesn't meet all criteria#

# Statistical Analysis
def calculate_statistics(file_number, file_path, missing_data_list, weak_passwords, duplicate_accounts):
    #Creates a string with all the data about the file organized in a tidy way#
    stats = f"Decryptable File Number {file_number}: {file_path}\nTotal Accounts: {missing_data_list[0]}\nUsernames Missing: {missing_data_list[1]}\nPasswords Missing: {missing_data_list[2]}\nEmails Missing: {missing_data_list[3]}\nCreation Dates Missing: {missing_data_list[4]}\nLogin Dates Missing: {missing_data_list[5]}\nBalances Missing: {missing_data_list[6]}\nAccount Numbers Missing: {missing_data_list[7]}\nNull Values: {missing_data_list[8]}\nEmpty Values: {missing_data_list[9]}\nPlaceholder Values: {missing_data_list[10]}\nPercent of Passwords Determined Weak: {(weak_passwords/missing_data_list[0])*100}%\nPercent of Potential Duplicate Accounts: {(duplicate_accounts/missing_data_list[0])*100}%\n\n"

    return stats #Returns this created string#
# Report Generation
def generate_report(statistics, amount_decryptable, amount_of_files, accounts_amount):
    with open(os.path.abspath("projects\Project 4\Reencrypted Data\Final Report"), 'w') as file:
        file.writelines(statistics)
        file.write(f"Total Accounts Reviewed: {accounts_amount}\nTotal Files: {amount_of_files}\nTotal Amount of Accounts with Weak Passwords: {total_weak_passwords}\nTotal Percent of Accounts with Weak Passwords: {((total_weak_passwords)/accounts_amount)*100}%\nTotal Amount of Potential Duplicate Accounts: {total_potential_duplicates}\nTotal Percent of Potential Duplicate Accounts: {((total_potential_duplicates)/accounts_amount)*100}%\nTotal Amount of Accounts with Missing Data: {total_accounts_missing_data}\nTotal Percent of Accounts with Missing Data: {(total_accounts_missing_data/accounts_amount)*100}%\nTotal Amount of Undecryptable Files: {amount_of_files-amount_decryptable}\nTotal Percent Undecryptable: {((amount_of_files-amount_decryptable)/amount_of_files)*100}%\n")

# Re-Encryption
def encrypt_data(data, encryption_key):
    encrypted_string = ''
    for char in data:
        ascii = ord(char) #ascii rep
        encrypted = (ascii - encryption_key) % 128
        converted_to_char = chr(encrypted)
        encrypted_string += converted_to_char
    return encrypted_string

def write_encrypted_data(data, file_path):
    with open(os.path.abspath(file_path), 'w') as file: #Creates a new file, writes the reencrypted data into the new file, then closes the file#
        file.writelines(data)

# Main Function
def main():
    # Get file paths
    file_paths = get_file_paths(os.path.abspath("projects\Project 4\Plain Data"))

    # Process each file
    stats = [] #Container for the stats of every file#
    decryptable = 0 #Number of files that could be decrypted#

    for file_path in file_paths: #Goes through all the found .txt subdirectories from the given directory#
        for key in range(128): #Goes through all valid ASCCI values 0-127#
            decrypted_content = decrypt_file(file_path, key)
            if decrypted_content:
                parsed_data = parse_decrypted_data(decrypted_content) #Checks if the data matches the expected dictionary format, then puts it into a dictionary format#
                if validate_data_format(parsed_data): #Checks if the data matches the expected dictionary format#
                    global accounts_amount
                    
                    print(file_path)
                    print(parsed_data)

                    decryptable += 1
                    missing_data = detect_missing_data(parsed_data)#Missing_data is a list with a bunch of info about which fields don't exist and whether of not there are null, emply, or placeholder values#
                    accounts_amount += missing_data[0]
                    #Count Strong Passwords#
                    weak_passwords = 0
                    if missing_data[1] == 0: #Ensures that the Password field exists#
                        for dic in parsed_data:
                            if 'Password' in dic:
                                weak_passwords += is_password_weak(dic['Password']) #weak_passwords is an int with the ammount of passwords that have been determined weak#
                    
                    #Detect Duplicate Accounts#
                    duplicate_accounts = 0
                    if missing_data[0] == 0: #Ensures that the Username field exists#
                        duplicate_accounts = detect_duplicate_accounts(parsed_data)#Calls the duplicate account function with the file data and stores the resulting list in var duplicate_accounts#

                    stats.append(calculate_statistics(decryptable, file_path, missing_data, weak_passwords, duplicate_accounts))
                    new_file_path = (f"projects\Project 4\Reencrypted Data\File {decryptable}")
                    write_encrypted_data(encrypt_data(str(parsed_data), 45), new_file_path)
                    break

    # Generates the report file
    generate_report(''.join(stats), decryptable, len(file_paths), accounts_amount)

#Test Cases#
class TestProject(unittest.TestCase):
    def test_is_password_weak(self):
        #Ensures that is_password_weak returns 0 when the password is strong#
        self.assertEqual(is_password_weak("Going698_23"), 0)
        self.assertEqual(is_password_weak("Awe_some_9090"), 0)
        self.assertEqual(is_password_weak("34Duck$$5"), 0)
        self.assertEqual(is_password_weak("2Cool-beans455@"), 0)
        #Ensures that is_password_weak returns 1 when the password is Weak#
        self.assertEqual(is_password_weak("3"), 1)
        self.assertEqual(is_password_weak("cool_beans"), 1)
        self.assertEqual(is_password_weak("Fridays70"), 1)
        self.assertEqual(is_password_weak("Awe_some"), 1)

if __name__ == "__main__":
    #unittest.main()
    main()