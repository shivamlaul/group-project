import webbrowser
a=str(input('Enter your name '))
print()
print('Hey ', a, ' welcome to Vibin: ')
print()
print('''Enter 1 for Songs
Enter 2 for Audio stories
Enter 3 for Podcasts''')
x=int(input("what would you like to hear?"))
if x==1:
    print ('''    Enter 1 for Hindi
    Enter 2 for punjabi
    Enter 3 for english''')
    n=int(input("enter the language"))
    print()
    if n==1:
        print('''        Enter 1 for romantic songs
        Enter 2 for rap songs
        Enter 3 for sad songs
        Enter 4 for dance songs
        Enter 5 for lofi songs
        Enter 6 for old songs''')
    elif n==2:
        print('''        Enter 1 for romantic songs
        Enter 2 for rap songs
        Enter 3 for sad songs
        Enter 4 for dance songs''')
    elif n==3:
        print('''        Enter 1 for romantic songs
        Enter 2 for pop songs
        Enter 3 for rap songs
        Enter 4 for slow songs
        Enter 5 for sad songs''')
    else:
        print()
        print("Invalid choice")
    m=int(input("Enter genre"))
    if n==1 and m==1:
        webbrowser.open_new('https://drive.google.com/drive/folders/1AtDg0bYaCbXHQE2TtHIm13j0lS7z45e7?usp=sharing')
    elif n==1 and m==2:
        webbrowser.open_new('https://drive.google.com/drive/folders/1vEn-nWVhGU0kwknEHgadSC1usCcQgBzd?usp=sharing')
    elif n==1 and m==3:
        webbrowser.open_new('https://drive.google.com/drive/folders/1qYRwlnyg58TGKQle2DySlcgOg24NwxYb?usp=sharing')
    elif n==1 and m==4:
        webbrowser.open_new('https://drive.google.com/drive/folders/1vC6hc8Q2BlW_HURPkMeI92rEKakzb3wQ?usp=sharing')
    elif n==1 and m==5:
        webbrowser.open_new('https://drive.google.com/drive/folders/1K8jK6CB78ItngZWE140PStpvdP18WRQx?usp=sharing')
    elif n==1 and m==6:
        webbrowser.open_new('https://drive.google.com/drive/folders/1M-Ixqunk2GtUskSTUvqGsofZbX5-mDoD?usp=sharing')
    elif n==2 and m==1:
        webbrowser.open_new('https://drive.google.com/drive/folders/1s_vk6F2lA8yYnLwTecm7BewK8SyF5EuK?usp=sharing')
    elif n==2 and m==2:
        webbrowser.open_new('https://drive.google.com/drive/folders/1s_vk6F2lA8yYnLwTecm7BewK8SyF5EuK?usp=sharing')
    elif n==2 and m==3:
        webbrowser.open_new('https://drive.google.com/drive/folders/1ICEHDBlr6XHpRhTKb9hoClX9jHjjzmeJ?usp=sharing')
    elif n==2 and m==4:
        webbrowser.open_new('https://drive.google.com/drive/folders/1w_0oHmEUi8hZiC9FV9eB1uS-gkxlrILs?usp=sharing')
    elif n==3 and m==1:
        webbrowser.open_new('https://drive.google.com/drive/folders/1bn01zVFGzpDJe7K9YUd1K3UGPrYwZDJz?usp=sharing')
    elif n==3 and m==2:
        webbrowser.open_new('https://drive.google.com/drive/folders/1rsW36tbPPX_GU1KoZDx-9Y7oPkkRtNcs?usp=sharing')
    elif n==3 and m==3:
        webbrowser.open_new('https://drive.google.com/drive/folders/1RgySOY7fXLwAkI-ZiyvdM3dyGPNLMVqq?usp=sharing')
    elif n==3 and m==4:
        webbrowser.open_new('https://drive.google.com/drive/folders/1tDcmWQYqlGqK8F-Er60v6X_x-sHQnB9J?usp=sharing')
    elif n==3 and m==5:
        webbrowser.open_new('https://drive.google.com/drive/folders/1W7U4Y__Gq74A7bEaGyXSftEYd5OHBpuk?usp=sharing')
    else:
        print()
        print("Invalid choice")
elif x==2:
    print('''     Enter 1 for horror
    Enter 2 for romantic
    Enter 3 for mystery
    Enter 4 for comic''')
    y=(int(input("Enter genre")))
    if y==1:
        webbrowser.open_new('https://drive.google.com/drive/folders/1qpo5b7eRxtnsga-IJmFVSEccqY3bmudL?usp=sharing')
    elif y==2:
        webbrowser.open_new('https://drive.google.com/drive/folders/1Z0wYHI5NcssaxncpN_2lPItN6t3uag8p?usp=sharing')
    elif y==3:
        webbrowser.open_new('https://drive.google.com/drive/folders/1pAbbIg07cqolCofSZ1uXYvTC8aw8UTUo?usp=sharing')
    elif y==4:
        webbrowser.open_new('https://drive.google.com/drive/folders/1if_PxfF2rxN02R3o3J5efFsxBCnYzrwH?usp=sharing')
    else:
        print()
        print("Invalid choice")
elif x==3:
    webbrowser.open_new('https://drive.google.com/drive/folders/1c0vfVDFHgocgTn1WmrrFnIEkfY4WiHZz?usp=share_link')
else:
    print()
    print("Invalid choice")
