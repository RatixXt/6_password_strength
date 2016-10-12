# -*- coding: utf-8 -*-
from re import search, match, fullmatch
from os.path import exists

default_pswd_list = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111',
                     '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey',
                     'letmein', '696969', 'shadow', 'master', '666666', 'qwertyuiop', '123321',
                     'mustang', '1234567890', 'michael', '654321', 'pussy', 'superman', '1qaz2wsx',
                     '7777777', 'fuckyou', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1',
                     'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley',
                     'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', 'fuckme', '2000', 'charlie',
                     'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233',
                     'george', 'asshole', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn',
                     '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'fuck', 'maggie',
                     '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer',
                     'love', 'ashley', '6969', 'nicole', 'chelsea', 'biteme', 'matthew', 'access',
                     'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix',
                     'william', 'corvette', 'hello', 'martin', 'heather', 'secret', 'fucker', 'merlin',
                     'diamond', '1234qwer', 'gfhjkm', 'hammer', 'silver', '222222', '88888888',
                     'anthony', 'justin', 'test', 'bailey', 'q1w2e3r4t5', 'patrick', 'internet',
                     'scooter', 'orange', '11111', 'golfer', 'cookie', 'richard', 'samantha', 'bigdog',
                     'guitar', 'jackson', 'whatever', 'mickey', 'chicken', 'sparky', 'snoopy',
                     'maverick', 'phoenix', 'camaro', 'sexy', 'peanut', 'morgan', 'welcome', 'falcon',
                     'cowboy', 'ferrari', 'samsung', 'andrea', 'smokey', 'steelers', 'joseph',
                     'mercedes', 'dakota', 'arsenal', 'eagles', 'melissa', 'boomer', 'booboo', 'spider',
                     'nascar', 'monster', 'tigers', 'yellow', 'xxxxxx', '123123123', 'gateway',
                     'marina', 'diablo', 'bulldog', 'qwer1234', 'compaq', 'purple', 'hardcore',
                     'banana', 'junior', 'hannah', '123654', 'porsche', 'lakers', 'iceman', 'money',
                     'cowboys', '987654', 'london', 'tennis', '999999', 'ncc1701', 'coffee', 'scooby',
                     '0000', 'miller', 'boston', 'q1w2e3r4', 'fuckoff', 'brandon', 'yamaha', 'chester',
                     'mother', 'forever', 'johnny', 'edward', '333333', 'oliver', 'redsox', 'player',
                     'nikita', 'knight', 'fender', 'barney', 'midnight', 'please', 'brandy', 'chicago',
                     'badboy', 'iwantu', 'slayer', 'rangers', 'charles', 'angel', 'flower', 'bigdaddy',
                     'rabbit', 'wizard', 'bigdick', 'jasper', 'enter', 'rachel', 'chris', 'steven',
                     'winner', 'adidas', 'victoria', 'natasha', '1q2w3e4r', 'jasmine', 'winter',
                     'prince', 'panties', 'marine', 'ghbdtn', 'fishing', 'cocacola', 'casper', 'james',
                     '232323', 'raiders', '888888', 'marlboro', 'gandalf', 'asdfasdf', 'crystal',
                     '87654321', '12344321', 'sexsex', 'golden', 'blowme', 'bigtits', '8675309',
                     'panther', 'lauren', 'angela', 'bitch', 'spanky', 'thx1138', 'angels', 'madison',
                     'winston', 'shannon', 'mike', 'toyota', 'blowjob', 'jordan23', 'canada', 'sophie',
                     'Password', 'apples', 'dick', 'tiger', 'razz', '123abc', 'pokemon', 'qazxsw',
                     '55555', 'qwaszx', 'muffin', 'johnson', 'murphy', 'cooper', 'jonathan', 'liverpoo',
                     'david', 'danielle', '159357', 'jackie', '1990', '123456a', '789456', 'turtle',
                     'horny', 'abcd1234', 'scorpion', 'qazwsxedc', '101010', 'butter', 'carlos',
                     'password1', 'dennis', 'slipknot', 'qwerty123', 'booger', 'asdf', '1991', 'black',
                     'startrek', '12341234', 'cameron', 'newyork', 'rainbow', 'nathan', 'john', '1992',
                     'rocket', 'viking', 'redskins', 'butthead', 'asdfghjkl', '1212', 'sierra',
                     'peaches', 'gemini', 'doctor', 'wilson', 'sandra', 'helpme', 'qwertyui', 'victor',
                     'florida', 'dolphin', 'pookie', 'captain', 'tucker', 'blue', 'liverpool', 'theman',
                     'bandit', 'dolphins', 'maddog', 'packers', 'jaguar', 'lovers', 'nicholas',
                     'united', 'tiffany', 'maxwell', 'zzzzzz', 'nirvana', 'jeremy', 'suckit', 'stupid',
                     'porn', 'monica', 'elephant', 'giants', 'jackass', 'hotdog', 'rosebud', 'success',
                     'debbie', 'mountain', '444444', 'xxxxxxxx', 'warrior', '1q2w3e4r5t', 'q1w2e3',
                     '123456q', 'albert', 'metallic', 'lucky', 'azerty', '7777', 'shithead', 'alex',
                     'bond007', 'alexis', '1111111', 'samson', '5150', 'willie', 'scorpio', 'bonnie',
                     'gators', 'benjamin', 'voodoo', 'driver', 'dexter', '2112', 'jason', 'calvin',
                     'freddy', '212121', 'creative', '12345a', 'sydney', 'rush2112', '1989', 'asdfghjk',
                     'red123', 'bubba', '4815162342', 'passw0rd', 'trouble', 'gunner', 'happy',
                     'fucking', 'gordon', 'legend', 'jessie', 'stella', 'qwert', 'eminem', 'arthur',
                     'apple', 'nissan', 'bullshit', 'bear', 'america', '1qazxsw2', 'nothing', 'parker',
                     '4444', 'rebecca', 'qweqwe', 'garfield', '01012011', 'beavis', '69696969', 'jack',
                     'asdasd', 'december', '2222', '102030', '252525', '11223344', 'magic', 'apollo',
                     'skippy', '315475', 'girls', 'kitten', 'golf', 'copper', 'braves', 'shelby',
                     'godzilla', 'beaver', 'fred', 'tomcat', 'august', 'buddy', 'airborne', '1993',
                     '1988', 'lifehack', 'qqqqqq', 'brooklyn', 'animal', 'platinum', 'phantom',
                     'online', 'xavier', 'darkness', 'blink182', 'power', 'fish', 'green', '789456123',
                     'voyager', 'police', 'travis', '12qwaszx', 'heaven', 'snowball', 'lover',
                     'abcdef', '00000', 'pakistan', '007007', 'walter', 'playboy', 'blazer', 'cricket',
                     'sniper', 'hooters', 'donkey', 'willow', 'loveme', 'saturn', 'therock', 'redwings',
                     'bigboy\n', 'pumpkin\n', 'trinity\n', 'williams\n', 'tits\n', 'nintendo\n', 'digital\n',
                     'destiny\n', 'topgun\n', 'runner\n', 'marvin\n', 'guinness\n', 'chance\n', 'bubbles\n',
                     'testing\n', 'fire\n', 'november\n', 'minecraft\n', 'asdf1234\n', 'lasvegas\n', 'sergey\n',
                     'broncos\n', 'cartman\n', 'private\n', 'celtic\n', 'birdie\n', 'little\n', 'cassie\n',
                     'babygirl\n', 'donald\n', 'beatles\n', '1313\n', 'dickhead\n', 'family\n', '12121212\n',
                     'school\n', 'louise\n', 'gabriel\n', 'eclipse\n', 'fluffy\n', '147258369\n', 'lol123\n',
                     'explorer\n', 'beer\n', 'nelson\n', 'flyers\n', 'spencer\n', 'scott\n', 'lovely\n', 'gibson\n',
                     'doggie\n', 'cherry\n', 'andrey\n', 'snickers\n', 'buffalo\n', 'pantera\n', 'metallica\n',
                     'member\n', 'carter\n', 'qwertyu\n', 'peter\n', 'alexande\n', 'steve\n', 'bronco\n', 'paradise\n',
                     'goober\n', '5555\n', 'samuel\n', 'montana\n', 'mexico\n', 'dreams\n', 'michigan\n', 'cock\n',
                     'carolina\n', 'yankee\n', 'friends\n', 'magnum\n', 'surfer\n', 'poopoo\n', 'maximus\n', 'genius\n',
                     'cool\n', 'vampire\n', 'lacrosse\n', 'asd123\n', 'aaaa\n', 'christin\n', 'kimberly\n', 'speedy\n',
                     'sharon\n', 'carmen\n', '111222\n', 'kristina\n', 'sammy\n', 'racing\n', 'ou812\n', 'sabrina\n',
                     'horses\n', '0987654321\n', 'qwerty1\n', 'pimpin\n', 'baby\n', 'stalker\n', 'enigma\n', '147147\n',
                     'star\n', 'poohbear\n', 'boobies\n', '147258\n', 'simple\n', 'bollocks\n', '12345q\n', 'marcus\n',
                     'brian\n', '1987\n', 'qweasdzxc\n', 'drowssap\n', 'hahaha\n', 'caroline\n', 'barbara\n', 'dave\n',
                     'viper\n', 'drummer\n', 'action\n', 'einstein\n', 'bitches\n', 'genesis\n', 'hello1\n', 'scotty\n',
                     'friend\n', 'forest\n', '010203\n', 'hotrod\n', 'google\n', 'vanessa\n', 'spitfire\n', 'badger\n',
                     'maryjane\n', 'friday\n', 'alaska\n', '1232323q\n', 'tester\n', 'jester\n', 'jake\n', 'champion\n',
                     'billy\n', '147852\n', 'rock\n', 'hawaii\n', 'badass\n', 'chevy\n', '420420\n', 'walker\n',
                     'stephen\n', 'eagle1\n', 'bill\n', '1986\n', 'october\n', 'gregory\n', 'svetlana\n', 'pamela\n',
                     '1984\n', 'music\n', 'shorty\n', 'westside\n', 'stanley\n', 'diesel\n', 'courtney\n', '242424\n',
                     'kevin\n', 'porno\n', 'hitman\n', 'boobs\n', 'mark\n', '12345qwert\n', 'reddog\n', 'frank\n',
                     'qwe123\n', 'popcorn\n', 'patricia\n', 'aaaaaaaa\n', '1969\n', 'teresa\n', 'mozart\n', 'buddha\n',
                     'anderson\n', 'paul\n', 'melanie\n', 'abcdefg\n', 'security\n', 'lucky1\n', 'lizard\n', 'denise\n',
                     '3333\n', 'a12345\n', '123789\n', 'ruslan\n', 'stargate\n', 'simpsons\n', 'scarface\n', 'eagle\n',
                     '123456789a\n', 'thumper\n', 'olivia\n', 'naruto\n', '1234554321\n', 'general\n', 'cherokee\n',
                     'a123456\n', 'vincent\n', 'Usuckballz1\n', 'spooky\n', 'qweasd\n', 'cumshot\n', 'free\n',
                     'frankie\n', 'douglas\n', 'death\n', '1980\n', 'loveyou\n', 'kitty\n', 'kelly\n', 'veronica\n',
                     'suzuki\n', 'semperfi\n', 'penguin\n', 'mercury\n', 'liberty\n', 'spirit\n', 'scotland\n',
                     'natalie\n', 'marley\n', 'vikings\n', 'system\n', 'sucker\n', 'king\n', 'allison\n', 'marshall\n',
                     '1979\n', '098765\n', 'qwerty12\n', 'hummer\n', 'adrian\n', '1985\n', 'vfhbyf\n', 'sandman\n',
                     'rocky\n', 'leslie\n', 'antonio\n', '98765432\n', '4321\n', 'softball\n', 'passion\n', 'mnbvcxz\n',
                     'bastard\n', 'passport\n', 'horney\n', 'rascal\n', 'howard\n', 'franklin\n', 'bigred\n',
                     'assman\n', 'alexander\n', 'homer\n', 'redrum\n', 'jupiter\n', 'claudia\n', '55555555\n',
                     '141414\n', 'zaq12wsx\n', 'shit\n', 'patches\n', 'nigger\n', 'cunt\n', 'raider\n', 'infinity\n',
                     'andre\n', '54321\n', 'galore\n', 'college\n', 'russia\n', 'kawasaki\n', 'bishop\n', '77777777\n',
                     'vladimir\n', 'money1\n', 'freeuser\n', 'wildcats\n', 'francis\n', 'disney\n', 'budlight\n',
                     'brittany\n', '1994\n', '00000000\n', 'sweet\n', 'oksana\n', 'honda\n', 'domino\n', 'bulldogs\n',
                     'brutus\n', 'swordfis\n', 'norman\n', 'monday\n', 'jimmy\n', 'ironman\n', 'ford\n', 'fantasy\n',
                     '9999\n', '7654321\n', 'PASSWORD\n', 'hentai\n', 'duncan\n', 'cougar\n', '1977\n', 'jeffrey\n',
                     'house\n', 'dancer\n', 'brooke\n', 'timothy\n', 'super\n', 'marines\n', 'justice\n', 'digger\n',
                     'connor\n', 'patriots\n', 'karina\n', '202020\n', 'molly\n', 'everton\n', 'tinker\n', 'alicia\n',
                     'rasdzv3\n', 'poop\n', 'pearljam\n', 'stinky\n', 'naughty\n', 'colorado\n', '123123a\n', 'water\n',
                     'test123\n', 'ncc1701d\n', 'motorola\n', 'ireland\n', 'asdfg\n', 'slut\n', 'matt\n', 'houston\n',
                     'boogie\n', 'zombie\n', 'accord\n', 'vision\n', 'bradley\n', 'reggie\n', 'kermit\n', 'froggy\n',
                     'ducati\n', 'avalon\n', '6666\n', '9379992\n', 'sarah\n', 'saints\n', 'logitech\n', 'chopper\n',
                     '852456\n', 'simpson\n', 'madonna\n', 'juventus\n', 'claire\n', '159951\n', 'zachary\n',
                     'yfnfif\n', 'wolverin\n', 'warcraft\n', 'hello123\n', 'extreme\n', 'penis\n', 'peekaboo\n',
                     'fireman\n', 'eugene\n', 'brenda\n', '123654789\n', 'russell\n', 'panthers\n', 'georgia\n',
                     'smith\n', 'skyline\n', 'jesus\n', 'elizabet\n', 'spiderma\n', 'smooth\n', 'pirate\n', 'empire\n',
                     'bullet\n', '8888\n', 'virginia\n', 'valentin\n', 'psycho\n', 'predator\n', 'arizona\n',
                     '134679\n', 'mitchell\n', 'alyssa\n', 'vegeta\n', 'titanic\n', 'christ\n', 'goblue\n', 'fylhtq\n',
                     'wolf\n', 'mmmmmm\n', 'kirill\n', 'indian\n', 'hiphop\n', 'baxter\n', 'awesome\n', 'people\n',
                     'danger\n', 'roland\n', 'mookie\n', '741852963\n', '1111111111\n', 'dreamer\n', 'bambam\n',
                     'arnold\n', '1981\n', 'skipper\n', 'serega\n', 'rolltide\n', 'elvis\n', 'changeme\n', 'simon\n',
                     '1q2w3e\n', 'lovelove\n', 'fktrcfylh\n', 'denver\n', 'tommy\n', 'mine\n', 'loverboy\n', 'hobbes\n',
                     'happy1\n', 'alison\n', 'nemesis\n', 'chevelle\n', 'cardinal\n', 'burton\n', 'wanker\n',
                     'picard\n', '151515\n', 'tweety\n', 'michael1\n', '147852369\n', '12312\n', 'xxxx\n', 'windows\n',
                     'turkey\n', '456789\n', '1974\n', 'vfrcbv\n', 'sublime\n', '1975\n', 'galina\n', 'bobby\n',
                     'newport\n', 'manutd\n', 'daddy\n', 'american\n', 'alexandr\n', '1966\n', 'victory\n',
                     'rooster\n', 'qqq111\n', 'madmax\n', 'electric\n', 'bigcock\n', 'a1b2c3\n', 'wolfpack\n',
                     'spring\n', 'phpbb\n', 'lalala\n', 'suckme\n', 'spiderman\n', 'eric\n', 'darkside\n',
                     'classic\n', 'raptor\n', '123456789q\n', 'hendrix\n', '1982\n', 'wombat\n', 'avatar\n', 'alpha\n',
                     'zxc123\n', 'crazy\n', 'hard\n', 'england\n', 'brazil\n', '1978\n', '01011980\n',
                     'wildcat\n', 'polina\n', 'freepass']



def check_pswd_digits(password):
    if not search('\d', password) is None:
        if not search('\d{2,}', password) is None:
            return 2
        return 1
    return 0


def check_pswd_various_cases(password):
    if not search('([a-z].*[A-Z])|([A-Z].*[a-z])', password) is None:
        if not search('(([a-z].*[A-Z])|([A-Z].*[a-z])){2}', password) is None:
            return 2
        return 1
    return 0


def check_special_symbols(password):
    if not search(r'\W', password) is None:

        if not search(r'\W{2}', password) is None:
            return 2
        return 1
    return 0


def check_pswd_is_digit(password):
    if password.isdigit():
        return True


def check_pswd_too_small_length(password):
    if len(password) < 5:
        return True


def check_pswd_big_length(password):
    if len(password) > 10:
        return True


def check_pswd_standard_length(password):
    if len(password) > 4:
        if len(password) > 6:
            return 2
        return 1
    return 0


def get_password_strength(password):
    pswd_strength = 1
    if check_pswd_is_digit(password) or check_pswd_too_small_length(password):
        return 1
    if check_pswd_big_length(password):
        return 10
    pswd_strength += check_pswd_standard_length(password)
    pswd_strength += check_pswd_digits(password)
    pswd_strength += check_special_symbols(password)
    pswd_strength += check_pswd_various_cases(password)
    return pswd_strength


def compare_with_common_passwords_dictionary(password, pswd_list):
    for bad_password in pswd_list:
        if fullmatch(bad_password.rstrip('\n'), password):
            return 1
        if match(bad_password.rstrip('\n'), password):
            return get_password_strength(password.strip(bad_password))
    return get_password_strength(password)


def load_password_dict(filepath):
    if exists(filepath):
        with open(filepath, 'r') as file_handler:
            return file_handler.readlines()


def choose_dictionary_with_common_passwords():
    filepath = input(u'Введите путь к файлу с паролями или нажмите Enter, чтобы воспользоваться встроенным словарем:')
    pswd_list = load_password_dict(filepath)
    if pswd_list is None:
        if filepath:
            print(u'Данных нет или указан неверный путь к файлу, будет использован встроенный словарь')
        pswd_list = default_pswd_list
    return pswd_list

if __name__ == '__main__':
    password = input(u"Введите свой пароль:")
    print(u"Защищенность вашего пароля %i из 10" %
          compare_with_common_passwords_dictionary(password, choose_dictionary_with_common_passwords()))
