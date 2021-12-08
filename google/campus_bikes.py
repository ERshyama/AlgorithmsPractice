# Author: Shyama Arunachalam
# Date created: 1/17/2021

import time


def assignBikes(workers, bikes):
    info = []
    for worker_no, worker in enumerate(workers):
        for bike_no, bike in enumerate(bikes):
            dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
            info.append((dist, worker_no, bike_no))
    info = sorted(info)
    assignments = {}
    bikes_taken = set()
    for _, worker, bike in info:
        if worker not in assignments and bike not in bikes_taken:
            assignments[worker] = bike
            bikes_taken.add(bike)
    answer = []
    for worker in range(len(workers)):
        answer.append(assignments[worker])
    return answer


workers = [[88, 982], [750, 37], [200, 33], [38, 840], [872, 452], [64, 673], [215, 559], [643, 913], [344, 669],
           [517, 621], [937, 582], [718, 136], [77, 358], [859, 447], [906, 740], [628, 235], [548, 892], [998, 843],
           [344, 62], [65, 319], [722, 989], [466, 214], [23, 664], [755, 681], [603, 852], [159, 261], [29, 152],
           [30, 277], [630, 231], [359, 494], [518, 346], [905, 258], [991, 540], [32, 166], [232, 660], [719, 907],
           [331, 54], [152, 16], [375, 594], [205, 38], [766, 924], [395, 867], [976, 330], [570, 944], [615, 721],
           [246, 707], [753, 409], [481, 430], [890, 92], [503, 142], [375, 35], [920, 548], [851, 353], [657, 512],
           [486, 814], [99, 697], [265, 237], [395, 510], [499, 486], [896, 864], [487, 509], [569, 85], [628, 633],
           [868, 519], [59, 94], [288, 443], [21, 595], [636, 963], [619, 845], [85, 796], [52, 450], [228, 201],
           [202, 983], [758, 678], [37, 35], [730, 117], [470, 945], [503, 293], [565, 346], [435, 238], [700, 9],
           [677, 734], [290, 125], [588, 231], [650, 930], [821, 702], [337, 144], [65, 134], [171, 435], [156, 787],
           [454, 25], [536, 648], [221, 911], [416, 721], [582, 605], [877, 649], [581, 669], [500, 878], [47, 392],
           [62, 288], [504, 305], [399, 117], [421, 887], [160, 920], [307, 887], [438, 622], [14, 792], [416, 575],
           [594, 62], [252, 299], [22, 32], [330, 186], [868, 690], [416, 803], [467, 84], [268, 350], [877, 872],
           [29, 986], [433, 216], [971, 208], [858, 725], [418, 853], [830, 769], [804, 884], [343, 7], [820, 170],
           [894, 517], [739, 328], [379, 297], [406, 621], [694, 385], [670, 738], [314, 649], [727, 308], [700, 993],
           [697, 557], [752, 293], [394, 346], [77, 819], [179, 878], [356, 848], [830, 630], [132, 284], [439, 292],
           [481, 169], [160, 637], [433, 280], [698, 154], [406, 44], [227, 747], [150, 716], [779, 191], [470, 677],
           [846, 181], [955, 694], [597, 406], [823, 491], [460, 608], [410, 19], [870, 597], [870, 666], [316, 458],
           [858, 359], [882, 392], [793, 775], [979, 855], [560, 56], [383, 662], [427, 31], [828, 820], [976, 475],
           [314, 378], [154, 15], [718, 535], [39, 108], [232, 555], [27, 44], [269, 700], [267, 705], [453, 852],
           [323, 556], [702, 400], [329, 262], [255, 851], [375, 890], [350, 649], [493, 409], [411, 20], [308, 965],
           [50, 899], [564, 38], [525, 198], [567, 720], [728, 203], [716, 707], [35, 644], [157, 802], [764, 15],
           [25, 68], [210, 445], [986, 622], [875, 995], [600, 744], [743, 668], [773, 939], [74, 204], [471, 561],
           [166, 134], [402, 325], [911, 640], [675, 734], [661, 122], [429, 529], [501, 683], [528, 532], [289, 116],
           [301, 364], [179, 258], [227, 432], [918, 480], [790, 363], [725, 387], [122, 430], [674, 636], [172, 51],
           [545, 418], [242, 747], [490, 533], [758, 162], [890, 116], [527, 61], [90, 752], [295, 163], [367, 823],
           [222, 153], [120, 450], [381, 28], [852, 687], [876, 36], [817, 807], [662, 555], [446, 337], [784, 385],
           [370, 437], [573, 275], [458, 266], [932, 944], [543, 458], [840, 155], [205, 152], [607, 700], [302, 65],
           [964, 871], [205, 136], [422, 891], [580, 343], [534, 523], [182, 157], [133, 737], [357, 395], [284, 214],
           [853, 798], [305, 916], [727, 576], [529, 220], [23, 503], [496, 304], [655, 101], [507, 794], [66, 94],
           [551, 91], [57, 653], [791, 845], [586, 351], [609, 657], [236, 270], [881, 930], [156, 951], [806, 104],
           [58, 717], [544, 135], [717, 212], [736, 381], [899, 630], [448, 815], [122, 754], [462, 796], [970, 760],
           [262, 513], [329, 414], [941, 107], [845, 974], [295, 56], [725, 85], [985, 415], [601, 94], [535, 819],
           [933, 973], [624, 532], [578, 909], [973, 805], [701, 418], [86, 119], [983, 360], [948, 965], [931, 90],
           [368, 422], [586, 675], [851, 127], [98, 497], [612, 774], [411, 572], [477, 72], [969, 580], [214, 123],
           [661, 225], [65, 973], [348, 832], [604, 227], [270, 517], [82, 739], [688, 75], [354, 315], [507, 926],
           [175, 455], [218, 681], [70, 951], [608, 224], [83, 878], [168, 752], [292, 396], [547, 466], [364, 413],
           [566, 124], [162, 912], [737, 247], [383, 946], [97, 210], [428, 552], [230, 237], [769, 736], [518, 135],
           [855, 809], [48, 9], [968, 837], [826, 137], [545, 382], [116, 432], [391, 815], [947, 732], [839, 655],
           [111, 15], [828, 474], [565, 206], [548, 927], [853, 402], [652, 2], [213, 547], [632, 44], [260, 992],
           [347, 198], [504, 280], [869, 98], [313, 996], [672, 90], [299, 378], [963, 519], [960, 748], [679, 515],
           [60, 375], [820, 607], [143, 165], [77, 782], [774, 835], [431, 768], [507, 379], [287, 920], [688, 859],
           [569, 919], [688, 677], [81, 951], [287, 53], [374, 848], [292, 462], [146, 750], [278, 285], [828, 144],
           [180, 100], [445, 83], [972, 441], [150, 918], [917, 492], [97, 76], [692, 525], [180, 453], [699, 227],
           [514, 916], [933, 238], [921, 578], [524, 686], [188, 370], [164, 225], [786, 459], [117, 785], [389, 305],
           [788, 276], [925, 293], [274, 242], [339, 648], [908, 187], [742, 828], [697, 670], [241, 19], [192, 35],
           [51, 534], [903, 738], [365, 951], [205, 978], [528, 799], [249, 555], [884, 33], [96, 556], [578, 21],
           [891, 638], [180, 726], [542, 198], [111, 356], [411, 359], [664, 347], [813, 374], [796, 746], [933, 772],
           [246, 725], [97, 368], [637, 812], [512, 274], [131, 122], [887, 321], [679, 446], [783, 454], [564, 781],
           [564, 767], [296, 542], [543, 901], [702, 21], [973, 630], [868, 408], [367, 260], [678, 277], [0, 387],
           [1, 290], [354, 39], [776, 924], [465, 436], [139, 489], [870, 452], [611, 965], [725, 237], [80, 169],
           [599, 904], [795, 703], [241, 291], [524, 976], [540, 640], [53, 894], [867, 364], [748, 162], [847, 961],
           [669, 215], [814, 108], [598, 429], [784, 87], [994, 535], [361, 232], [247, 13], [922, 305], [799, 379],
           [736, 206], [411, 264], [547, 410], [331, 80], [249, 338], [703, 851], [312, 872], [865, 43], [151, 281],
           [73, 154], [158, 848], [952, 66], [129, 249], [725, 595], [649, 878], [139, 232], [995, 422], [425, 26],
           [143, 841], [41, 908], [18, 461], [497, 893], [980, 228], [453, 41], [803, 124], [323, 344], [759, 741],
           [477, 62], [699, 23], [971, 73], [539, 585], [886, 927], [168, 259], [926, 493], [21, 765], [197, 32],
           [782, 981], [42, 496], [476, 358], [959, 376], [666, 955], [700, 352], [115, 608], [785, 203], [746, 402],
           [976, 857], [79, 513], [552, 30], [377, 301], [835, 905], [87, 863], [777, 310], [78, 203], [427, 789],
           [614, 836], [449, 224], [181, 224], [116, 273], [50, 656], [885, 122], [531, 498], [684, 899], [600, 903],
           [602, 23], [933, 861], [303, 479], [492, 389], [869, 589], [649, 230], [234, 107], [364, 865], [18, 234],
           [794, 75], [507, 75], [605, 526], [232, 642], [303, 623], [359, 245], [987, 642], [427, 321], [52, 170],
           [554, 334], [948, 633], [351, 422], [359, 830], [961, 514], [653, 210], [963, 797], [699, 626], [746, 302],
           [530, 384], [210, 795], [327, 954], [250, 729], [754, 801], [851, 461], [607, 484], [444, 950], [416, 906],
           [865, 48], [392, 923], [816, 354], [809, 32], [178, 617], [599, 39], [104, 83], [996, 744], [804, 653],
           [170, 738], [579, 334], [892, 591], [90, 921], [237, 91], [990, 487], [278, 9], [530, 667], [237, 406],
           [53, 380], [505, 380], [305, 614], [15, 465], [469, 129], [888, 269], [28, 696], [256, 815], [324, 516],
           [337, 825], [872, 79], [934, 832], [95, 705], [368, 581], [178, 415], [429, 702], [178, 198], [468, 917],
           [695, 620], [522, 872], [770, 744], [207, 968], [780, 821], [818, 58], [589, 963], [737, 273], [718, 510],
           [130, 201], [567, 397], [469, 134], [466, 740], [248, 579], [582, 619], [42, 155], [653, 388], [352, 124],
           [726, 377], [298, 279], [491, 707], [671, 250], [268, 852], [101, 910], [875, 951], [130, 608], [870, 250],
           [126, 164], [166, 742], [401, 128], [675, 567], [105, 5], [249, 958], [273, 226], [480, 764], [738, 659],
           [639, 895], [779, 630], [204, 808], [111, 248], [237, 517], [69, 561], [530, 599], [95, 611], [768, 757],
           [35, 663], [231, 672], [805, 423], [909, 549], [115, 573], [42, 670], [528, 731], [698, 793], [329, 177],
           [942, 207], [963, 443], [59, 958], [867, 64], [681, 560], [260, 908], [45, 34], [325, 606], [399, 534],
           [224, 459], [797, 705], [397, 785], [934, 877], [692, 93], [304, 256], [663, 94], [123, 412], [190, 783],
           [68, 941], [800, 449], [267, 790], [977, 318], [877, 476], [510, 527], [178, 257], [579, 192], [936, 339],
           [773, 527], [30, 194], [993, 176], [714, 629], [323, 603], [844, 478], [664, 661], [825, 273], [364, 939],
           [360, 273], [220, 866], [568, 436], [494, 642], [24, 490], [908, 966], [990, 241], [717, 109], [201, 444],
           [292, 444], [167, 999], [375, 546], [24, 749], [985, 875], [472, 867], [248, 606], [425, 58], [24, 55],
           [175, 8], [454, 869], [410, 903], [453, 549], [399, 581], [749, 237], [768, 451], [591, 770], [343, 423],
           [314, 883], [615, 817], [489, 419], [35, 593], [379, 379], [85, 72], [554, 309], [529, 930], [916, 578],
           [215, 355], [645, 229], [572, 726], [771, 926], [273, 79], [233, 817], [411, 579], [436, 28], [809, 403],
           [481, 980], [650, 701], [749, 272], [660, 483], [771, 253], [654, 705], [626, 888], [695, 779], [245, 583],
           [516, 317], [753, 513], [286, 489], [626, 673], [818, 229], [902, 479], [119, 354], [240, 687], [19, 302],
           [967, 487], [727, 867], [668, 525], [958, 382], [488, 504], [554, 168], [955, 698], [175, 329], [38, 260],
           [574, 104], [682, 50], [284, 212], [943, 19], [296, 398], [366, 482], [104, 964], [47, 200], [964, 208],
           [428, 911], [562, 655], [796, 384], [1, 755], [681, 838], [574, 506], [338, 193], [306, 220], [802, 197],
           [985, 192], [407, 704], [876, 472], [444, 375], [880, 568], [783, 249], [541, 923], [636, 282], [353, 814],
           [488, 530], [578, 723], [62, 332], [463, 712], [454, 439], [400, 165], [937, 680], [249, 762], [662, 798],
           [260, 118], [256, 293], [131, 393], [294, 820], [2, 835], [338, 775], [811, 138], [467, 901], [655, 729],
           [171, 339], [972, 691], [873, 319], [194, 396], [823, 694], [381, 944], [645, 6], [86, 498], [4, 172],
           [178, 943], [821, 328], [457, 392], [464, 517], [312, 636], [789, 666], [592, 891], [694, 875], [501, 156],
           [787, 784], [847, 408], [732, 788], [380, 420], [99, 975], [260, 803], [8, 365], [140, 354], [858, 245],
           [932, 539], [269, 355], [73, 826], [790, 23], [11, 451], [417, 876], [864, 938], [380, 97], [183, 497],
           [641, 91], [542, 862], [336, 289], [333, 930], [146, 599], [753, 139], [727, 692], [650, 178], [777, 676],
           [165, 534], [511, 654], [218, 784], [419, 494], [367, 109], [188, 933], [923, 943], [293, 508], [436, 980],
           [684, 93], [106, 365], [700, 786], [313, 361], [971, 644], [795, 391], [781, 949], [628, 463], [399, 86],
           [836, 762], [101, 738], [673, 933], [132, 337], [482, 923], [464, 262], [821, 8], [472, 626], [769, 254],
           [493, 878], [789, 604], [535, 629], [24, 906], [480, 944], [798, 614], [814, 951], [121, 298], [589, 247],
           [686, 523], [715, 255], [836, 796], [779, 994], [177, 785], [787, 40], [228, 884], [821, 124], [260, 604],
           [537, 679], [231, 833], [338, 652], [468, 313], [909, 658], [58, 791], [533, 909], [342, 982], [937, 838],
           [673, 538], [260, 278], [648, 991], [85, 471], [906, 712], [285, 419], [270, 170], [331, 218], [698, 782],
           [899, 73], [229, 466], [514, 574], [470, 225], [996, 957], [538, 590], [215, 46], [554, 45], [365, 196],
           [690, 179], [454, 359], [468, 145], [547, 483], [467, 988], [388, 431], [776, 240], [971, 143], [297, 848],
           [119, 323], [717, 24], [666, 854], [481, 724], [124, 47], [558, 550], [85, 795], [568, 763], [967, 929],
           [657, 662], [425, 628], [596, 780], [757, 205], [898, 599], [171, 799], [688, 516], [204, 57], [335, 948],
           [864, 736], [963, 342], [656, 146], [613, 924], [69, 875], [249, 89], [926, 452], [288, 626], [23, 783],
           [919, 522], [124, 61], [335, 884], [898, 432], [171, 452], [471, 889], [989, 382], [101, 115], [345, 670],
           [827, 998], [687, 735], [916, 877], [149, 917], [133, 440], [804, 850], [603, 811], [262, 908], [939, 733],
           [231, 605], [241, 842], [505, 898], [498, 722], [837, 749], [129, 999], [25, 476], [301, 51], [789, 63],
           [274, 440]]
bikes = [[813, 565], [412, 590], [618, 8], [343, 72], [433, 380], [409, 263], [946, 636], [918, 710], [242, 757],
         [356, 900], [1, 986], [180, 877], [661, 870], [271, 777], [502, 637], [919, 868], [448, 403], [905, 212],
         [180, 659], [842, 870], [350, 465], [655, 818], [880, 344], [939, 218], [382, 710], [85, 535], [401, 427],
         [991, 444], [292, 526], [512, 617], [202, 328], [563, 825], [102, 846], [766, 932], [585, 987], [476, 158],
         [791, 644], [276, 150], [914, 538], [743, 944], [686, 27], [381, 364], [411, 866], [201, 836], [455, 339],
         [25, 386], [769, 696], [543, 656], [919, 654], [898, 781], [545, 864], [406, 871], [595, 715], [359, 724],
         [583, 617], [762, 855], [985, 950], [117, 146], [761, 118], [386, 814], [732, 629], [456, 852], [972, 213],
         [690, 711], [395, 308], [294, 32], [636, 291], [790, 201], [491, 168], [475, 378], [735, 437], [517, 984],
         [423, 975], [972, 297], [906, 887], [602, 673], [677, 180], [359, 911], [194, 24], [684, 744], [459, 559],
         [920, 804], [211, 179], [486, 180], [581, 58], [869, 787], [3, 62], [967, 289], [944, 28], [314, 889],
         [502, 470], [674, 845], [786, 457], [749, 892], [403, 383], [845, 843], [990, 655], [210, 433], [789, 392],
         [62, 401], [555, 833], [679, 548], [49, 252], [40, 964], [797, 567], [944, 555], [230, 562], [177, 458],
         [97, 179], [458, 482], [87, 949], [878, 70], [436, 716], [419, 471], [554, 570], [460, 831], [100, 766],
         [583, 198], [243, 248], [256, 705], [821, 862], [492, 213], [905, 899], [175, 328], [564, 138], [23, 9],
         [815, 415], [366, 27], [318, 526], [235, 886], [562, 482], [290, 678], [200, 632], [880, 2], [937, 153],
         [840, 750], [736, 452], [776, 185], [551, 929], [76, 216], [210, 999], [514, 297], [985, 807], [589, 105],
         [651, 894], [819, 679], [286, 743], [799, 94], [208, 287], [559, 767], [689, 751], [430, 181], [494, 494],
         [436, 927], [376, 140], [265, 881], [619, 232], [333, 707], [256, 811], [596, 833], [603, 131], [2, 881],
         [701, 225], [131, 576], [331, 187], [134, 157], [509, 771], [476, 301], [72, 358], [334, 789], [469, 413],
         [357, 235], [647, 735], [184, 230], [865, 565], [809, 201], [222, 885], [944, 828], [647, 761], [470, 587],
         [905, 437], [36, 853], [68, 980], [634, 974], [725, 298], [888, 5], [676, 115], [288, 991], [255, 60],
         [161, 874], [358, 181], [606, 619], [868, 421], [981, 905], [716, 165], [609, 167], [482, 652], [497, 710],
         [478, 729], [702, 720], [197, 469], [201, 214], [383, 167], [898, 588], [514, 773], [354, 752], [109, 897],
         [26, 958], [350, 114], [578, 214], [93, 871], [459, 444], [23, 432], [821, 152], [428, 549], [770, 180],
         [904, 892], [617, 801], [366, 519], [348, 386], [760, 620], [314, 254], [64, 83], [726, 658], [787, 12],
         [246, 517], [721, 678], [900, 619], [302, 521], [361, 235], [52, 533], [29, 313], [655, 705], [720, 436],
         [367, 261], [381, 841], [626, 536], [241, 718], [327, 26], [472, 656], [83, 963], [57, 966], [256, 83],
         [309, 139], [818, 696], [884, 560], [808, 859], [135, 663], [361, 243], [743, 417], [732, 400], [501, 273],
         [758, 73], [144, 271], [752, 319], [282, 295], [719, 927], [259, 999], [883, 252], [525, 116], [712, 859],
         [958, 981], [31, 662], [369, 151], [46, 578], [325, 423], [764, 8], [156, 963], [350, 863], [686, 618],
         [93, 432], [388, 135], [958, 33], [349, 34], [960, 587], [396, 454], [433, 340], [807, 596], [370, 902],
         [586, 655], [998, 286], [746, 607], [623, 126], [683, 846], [537, 779], [595, 237], [997, 847], [340, 608],
         [536, 840], [669, 6], [417, 664], [890, 834], [302, 787], [168, 621], [440, 540], [586, 353], [882, 816],
         [359, 991], [790, 57], [337, 418], [408, 68], [111, 914], [353, 843], [236, 859], [549, 908], [862, 387],
         [197, 793], [503, 255], [430, 118], [520, 614], [49, 694], [329, 372], [737, 311], [450, 465], [664, 345],
         [486, 680], [370, 810], [202, 752], [255, 861], [523, 686], [637, 350], [189, 929], [45, 288], [740, 509],
         [426, 991], [167, 833], [405, 878], [664, 297], [875, 755], [645, 868], [69, 726], [786, 7], [479, 166],
         [853, 848], [521, 867], [521, 683], [321, 741], [267, 873], [887, 788], [8, 644], [992, 797], [413, 5],
         [548, 572], [582, 118], [560, 604], [845, 928], [638, 535], [967, 294], [879, 512], [566, 463], [574, 58],
         [744, 561], [873, 874], [741, 797], [891, 101], [362, 265], [819, 906], [143, 318], [907, 829], [449, 387],
         [969, 110], [776, 376], [513, 552], [626, 580], [240, 42], [655, 272], [371, 753], [995, 354], [670, 964],
         [198, 811], [846, 7], [415, 393], [512, 201], [189, 470], [991, 814], [837, 223], [162, 261], [503, 445],
         [115, 210], [89, 423], [81, 278], [122, 119], [831, 578], [368, 873], [907, 200], [755, 7], [120, 314],
         [823, 655], [980, 465], [86, 339], [154, 791], [580, 840], [298, 53], [673, 648], [212, 406], [555, 472],
         [857, 298], [305, 610], [818, 452], [169, 236], [214, 812], [107, 96], [353, 494], [483, 466], [55, 410],
         [459, 709], [213, 458], [30, 750], [577, 934], [671, 407], [557, 891], [216, 494], [32, 256], [851, 979],
         [652, 63], [693, 133], [889, 74], [13, 454], [377, 212], [418, 658], [562, 988], [690, 852], [207, 382],
         [436, 602], [295, 73], [735, 964], [213, 777], [536, 497], [518, 758], [665, 753], [462, 700], [980, 452],
         [339, 530], [892, 9], [480, 147], [148, 616], [812, 591], [53, 529], [361, 891], [181, 147], [989, 461],
         [411, 462], [348, 529], [852, 737], [260, 359], [833, 309], [559, 474], [967, 423], [29, 474], [229, 210],
         [935, 939], [265, 43], [333, 868], [980, 235], [153, 233], [9, 105], [666, 906], [586, 357], [210, 522],
         [747, 990], [736, 528], [93, 61], [991, 129], [300, 656], [373, 940], [322, 888], [613, 892], [434, 331],
         [221, 306], [677, 522], [633, 89], [112, 100], [190, 712], [380, 194], [704, 460], [749, 41], [908, 587],
         [300, 275], [47, 865], [485, 638], [5, 279], [954, 483], [394, 887], [134, 112], [77, 585], [738, 927],
         [936, 962], [627, 581], [26, 600], [850, 316], [381, 79], [475, 409], [872, 991], [366, 302], [941, 851],
         [506, 17], [932, 627], [413, 795], [383, 899], [189, 867], [84, 562], [586, 969], [766, 836], [665, 947],
         [316, 417], [3, 435], [745, 99], [795, 710], [938, 644], [52, 950], [739, 758], [385, 266], [378, 672],
         [579, 969], [283, 768], [71, 411], [818, 172], [429, 232], [148, 927], [826, 110], [654, 835], [727, 103],
         [36, 433], [399, 472], [628, 722], [661, 876], [704, 714], [684, 87], [80, 95], [61, 772], [590, 598],
         [901, 664], [800, 319], [643, 596], [449, 588], [30, 22], [936, 350], [70, 720], [607, 208], [399, 544],
         [349, 546], [9, 71], [205, 543], [986, 842], [45, 23], [714, 900], [96, 854], [757, 2], [660, 147], [837, 125],
         [501, 578], [54, 180], [944, 955], [624, 615], [561, 800], [193, 869], [709, 155], [552, 823], [168, 142],
         [971, 955], [737, 744], [394, 530], [529, 295], [161, 850], [768, 593], [850, 556], [768, 865], [1, 935],
         [760, 184], [622, 11], [954, 818], [519, 15], [637, 317], [83, 676], [139, 37], [152, 576], [172, 667],
         [469, 996], [522, 953], [425, 6], [707, 607], [154, 584], [27, 842], [727, 991], [615, 536], [815, 861],
         [818, 629], [280, 71], [251, 464], [121, 711], [446, 422], [127, 435], [543, 823], [36, 844], [762, 292],
         [675, 864], [142, 343], [358, 457], [756, 915], [208, 924], [757, 384], [420, 91], [898, 113], [548, 51],
         [450, 637], [210, 263], [319, 233], [474, 451], [601, 564], [78, 777], [993, 649], [289, 8], [119, 937],
         [13, 192], [861, 150], [949, 23], [738, 937], [491, 535], [913, 510], [523, 997], [983, 291], [478, 364],
         [552, 748], [409, 464], [970, 770], [755, 4], [320, 863], [410, 60], [488, 435], [111, 923], [278, 411],
         [213, 223], [615, 972], [558, 296], [527, 500], [606, 997], [235, 690], [606, 294], [320, 753], [778, 459],
         [626, 873], [379, 939], [997, 94], [174, 350], [320, 951], [700, 732], [93, 936], [248, 708], [619, 496],
         [596, 14], [932, 348], [575, 946], [313, 678], [871, 295], [847, 243], [362, 802], [583, 576], [250, 886],
         [302, 813], [560, 300], [916, 203], [908, 359], [86, 214], [182, 222], [5, 706], [113, 525], [989, 683],
         [602, 52], [447, 587], [277, 158], [591, 368], [184, 772], [646, 683], [879, 728], [289, 866], [270, 442],
         [0, 990], [810, 639], [816, 70], [761, 204], [498, 75], [933, 159], [329, 690], [692, 711], [104, 93],
         [531, 431], [554, 818], [759, 655], [544, 458], [834, 979], [231, 811], [188, 162], [215, 567], [983, 904],
         [525, 267], [946, 772], [441, 393], [800, 587], [393, 542], [814, 611], [37, 428], [488, 113], [409, 273],
         [940, 372], [334, 631], [541, 759], [520, 954], [857, 259], [561, 717], [540, 34], [45, 909], [379, 989],
         [141, 844], [146, 687], [412, 655], [23, 760], [517, 569], [124, 868], [2, 998], [176, 257], [310, 857],
         [743, 44], [637, 710], [878, 61], [559, 600], [768, 862], [88, 148], [747, 936], [779, 933], [684, 861],
         [970, 934], [71, 863], [560, 715], [71, 48], [119, 896], [972, 704], [762, 632], [344, 435], [581, 327],
         [969, 160], [935, 865], [531, 27], [135, 137], [459, 939], [364, 258], [236, 829], [316, 90], [494, 783],
         [46, 610], [482, 326], [680, 71], [663, 48], [705, 796], [873, 235], [328, 710], [868, 436], [939, 142],
         [949, 689], [745, 539], [250, 496], [433, 565], [797, 253], [528, 251], [292, 848], [472, 414], [108, 749],
         [539, 564], [634, 186], [940, 758], [176, 76], [134, 98], [78, 674], [859, 641], [263, 464], [990, 946],
         [152, 486], [801, 662], [84, 911], [176, 738], [834, 531], [228, 960], [133, 837], [522, 310], [123, 813],
         [361, 149], [463, 46], [80, 251], [760, 753], [621, 282], [39, 49], [78, 894], [917, 653], [196, 643],
         [899, 802], [116, 517], [295, 38], [685, 503], [838, 46], [372, 965], [692, 137], [386, 225], [438, 258],
         [956, 585], [152, 234], [539, 831], [416, 139], [586, 680], [649, 454], [795, 470], [24, 542], [650, 726],
         [388, 827], [344, 739], [517, 400], [57, 185], [564, 654], [766, 346], [731, 807], [692, 765], [840, 307],
         [164, 170], [335, 822], [841, 319], [605, 888], [533, 478], [358, 892], [588, 693], [215, 641], [342, 276],
         [724, 548], [386, 314], [20, 788], [590, 305], [368, 45], [40, 838], [808, 990], [504, 338], [653, 107],
         [531, 59], [8, 835], [474, 267], [354, 378], [273, 496], [378, 281], [24, 3], [946, 569], [509, 545],
         [706, 124], [649, 237], [636, 732], [678, 52], [134, 138], [479, 927], [715, 64], [993, 45], [50, 95],
         [482, 350], [710, 826], [905, 17], [604, 113], [117, 535], [392, 456], [412, 509], [992, 629], [510, 134],
         [727, 669], [848, 335], [12, 815], [826, 297], [816, 15], [905, 195], [564, 429], [54, 558], [864, 484],
         [452, 87], [269, 243], [654, 424], [308, 535], [975, 582], [757, 263], [472, 381], [954, 159], [677, 896],
         [912, 134], [32, 841], [637, 655], [221, 31], [236, 492], [700, 787], [794, 814], [755, 978], [446, 806],
         [281, 38], [624, 32], [924, 389], [585, 323], [340, 192], [11, 906], [926, 309], [245, 493], [9, 486],
         [504, 257], [388, 192], [68, 700], [270, 253], [116, 178], [957, 466], [485, 219], [544, 114], [740, 82],
         [925, 897], [101, 519], [428, 73], [284, 254], [105, 96], [648, 830], [414, 304], [371, 940], [479, 103],
         [819, 813], [676, 501], [692, 183], [338, 528], [204, 216], [490, 250], [774, 877], [137, 74], [504, 453],
         [239, 175], [324, 780], [680, 833], [323, 961], [126, 496], [853, 744], [212, 50], [482, 856], [748, 129],
         [116, 397], [379, 427], [923, 671], [400, 633], [920, 362], [464, 696], [970, 845], [373, 723], [124, 939],
         [658, 30], [357, 556], [857, 701], [462, 341], [741, 11], [48, 356], [400, 803], [35, 965], [950, 35],
         [808, 248], [904, 820], [89, 472], [875, 780], [243, 381], [246, 843], [251, 283], [255, 649], [334, 505],
         [759, 199], [423, 355], [561, 985], [701, 913], [391, 259], [202, 69], [261, 401], [933, 905], [828, 197],
         [345, 207], [608, 668], [652, 983], [499, 217], [145, 28], [80, 417], [198, 95], [744, 14], [239, 643],
         [305, 525], [1, 951], [889, 383], [975, 175], [831, 123], [657, 876], [307, 34], [648, 727], [521, 210],
         [180, 482], [819, 460], [542, 895], [796, 55], [878, 774], [437, 98], [478, 28], [523, 245], [588, 991]]
# workers = [[0, 0], [2, 1]]
# bikes = [[1, 2], [3, 3]]

start = time.time()
print(assignBikes(workers, bikes))
end = time.time()
print("Time taken = " + str(end - start) + " s")
