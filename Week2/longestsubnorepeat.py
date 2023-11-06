def lengthoflongestsubstring(s):
    currentLongest = ""
    currentCheck = ""
    index_last_app = 0

    for letter in s:

        print("current longest: " + currentLongest)
        print("current letter is: ", letter)
        if letter in currentCheck:
            
            #check to see if longer than max
            if len(currentCheck) > len(currentLongest):
                currentLongest = currentCheck
                for new_letter in range(len(currentLongest)):
                    if currentCheck[new_letter] == letter:
                        if new_letter > index_last_app:
                            index_last_app = new_letter
                currentCheck = currentCheck[index_last_app::]
            else:
                currentCheck = ""
        else:
            print(currentCheck)
            currentCheck += letter
            print(currentCheck)
    if len(currentCheck) > len(currentLongest):
        currentLongest = currentCheck
    return len(currentLongest)


print(lengthoflongestsubstring("aabaab!bb"))
