def vowel(str):
    vowel = "aeiouAEIOU"
    
    if str.isalpha():
            if str in vowel:
                print("vowel")
            else:
                print("Is not a vowel")
    else:
         print("Is not a letter")
vowel("a")
vowel("m")
vowel("i")
vowel("k")
vowel("o")
vowel("n")
