# Regular Expressions use re module  regular expressions is for searching the patterns
print("\tTab")  # it give space
print(r"\tTab")  # it does not give space

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234


cat
mat
pat
bat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''


										#characters to match in text_to_search like Ha k

# pattern = re.compile(r"abc")
# pattern = re.compile(r".")
# pattern = re.compile(r"\.")
# pattern = re.compile(r"\bHa")
# pattern = re.compile(r"\BHa")
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)
    # print(text_to_search[256:257])  # output abc


										# pattern matching for phone numbers in text to search

# pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

										# pattern matching for Data.txt file

# pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
# matches = pattern.finditer(text_to_search)
# if u get a unicodeDecode error asccii code cannot decode byte oxe2 then add encoding='utf-8' in below line ok after r
# with open("30.2_Data.txt", "r") as f:
#     content = f.read()
#     matches = pattern.finditer(content)
#     for match in matches:
#         print(match)

									# Pattern Matching for Data.txt file for 800 to 900 numbers searchable

# pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")			# pattern only matching for - and .
# matches = pattern.finditer(text_to_search)
# with open("30.2_Data.txt", "r") as f:
#     content = f.read()
#     matches = pattern.finditer(content)
#     for match in matches:
#         print(match)


									# pattern matching for phone numbers in text to search

# pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")			# pattern only matching for - and .
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

									# pattern matching for 800 to 900 in text_to_search

# pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")			# pattern only matching for - and .
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

		# quantifiers for matching more than one character in text_to_search file


# pattern = re.compile(r"\d{3}.\d{3}.\d{4}")			# pattern only matching for series of numbers
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


#use findall method also but compared to findall finditer has more useful got it
# pattern = re.compile(r"\d{3}.\d{3}.\d{4}")			# pattern only matching for series of numbers
# matches = pattern.findall(text_to_search)
# for match in matches:
#     print(match)



#pattern matching for Mr Ms and Mrs in text_to_search  
# pattern = re.compile(r"Mr\.")			# pattern only matching for Mr.
# pattern = re.compile(r"Mr\.?")			# pattern only matching for Mr. and Mr
# pattern = re.compile(r"Mr\.?\s[A-Z]")			# pattern only matching for Mr. and Mr and upper characters
# pattern = re.compile(r"Mr\.?\s[A-Z]\w+")			# pattern only matching for Mr. and Mr with words
# pattern = re.compile(r"Mr\.?\s[A-Z]\w*")			# pattern only matching for Mr. and Mr with words include T because of *
# # pattern only matching for Mr. and Mr Mrs with words because of Group patterns use () for create Groups*
# pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")			
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# pattern = re.compile(r"[A-Z]")			# pattern only matching for in the range mention.
# pattern = re.compile(r"[0-5]")			# pattern only matching for in the range mention.
# pattern = re.compile(r"[a-zA-Z0-9]")			# pattern only matching for in the range mention.
# # ^(caret) if it is outside of the character set that matches the beginning of the string. 
# # ^ if it is in the characterset it negates the setand matches everything that is not in character set  
# pattern = re.compile(r"[^a-zA-Z0-9]")			#means it negates lower case uppercase words and numbers 
# pattern=re.compile(r"[^p]at")					#negate the bat word in text to search ok na
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# sentence = "Start a sentence and then bring it to an end"
# pattern = re.compile(r'^Start')			#gives output beginning of the string 	like
# pattern = re.compile(r'end$')			#gives output end of the string like	end
# # matches = pattern.finditer(sentence)

# print(match)

# for match in matches:
#     print(match)


#use finditer method in regular expression
# sentence = "Start a sentence and then bring it to an end"
# # pattern = re.compile(r'^Start')			#gives output beginning of the string 	like
# # pattern = re.compile(r'end$')			#gives output end of the string like	end
# # matches = pattern.finditer(sentence)

# print(match)

# for match in matches:
#     print(match)


#use match method of regular expression

# sentence = "Start a sentence and then bring it to an end"
# pattern = re.compile(r'Start')	
# pattern = re.compile(r'sentence')			#gives output beginning of the string Start i comment for loop because match does not able to iter
# matches = pattern.match(sentence)			#None because it gives strting string only contains if it does not contains result was 0
# matches = pattern.search(sentence)


# print(matches)							

# for match in matches:
#     print(match)




#Flags in regular Expression is very useful in Python but there are lot more methods cover in next videos corey babai
# sentence = "Start a sentence and then bring it to an end"
# pattern = re.compile(r'[Ss][Tt][Aa]')		#normal way for pattern method
# pattern = re.compile(r'start',re.IGNORECASE)		#Flag way for pattern method
# pattern = re.compile(r'start',re.I)					# short hand notation Flag way for pattern method
# matches=pattern.search(sentence)
# print(matches)							