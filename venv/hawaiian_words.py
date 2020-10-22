legalLetters = ["a", "e", "i", "o", "u", "p", "k", "h", "l", "m", "n", "w", " ", "'"]
vowels = ["a", "e", "i", "o", "u"]
singleVowels = {"a": "ah", "e": "eh", "i": "ee", "o": "oh", "u": "oo"}
const = ["p", "k", "h", "l", "m", "n"]
vowelPairs = {"ai": "eye", "ae": "eye", "ao": "ow", "au": "ow",
              "ei": "ay", "eu": "eh-oo", "iu": "ew", "oi": "oy",
              "ou": "ow", "ui": "ooey"}


def checkString(string):
    string = string.lower()
    for letter in string:
        if letter not in legalLetters:
            print(letter, "is not a valid letter")
            return False
    return True


def translate(string):
    output = []
    string = string.lower()
    words = string.split()
    secondVowel = False
    for word in words:
        wordOutput = ""
        for letterIdx in range(len(word)):
            # skip if second vowel in pair already accounted for
            if secondVowel:
                secondVowel = False
                continue

            # apostrophes and spaces don't need translating
            if word[letterIdx] == "'":
                wordOutput = wordOutput + "'"
                continue
            if word[letterIdx] == " ":
                wordOutput = wordOutput + " "
                continue

            # if it's a constanant and not a w, just add it and continue
            if word[letterIdx] in const:
                wordOutput = wordOutput + word[letterIdx]
                continue

            # if it's a w, check if it's not the first letter and comes after i or e -> v
            # else it's pronounced w
            if word[letterIdx] == "w":
                if letterIdx == 0:
                    wordOutput = wordOutput + "w"
                    continue
                else:
                    if word[letterIdx - 1] == "i" or word[letterIdx - 1] == "e":
                        wordOutput = wordOutput + "v"
                        continue
                    else:
                        wordOutput = wordOutput + "w"
                        continue

            # if we're here, must be a vowel. Need to check if it's a pair.
            try:
                if word[letterIdx + 1] in vowels:
                    couple = "" + word[letterIdx] + word[letterIdx + 1]
                    sound = vowelPairs.get(couple)
                    if sound == None:
                        # if second vowel isn't in a pair, just add vowel and continue normally
                        sound = singleVowels.get(word[letterIdx])
                        wordOutput = wordOutput + sound + "-"
                        continue
                    else:
                        # vowels are paired, therefore add it and skip next letter (second vowel)
                        wordOutput = wordOutput + sound + "-"
                        secondVowel = True
                        continue

                # vowel followed by const
                else:
                    wordOutput = wordOutput + singleVowels.get(word[letterIdx]) + "-"
                    continue

            # exception thrown if vowel is last letter in word
            except IndexError:
                wordOutput = wordOutput + singleVowels.get(word[letterIdx]) + "-"
                continue
        if wordOutput[-1] == "-":
            wordOutput = wordOutput[:-1]
        wordOutput = wordOutput.replace("-'", "'")
        wordOutput = wordOutput.capitalize()
        output.append(wordOutput)
    return output

def main():
    flag1 = True
    yes = ["Y", "YES"]
    no = ["N", "NO"]
    while flag1:
        string = input("Enter a hawaiian word to pronounce: ")
        if checkString(string):
            translatedString = translate(string)
            print(string.upper(), "is pronounched", *translatedString)

        else:
            continue
        while True:
            cont = input("Do you want to enter another word? Y/Yes/N/No: ")
            if cont.upper() in yes:
                break
            elif cont.upper() in no:
                flag1 = False
                break
            else:
                print("Enter Y, YES, N or NO")

if __name__ == '__main__':
    main()