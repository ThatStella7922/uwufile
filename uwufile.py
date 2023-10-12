# uwufile.py 1.0
# ThatStella7922 - https://thatstel.la

name = "uwufile.py"
ver = "1.0.1"

# Colors
class colors:
    pink = '\033[38;5;206m'
    end = '\033[0m'
    ok = "\033[96m[*]\033[0m"
    success = "\033[92m[√]\033[0m"
    warn = "\033[93m[!]\033[0m"
    question = "\033[94m[?]\033[0m"
    fail = "\033[91m[x]\033[0m"
## End of colors

print(f"{name} v{ver} - uwuify your files \n{colors.pink}ThatStella7922{colors.end} (https://thatstel.la)")

import sys
import re
import random as rand
from pathlib import Path, PosixPath

## Taken from uwuipy.py from https://github.com/Cuprum77/uwuipy
## This was done so installation via PyPi isn't needed
class uwuipy:
    __uwu_pattern = [
        (r'[rl]', 'w'),
        (r'[RL]', 'W'),
        (r'n([aeiou])', 'ny\\g<1>'),
        (r'N([aeiou])', 'Ny\\g<1>'),
        (r'N([AEIOU])', 'NY\\g<1>'),
        (r'ove', 'uv'),
        (r'pog', 'poggies'),
    ]

    __actions = [
        '***blushes***',
        '***whispers to self***',
        '***cries***',
        '***screams***',
        '***sweats***',
        '***twerks***',
        '***runs away***',
        '***screeches***',
        '***walks away***',
        '***sees bulge***',
        '***looks at you***',
        '***notices buldge***',
        '***starts twerking***',
        '***huggles tightly***',
        '***boops your nose***',
        '***wags my tail***',
        '***pounces on you***',
        '***nuzzles your necky wecky***',
        '***unzips your pants***',
        '***licks lips***',
        '***glomps and huggles***',
        '***glomps***',
        '***looks around suspiciously***',
        '***smirks smuggly***',
        '***pounces on your buldge***',
        '***breaks into your house and aliases neofetch to rm -rf --no-preserve-root /***',
    ]

    __exclamations = [
        '!?',
        '?!!',
        '?!?1',
        '!!11',
        '!!1!',
        '?!?!',
    ]

    __faces = [
        "(・\\`ω\\´・)",
        ";;w;;",
        "OwO",
        "owo",
        "UwU",
        "\\>w\\<",
        "^w^",
        "ÚwÚ",
        "^-^",
        ":3",
        "x3",
        'Uwu',
        'uwU',
        '(uwu)',
        "(ᵘʷᵘ)",
        "(ᵘﻌᵘ)",
        "(◡ ω ◡)",
        "(◡ ꒳ ◡)",
        "(◡ w ◡)",
        "(◡ ሠ ◡)",
        "(˘ω˘)",
        "(⑅˘꒳˘)",
        "(˘ᵕ˘)",
        "(˘ሠ˘)",
        "(˘³˘)",
        "(˘ε˘)",
        "(˘˘˘)",
        "( ᴜ ω ᴜ )",
        "(„ᵕᴗᵕ„)",
        "(ㅅꈍ ˘ ꈍ)",
        "(⑅˘꒳˘)",
        "( ｡ᵘ ᵕ ᵘ ｡)",
        "( ᵘ ꒳ ᵘ ✼)",
        "( ˘ᴗ˘ )",
        "(ᵕᴗ ᵕ⁎)",
        "*:･ﾟ✧(ꈍᴗꈍ)✧･ﾟ:*",
        "*˚*(ꈍ ω ꈍ).₊̣̇.",
        "(。U ω U。)",
        "(U ᵕ U❁)",
        "(U ﹏ U)",
        "(◦ᵕ ˘ ᵕ◦)",
        "ღ(U꒳Uღ)",
        "♥(。U ω U。)",
        "– ̗̀ (ᵕ꒳ᵕ) ̖́-",
        "( ͡U ω ͡U )",
        "( ͡o ᵕ ͡o )",
        "( ͡o ꒳ ͡o )",
        "( ˊ.ᴗˋ )",
        "(ᴜ‿ᴜ✿)",
        "~(˘▾˘~)",
        "(｡ᴜ‿‿ᴜ｡)",
    ]

    def __init__(self, seed: int = None, stutter_chance: float = 0.1, face_chance: float = 0.05,
                 action_chance: float = 0.075, exclamation_chance: float = 1):

        # input protection to make sure the user stays within allowed parameters
        if not 0.0 <= stutter_chance <= 1.0:
            raise ValueError("Invalid input value for stutterChance, supported range is 0-1.0")
        elif not 0.0 <= face_chance <= 1.0:
            raise ValueError("Invalid input value for faceChance, supported range is 0-1.0")
        elif not 0.0 <= action_chance <= 1.0:
            raise ValueError("Invalid input value for actionChance, supported range is 0-1.0")
        elif not 0.0 <= exclamation_chance <= 1.0:
            raise ValueError("Invalid input value for exclamationChance, supported range is 0-1.0")

        rand.seed(seed)
        self._stutter_chance = stutter_chance
        self._face_chance = face_chance
        self._action_chance = action_chance
        self._exclamation_chance = exclamation_chance

    def _uwuify_words(self, _msg):
        # split the message into words
        words = _msg.split(' ')
        
        # iterate over each individual word
        # sure you could regex the entire thing, but then you lose
        # the ability to ignore certain cases, like pings and urls
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            # skip URLs
            if re.search(r'((http:|https:)//[^ \<]*[^ \<\.])', word):
                continue
            # skip pings
            if word[0] == '@' or word[0] == '#' or word[0] == ':' or word[0] == '<':
                continue
            # for each pattern in the array
            for pattern, substitution in self.__uwu_pattern:
                # attempt to use the pattern on the word
                word = re.sub(pattern, substitution, word)
            
            # add the modified word to the original words array
            words[idx] = word

        # return the joined string
        return ' '.join(words)

    def _uwuify_spaces(self, _msg):
        # split the message into words
        words = _msg.split(' ')

        # iterate over each individual word
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            # skip pings
            if word[0] == '@' or word[0] == '#' or word[0] == ':' or word[0] == '<':
                continue
            
            # get the character case for the second letter in the word
            next_char_case = word[1].isupper() if len(word) > 1 else False
            _word = ''
            
            # if we are to add stutters, do it
            if rand.random() <= self._stutter_chance:
                # creates a random number between 1 and 2
                stutter_len = rand.randrange(1, 3)
                # add as many characters to the stutter as stutter_len dictates
                for j in range(stutter_len + 1):
                    _word += (word[0] if j == 0 else (word[0].upper() if next_char_case else word[0].lower())) + "-"
                    
                # add in the whole word, but make sure the case matches the next rest of the word
                _word += (word[0].upper() if next_char_case else word[0].lower()) + word[1:]
                
            # if we are to add a face, do it
            if rand.random() <= self._face_chance:
                _word = (_word or word) + ' ' + self.__faces[rand.randrange(0, len(self.__faces))]
                
            # if we are to add an action, do it
            if rand.random() <= self._action_chance:
                _word = (_word or word) + ' ' + self.__actions[rand.randrange(0, len(self.__actions))]
                
            # replace the word in the array with the modified if it exists, if not add the original word back
            words[idx] = (_word or word)

        return ' '.join(words)
            
    def _uwuify_exclamations(self, _msg):
        # split the message into words
        words = _msg.split(' ')
        
        # iterate over each individual word
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            # skip if an exclamation is not present or the random number is greater than the chance
            if (not re.search(r'[?!]+$', word)) or rand.random() > self._exclamation_chance:
                continue
            
            # strip the exclamation from the word, add new exclamations and return it to the words array
            index = rand.randrange(0, len(self.__exclamations))
            word = re.sub(r'[?!]+$', '', word) + self.__exclamations[index]
            words[idx] = word
        
        # return the joined string
        return ' '.join(words)

    def uwuify(self, msg):
        msg = self._uwuify_words(msg)
        msg = self._uwuify_spaces(msg)
        msg = self._uwuify_exclamations(msg)

        return msg
## End of uwuipy.py

helpStr = """Usage: uwufile.py input_file output_file

    input_file: The source file to uwuify
    output_file: The destination for the uwuified version
    
    Example: uwufile.py input.txt output.txt
    
    Notes: 
    - If the output file already exists, it will be overwritten
    - If the input file is a character device (such as /dev/urandom),
      it wont't be read for safety reasons"""

if len(sys.argv) <= 2:
    print()
    print(f"Help for {name} v{ver}:")
    print(helpStr)
    print()
    sys.exit(0)
elif len(sys.argv) != 3:
    print()
    print(f"Error while processing arguments.\nSee the help below:")
    print()
    print(helpStr)
    print()
    sys.exit(1)

print()

file_path = Path(sys.argv[1])
out_path = Path(sys.argv[2])

try:
    if type(file_path) is PosixPath:
        if file_path.is_char_device():
            raise PermissionError("", f"Reading from {file_path} is disallowed for safety reasons.\n\t(no you cannot read from /dev/urandom fuck off)")
    if file_path.is_dir() == True:
        raise IsADirectoryError("", f"uwufile does not support directories")
    if file_path.is_file() == False:
        raise FileNotFoundError("", f"File is invalid")
    #if file_path == out_path:
        #raise FileExistsError("", "Input and output files cannot be the same.")
    with open(file_path, 'r', encoding="utf-8") as file:
        file_contents = file.read()
    print(f"{colors.ok} Opened input file \"{file_path}\"")
except IsADirectoryError as e:
    print(f"{colors.fail} Error while reading the input directory \"{file_path}\":\n{colors.warn}\t{e.args[1]}")
    print()
    sys.exit(1)
except UnicodeDecodeError as e:
    print(f"{colors.fail} UnicodeDecodeError while reading the input file \"{file_path}\":\n{colors.warn}\t{e.args[4]}\n{colors.question} Have you ensured that the input file contains text?")
    print()
    sys.exit(1)
except Exception as e:
    print(f"{colors.fail} Error while reading the input file \"{file_path}\":\n{colors.warn}\t{e.args[1]}")
    print()
    sys.exit(1)

try:
    uwuObj = uwuipy()
    uwuified_contents = uwuObj.uwuify(file_contents)
    print(f"{colors.success} Uwuified successfully! ({len(uwuified_contents)} characters)")
except Exception as e:
    print(f"{colors.fail} Error while uwuifying:\n{e}")
    print()
    sys.exit(1)

try:
    with open(out_path, 'w', encoding="utf-8") as out_file:
        out_file.write(uwuified_contents)
    print(f"{colors.ok} Wrote output to \"{out_path}\"")
except Exception as e:
    print(f"{colors.fail} Error while writing to output file \"{out_path}\":\n{colors.warn}\t{e.args[1]}")
    print()
    sys.exit(1)

print(f"{colors.success} Uwuifying completed with no errors, exiting with code 0.\n:3")
print()
sys.exit(0)