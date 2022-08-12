# TestSuiteALAN

Test suite for scanner. 
Clone the repository in the same directory which contains the "alan" directory and run scanner.py inside the TestSuiteALAN directory in terminal with appropriate arguments shown below. 

1. **Comments**
	`python3 scanner.py comments`
	- nested comments
	- error messages; testing position
	- curly brackets inside string literals
	- block comments with error; testing position
	
2. **String Literals**
	`python3 scanner.py strings`
	- escape codes 
	- multi line string literal error
	- illegal escape codes
	- " at end
	- empty string
	- "untidy"strings"
	
3. **Error handling**
	`python3 scanner.py errors`
	- illegal characters
	- numbers too long
	- identifiers too long
	- error precedence
	- string not closed
	- comment not closed; normal and nested testing position
	
4. **All available**
	`python3 scanner.py all`
	- tests all above, and more.
	
4. **Official Test Script provided**
	`python3 scanner.py official1`
	- tests all above, and more.
	
--- 

To add test cases, add xxx.alan file to appropriate folder in TestCases/ and xxx.txt to Results/
where xxx is the same name.
	
	
