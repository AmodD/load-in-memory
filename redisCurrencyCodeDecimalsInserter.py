def redisInserter(redisClient):

    currencyCodes = {'784': 2, '971': 2, '008': 2, '051': 2, '532': 2, '973': 2, '032': 2, '036': 2, '533': 2, '944': 2,
                     '977': 2, '052': 2, '050': 2, '975': 2, '048': 3, '108': 0, '060': 2,
                     '096': 2, '068': 2, '984': 2, '986': 2, '044': 2, '064': 2, '072': 2, '933': 2, '084': 2, '124': 2,
                     '976': 2, '947': 2, '756': 2, '948': 2, '990': 4, '152': 0, '156': 2,
                     '170': 2, '970': 2, '188': 2, '931': 2, '192': 2, '132': 2, '203': 2, '262': 0, '208': 2, '214': 2,
                     '012': 2, '818': 2, '232': 2, '230': 2, '978': 2, '242': 2, '238': 2,
                     '826': 2, '981': 2, '936': 2, '292': 2, '270': 2, '324': 0, '320': 2, '328': 2, '344': 2, '340': 2,
                     '191': 2, '332': 2, '348': 2, '360': 2, '376': 2, '356': 2, '368': 3,
                     '364': 2, '352': 0, '388': 2, '400': 3, '392': 0, '404': 2, '417': 2, '116': 2, '174': 0, '408': 2,
                     '410': 0, '414': 3, '136': 2, '398': 2, '418': 2, '422': 2, '144': 2,
                     '430': 2, '426': 2, '434': 3, '504': 2, '498': 2, '969': 2, '807': 2, '104': 2, '496': 2, '446': 2,
                     '929': 2, '480': 2, '462': 2, '454': 2, '484': 2, '979': 2, '458': 2,
                     '943': 2, '516': 2, '566': 2, '558': 2, '578': 2, '524': 2, '554': 2, '512': 3, '590': 2, '604': 2,
                     '598': 2, '608': 2, '586': 2, '985': 2, '600': 0, '634': 2, '946': 2,
                     '941': 2, '643': 2, '646': 0, '682': 2, '900': 2, '690': 2, '938': 2, '752': 2, '702': 2, '654': 2,
                     '694': 2, '706': 2, '968': 2, '728': 2, '930': 2, '222': 2, '760': 2,
                     '748': 2, '764': 2, '972': 2, '934': 2, '788': 3, '776': 2, '949': 2, '780': 2, '901': 2, '834': 2,
                     '980': 2, '800': 0, '840': 2, '997': 2, '940': 0, '858': 2, '927': 4,
                     '860': 2, '928': 2, '704': 0, '548': 0, '882': 2, '950': 0, '951': 2, '952': 0, '953': 0, '886': 2,
                     '710': 2, '967': 2, '932': 2}



    redisClient.hmset('currencyCodeMapping', currencyCodes)
    # print(redisClient.hgetall('currencyCodeMapping'))
    print("Currency codes and number of decimal places loaded in memory")
