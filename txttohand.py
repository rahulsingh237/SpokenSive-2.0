from PIL import Image

from fpdf import FPDF



imgg=Image.open("file\\bg.png")
sizeOfSheet=imgg.width
gap,_=0,0
allowedchar='qwertyuiopasdfghjklzxcvbnm(),.?;1234567890'

def Write(char):
    if char=='\n':
        pass
    else:
        global gap,_
        char.lower()
        cases=Image.open("file\\%s.png"%char)
        imgg.paste(cases,(gap,_))
        size=cases.width
        gap+=size
        del cases

def Letters(word):
    global gap,_
    if gap > sizeOfSheet-95*(len(word)):
        gap=0
        _+=200
    for letter in word:
        if letter in allowedchar:
            if letter.islower():
                pass
            elif letter.isupper():
                letter.lower()
                letter+='Upper'
            elif letter=='.':
                letter="fullstop"
            elif letter==',':
                letter="comma"

            elif letter==':':
                letter="colon"
            elif letter=='!':
                letter="exclamation"
            elif letter=='?':
                letter="question"

            elif letter=='(':
                letter="bracketclose"
            elif letter==')':
                letter="bracketclose"

            Write(letter)


def Word(Input):
    wordlist=Input.split(' ')
    for i in wordlist:
        Letters(i)
        Write('space')




def input_out(text):

    f = open("file\\black.txt","w")
    f.write(text)
    f.close()



    try:
        with open("file\\black.txt",'r') as file:
            data=file.read().replace('\n','')
            l=len(data)
            nn= 1
            print(nn)
            print(l)
            chunks,chunk_size=len(data),len(data)//nn+1
            p=[data[i:i+chunk_size] for i in range(0,chunks,chunk_size)]

            for i in range(0,len(p)):
                Word(p[i])
                Write('\n')
                imgg.save("images\\%doutt.png"%i)
                img1=Image.open("C:\\Users\\asus\\Desktop\\lakshit\\Python programs\\Hand\\file\\bg.png")
                #imgg=img1
                gap,_=0,0
    except ValueError as E:
        print("{}\nTry again",format(E))
    '''imageList=[]
    for i in range(0,len(p)):
        imageList.append("C:\\Users\\asus\\Desktop\\lakshit\\Python programs\\Hand\\file\\%doutt.png"%i)
        if i == len(p)-1:
            print("aagya mein")
            exit
'''

    '''cover=Image.open(imageList[0])
    width,height=cover.size
    pdf=FPDF(unit="pt",format=[width,height])
    for i in range(0,len(imageList)):
        pdf.add_page()
        pdf.image(imageList[i],0,0)
    pdf.output("C:\\Users\\asus\\Desktop\\lakshit\\Python programs\\Hand\\file\\neww_2.pdf","F")'''

    img = Image.open('images\\0outt.png')
    img.show()

    text=""






