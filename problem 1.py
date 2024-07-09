letters={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred',
    1000:'thousand'
}
#numbers from 1 to 10
o=0
for n in range(1,11):
    o+=len(letters[n])
print(o)
#numbers from 11 to 20
t=0
for n in range(11,21):
    t+=len(letters[n])
print(t)

#numbers from 20 to 90
tens=0
for n in range(20,91,10):
    tens+=len(letters[n])
print(tens)

print(0+t+tens)
