# TestSuiteALAN

## Cloning
1.`clone https://github.com/jjvraw/TestSuiteALAN.git` into the directory/folder which holds your alan folder.
2. Navigate to directory `cd TestSuiteALAN`
3. Run a script `python3 test.py xxx`

---
## Testing CodeGen
1.**Test funcdef and vardef**
`python3 test.py funcdef`
	- all official testcases without any errors 
> (1) should run without any errors to continue with codegen

---
## Testing HashTable
1. **Test HashTable**
`python3 test.py hash`
	- should run without any problems
	- inserts 100,000+ random strings in hashtable

---
## Testing Type Checking 
1. `python3 test.py typechecking official`
	- runs through and compares official test cases

---

## Testing Parser 
> Can only be used before any TypeChecking additions have been made 
1. **Run test cases**
`python3 test.py most`

2. **Run 10k generated test cases**
`python3 test.py tenthousand`
	- thanks Iain.

3. **Run official tests**
`python3 test.py official`

---

## Testing Scanner
1. **Comments**
	`python3 test.py comments`
	- nested comments
	- error messages; testing position
	- curly brackets inside string literals
	- block comments with error; testing position
	
2. **String Literals**
	`python3 test.py strings`
	- escape codes 
	- multi line string literal error
	- illegal escape codes
	- " at end
	- empty string
	- "untidy"strings"
	
3. **Error handling**
	`python3 test.py errors`
	- illegal characters
	- numbers too long
	- identifiers too long
	- error precedence
	- string not closed
	- comment not closed; normal and nested testing position
	
4. **All available**
	`python3 test.py all`
	- tests all above, and more.
	
4. **Official Test Script provided**
	`python3 test.py official`
	- unit tests provided.	
--- 