# importing library
from difflib import SequenceMatcher
# file path
f1_path='p_check1.txt'
f2_path='p_check2.txt'

# defining file_read to open the file in read mode which is present in mentioned path

def file_read(f_path):
    with open(f_path,'r') as doc:
        return doc.read()

# calling the file_read function to read the 2 documents that were to be checked

f1_content=file_read(f1_path)
f2_content=file_read(f2_path)

# plagiarism_checker is defined which return the perecentage of plagiarism


def plagiarism_checker(f1_content, f2_content):
    match=SequenceMatcher(None,f1_content, f2_content).ratio()
    percentage=int(match*100)
    return [percentage]

# calling plagiarism_checker function and printing the output

percentage=plagiarism_checker(f1_content,f2_content)
print(f"plagirarism percentage {percentage}")