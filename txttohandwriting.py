from PIL import Image
from fpdf import FPDF
from PIL import Image
import os
BG = Image.open("myfont/bg.png")
sizeOfSheet = BG.width
gap, _ = 0, 0
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'

def writee(char):
    global gap, _
    if char != '\n':
        cases = Image.open("myfont/%s.png" % char.lower())
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size

def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95 * (len(word)):
        gap = 0
        _ += 200
    special_char = {'.':'fullstop','!':'exclamation','?':'question',',':'comma','(':'braketop', ')':'braketcl','-':'hiphen'}
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif special_char[letter] != None:
                letter = special_char[letter]
            writee(letter)


def worddd(Input):
    wordlist = Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')


if __name__ == '__main__':
    try:
        with open('boom.txt', 'r') as file:
            data = file.read().replace('\n', '')

        with open('final_output.pdf', 'w') as file:
            pass

        l = len(data)
        nn = len(data) // 600
        chunks, chunk_size = len(data), len(data) // (nn + 1)
        p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        for i in range(0, len(p)):
            worddd(p[i])
            writee('\n')
            BG.save('%doutt.png' % i)
            BG1 = Image.open("myfont/bg.png")
            BG = BG1
            gap = 0
            _ = 0
    except ValueError as E:
        print("{}\nTry again".format(E))

imagelist = []
for i in range(0, len(p)):
    imagelist.append('%doutt.png' % i)

#Converting images to pdf
#Source:https://datatofish.com/images-to-pdf-python/


def pdf_creation(PNG_FILE, flag=False):
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])  # paste using alpha channel as mask
    rgb.save('final_output.pdf',
             append=flag)  #Now save multiple images in same pdf file


#First create a pdf file if not created
pdf_creation(imagelist.pop(0))

#Now I am opening each images and converting them to pdf
#Appending them to pdfs
for PNG_FILE in imagelist:
    pdf_creation(PNG_FILE, flag=True)
