# Python Project on Password Generator
##(Random Password Generator and Based on Condition)

##Introduction
###In an age where online security is paramount, creating strong and unique passwords is critical to protecting personal information from unauthorized access. This mini-project focuses on developing a password generator in Python that generates random passwords based on user-defined conditions.
The password generator allows users to specify various criteria, including the desired length of the password and the types of characters it should contain, such as uppercase letters, lowercase letters, numbers, and special symbols. By customizing these parameters, users can create secure passwords tailored to their needs.
Using built-in Python libraries, this project emphasizes simplicity and usability, while ensuring that generated passwords are random and secure. Through this mini project, we aim to provide a practical tool that increases password security for users in their digital lives.


###Scenario 1
The First option is to generate the password based on the requirements provided by the user. In which the requirements include how many alphabets, digits, special characters, and overall total length of the password are required.

###Scenario 2
The second option is generating a random password based on the password length that we are providing. Here there is no other input required from the user-side.


## Modules Used

### String 
- `string.ascii_letters` Concatenation of the ascii 
- `string.digits` The string ‘0123456789’.
- `string.punctuation` String of ASCII characters which are considered punctuation characters in the C locale.

### Random
- `choice` method returns a randomly selected element from the specified sequence. The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
- `sample` function for random sampling, randomly picking more than one element from the list without repeating elements. It returns a list of unique items chosen randomly from the list, sequence, or set.


##Output
Please Select the below options

1 - Generating based on Conditions
2 - Randomly Generating the Password
 Enter the Option: 1
Enter the Password Length: 16
Enter the Alphabets Count in Password: 6
Enter the Digits Count in Password: 4
Enter the Special Characters Count: 5
UyqxYf4616.{%@.:
```

### Secnario - 2

```sh
python3 password.py
Please Select the below options

1 - Generating based on Conditions
2 - Randomly Generating the Password
 Enter the Option: 2
Enter the Password Length: 16
?@:W(=,e^Nto+%Au
```


