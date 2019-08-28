import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://')
# pattern = re.compile(r'https?://(www\.)?\w+')
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # using group expressions
# matches = pattern.finditer(urls)
# for match in matches:
#     # print(match)
#     # print(match.group(0))
#     # print(match.group(1))
#     # print(match.group(2))
#     print(match.group(2))


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # using group expressions
sub_url = pattern.sub(r"\2\3", urls)
print(sub_url)
