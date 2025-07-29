def green_glass(word):
    can_pass = False
    for index in range(0,len(word)-1):
        if word[index].lower() == word[index+1].lower():
            can_pass = True
        if can_pass:
            print("Yup, this could pass the Green Glass Door")
        else:
            print("Nope, this can't pass the door, try again!")

green_glass("google")
green_glass("dog")
green_glass("ball")
green_glass("llama")
        