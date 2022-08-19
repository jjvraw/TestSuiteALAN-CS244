# TestSuiteALAN

## How to Clone
Go into the directory/folder which holds your alan folder.

1. Then in termianl, in the directory type `clone https://github.com/jjvraw/TestSuiteALAN.git` 
2. Navigate to directory `cd TestSuiteALAN`
3. Run a script `python3 scanner.py all`

---
## For Testing Parser 
1. **Run test cases**
`python3 parser.py`

2. **Run 10k generated test cases**
`python3 parser.py tenthousand`
	- thanks Iain.

3. **Run offical tests**
`python3 parser.py offical`

---

## For Testing Scanner

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
	`python3 scanner.py official`
	- unit tests provided.	
--- 

To add test cases, add xxx.alan file to appropriate folders in TestCases/ and xxx.txt to Results/
where xxx is the same name.
	
	
