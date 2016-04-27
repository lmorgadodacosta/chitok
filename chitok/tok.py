from chien.chien import cnendict as cdict

def tokenize(sentence):

    s = list(sentence)

    new_s = []
    skip1 = False
    for i, w in enumerate(s):

        if not skip1:


            try:
                if w+s[i+1] in cdict.keys():

                    big_w = w+s[i+1] 
                    new_s.append(w+s[i+1])
                    skip1 = True

                else:
                    new_s.append(w)
                    skip1 = False
                
            except:
                new_s.append(w)
                skip1 = False

        else:
            skip1 = False
            
                
    return new_s


def main():
    print(tokenize("我喜欢狗"))

if __name__ == '__main__':
    main()
