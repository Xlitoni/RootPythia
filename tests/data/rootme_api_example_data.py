# pylint: disable=line-too-long

# !!! CAUTION !!!
#
# Some test heavily depends on the hardcoded data in here
# changing it will probably result in a lot of broken tests
#
# !!! CAUTION !!!

# This is not the real output for /auteurs/1, challenges, solutions and validations have been truncated!
auteurs_example_data = {
    "id_auteur": "1",
    "nom": "g0uZ",
    "statut": "0minirezo",
    "score": "3040",
    "position": 2514,
    "rang": "insider",
    "challenges": [
        {
            "id_challenge": "5",
            "url_challenge": "fr/Challenges/Web-Serveur/HTML-Code-source",
        },
        {
            "id_challenge": "11",
            "url_challenge": "fr/Challenges/App-Script/Bash-cron",
        },
        {
            "id_challenge": "13",
            "url_challenge": "fr/Challenges/Web-Serveur/HTTP-User-agent",
        },
    ],
    "solutions": [
        {
            "id_solution": "3",
            "url_solution": "fr/Challenges/Web-Serveur/Mot-de-passe-faible/Solution-no3",
        },
        {
            "id_solution": "15",
            "url_solution": "fr/Challenges/Cryptanalyse/Hash-Message-Digest-5/Solution-no15",
        },
        {
            "id_solution": "303",
            "url_solution": "fr/Challenges/Reseau/DNS-transfert-de-zone/Solution-no303",
        },
    ],
    "validations": [
        {"id_challenge": "2364", "id_rubrique": "189", "date": "2022-08-23 13:10:02"},
        {"id_challenge": "2259", "id_rubrique": "189", "date": "2022-05-20 09:00:54"},
        {"id_challenge": "2843", "id_rubrique": "189", "date": "2022-05-20 08:53:46"},
    ],
}

# This is not the real output for /auteurs/819227 on October, 26th 2023
auteurs_with_score_zero_example_data = {
    "id_auteur": "819227",
    "nom": "Alphaphi",
    "statut": "6forum",
    "score": "0",
    "position": "",
    "challenges": [],
    "solutions": [],
    "validations": [],
}


# the real output for /challenges/5 on May, 30th 2023
challenges_example_data = [
    {
        "titre": "HTML - Code source",
        "rubrique": "Web - Serveur",
        "soustitre": "Rien de bien difficile",
        "score": "5",
        "id_rubrique": "68",
        "id_trad": "5",
        "url_challenge": "fr/Challenges/Web-Serveur/HTML-Code-source",
        "date_publication": "2006-01-17 13:45:35",
        "maj": "2019-08-15 13:52:07",
        "difficulte": "Très facile",
        "auteurs": {"0": {"id_auteur": "1", "nom": "g0uZ"}},
        "validations": {
            "0": {"id_auteur": "784632", "date": "2023-05-30 11:59:32"},
            "1": {"id_auteur": "784613", "date": "2023-05-30 11:21:43"},
            "2": {"id_auteur": "781693", "date": "2023-05-30 10:20:46"},
            "3": {"id_auteur": "779285", "date": "2023-05-30 09:22:58"},
            "4": {"id_auteur": "783076", "date": "2023-05-30 09:01:42"},
            "5": {"id_auteur": "784561", "date": "2023-05-30 02:45:22"},
            "6": {"id_auteur": "780797", "date": "2023-05-30 01:55:46"},
            "7": {"id_auteur": "783979", "date": "2023-05-30 01:40:39"},
            "8": {"id_auteur": "762185", "date": "2023-05-30 01:28:57"},
            "9": {"id_auteur": "781614", "date": "2023-05-29 22:30:09"},
            "10": {"id_auteur": "784528", "date": "2023-05-29 21:51:01"},
            "11": {"id_auteur": "134726", "date": "2023-05-29 20:11:12"},
            "12": {"id_auteur": "784504", "date": "2023-05-29 19:42:42"},
            "13": {"id_auteur": "784131", "date": "2023-05-29 19:36:04"},
            "14": {"id_auteur": "784497", "date": "2023-05-29 19:25:02"},
            "15": {"id_auteur": "784073", "date": "2023-05-29 18:52:38"},
            "16": {"id_auteur": "703731", "date": "2023-05-29 17:29:10"},
            "17": {"id_auteur": "636308", "date": "2023-05-29 17:28:07"},
            "18": {"id_auteur": "750768", "date": "2023-05-29 17:16:34"},
            "19": {"id_auteur": "612481", "date": "2023-05-29 17:14:00"},
            "20": {"id_auteur": "774520", "date": "2023-05-29 16:36:20"},
            "21": {"id_auteur": "783494", "date": "2023-05-29 16:33:53"},
            "22": {"id_auteur": "784451", "date": "2023-05-29 16:25:00"},
            "23": {"id_auteur": "783561", "date": "2023-05-29 16:12:27"},
            "24": {"id_auteur": "784424", "date": "2023-05-29 15:53:35"},
            "25": {"id_auteur": "759326", "date": "2023-05-29 15:44:18"},
            "26": {"id_auteur": "784446", "date": "2023-05-29 15:39:38"},
            "27": {"id_auteur": "784449", "date": "2023-05-29 15:34:52"},
            "28": {"id_auteur": "784439", "date": "2023-05-29 15:33:22"},
            "29": {"id_auteur": "782639", "date": "2023-05-29 13:49:17"},
            "30": {"id_auteur": "112090", "date": "2023-05-29 13:03:36"},
            "31": {"id_auteur": "783443", "date": "2023-05-29 12:47:02"},
            "32": {"id_auteur": "760408", "date": "2023-05-29 10:51:57"},
            "33": {"id_auteur": "772057", "date": "2023-05-29 10:02:45"},
            "34": {"id_auteur": "713396", "date": "2023-05-29 10:00:21"},
            "35": {"id_auteur": "517157", "date": "2023-05-29 06:17:39"},
            "36": {"id_auteur": "626556", "date": "2023-05-29 05:50:39"},
            "37": {"id_auteur": "724402", "date": "2023-05-29 04:20:36"},
            "38": {"id_auteur": "784348", "date": "2023-05-29 02:48:00"},
            "39": {"id_auteur": "778499", "date": "2023-05-29 02:36:26"},
            "40": {"id_auteur": "719729", "date": "2023-05-28 23:51:09"},
            "41": {"id_auteur": "783478", "date": "2023-05-28 23:28:47"},
            "42": {"id_auteur": "769948", "date": "2023-05-28 23:26:48"},
            "43": {"id_auteur": "724083", "date": "2023-05-28 23:20:57"},
            "44": {"id_auteur": "725740", "date": "2023-05-28 23:16:36"},
            "45": {"id_auteur": "784312", "date": "2023-05-28 21:32:33"},
            "46": {"id_auteur": "784155", "date": "2023-05-28 20:19:48"},
            "47": {"id_auteur": "784293", "date": "2023-05-28 19:49:24"},
            "48": {"id_auteur": "625345", "date": "2023-05-28 18:33:04"},
            "49": {"id_auteur": "784280", "date": "2023-05-28 18:25:34"},
            "50": {"id_auteur": "784225", "date": "2023-05-28 17:18:02"},
            "51": {"id_auteur": "784269", "date": "2023-05-28 17:13:14"},
            "52": {"id_auteur": "784158", "date": "2023-05-28 17:02:09"},
            "53": {"id_auteur": "778763", "date": "2023-05-28 16:08:29"},
            "54": {"id_auteur": "784249", "date": "2023-05-28 15:13:50"},
            "55": {"id_auteur": "784230", "date": "2023-05-28 14:34:57"},
            "56": {"id_auteur": "765896", "date": "2023-05-28 14:17:49"},
            "57": {"id_auteur": "778100", "date": "2023-05-28 12:00:02"},
            "58": {"id_auteur": "784198", "date": "2023-05-28 10:23:10"},
            "59": {"id_auteur": "784210", "date": "2023-05-28 10:17:04"},
            "60": {"id_auteur": "757315", "date": "2023-05-28 10:16:02"},
            "61": {"id_auteur": "758452", "date": "2023-05-28 09:57:21"},
            "62": {"id_auteur": "771667", "date": "2023-05-28 06:41:48"},
            "63": {"id_auteur": "784093", "date": "2023-05-28 02:44:12"},
            "64": {"id_auteur": "160646", "date": "2023-05-28 01:57:33"},
            "65": {"id_auteur": "758361", "date": "2023-05-27 22:36:04"},
            "66": {"id_auteur": "772238", "date": "2023-05-27 21:12:56"},
            "67": {"id_auteur": "783872", "date": "2023-05-27 21:10:38"},
            "68": {"id_auteur": "784107", "date": "2023-05-27 20:56:29"},
            "69": {"id_auteur": "784119", "date": "2023-05-27 19:52:49"},
            "70": {"id_auteur": "698147", "date": "2023-05-27 19:19:42"},
            "71": {"id_auteur": "784111", "date": "2023-05-27 18:50:05"},
            "72": {"id_auteur": "752552", "date": "2023-05-27 18:05:34"},
            "73": {"id_auteur": "749755", "date": "2023-05-27 17:37:11"},
            "74": {"id_auteur": "784095", "date": "2023-05-27 17:34:30"},
            "75": {"id_auteur": "776217", "date": "2023-05-27 17:23:58"},
            "76": {"id_auteur": "774798", "date": "2023-05-27 15:12:18"},
            "77": {"id_auteur": "726160", "date": "2023-05-27 15:00:46"},
            "78": {"id_auteur": "784078", "date": "2023-05-27 14:57:52"},
            "79": {"id_auteur": "783869", "date": "2023-05-27 13:14:18"},
            "80": {"id_auteur": "784037", "date": "2023-05-27 13:00:24"},
            "81": {"id_auteur": "502384", "date": "2023-05-27 11:28:41"},
            "82": {"id_auteur": "735231", "date": "2023-05-27 10:00:37"},
            "83": {"id_auteur": "783906", "date": "2023-05-27 09:57:41"},
            "84": {"id_auteur": "781433", "date": "2023-05-27 09:16:53"},
            "85": {"id_auteur": "784009", "date": "2023-05-27 04:02:06"},
            "86": {"id_auteur": "784006", "date": "2023-05-27 03:33:37"},
            "87": {"id_auteur": "783310", "date": "2023-05-27 03:31:57"},
            "88": {"id_auteur": "783299", "date": "2023-05-27 02:18:26"},
            "89": {"id_auteur": "695339", "date": "2023-05-26 23:15:39"},
            "90": {"id_auteur": "716147", "date": "2023-05-26 23:15:26"},
            "91": {"id_auteur": "783958", "date": "2023-05-26 22:09:40"},
            "92": {"id_auteur": "783975", "date": "2023-05-26 22:03:44"},
            "93": {"id_auteur": "777075", "date": "2023-05-26 21:59:27"},
            "94": {"id_auteur": "470669", "date": "2023-05-26 21:50:33"},
            "95": {"id_auteur": "344282", "date": "2023-05-26 21:37:49"},
            "96": {"id_auteur": "783946", "date": "2023-05-26 21:22:06"},
            "97": {"id_auteur": "781417", "date": "2023-05-26 19:50:47"},
            "98": {"id_auteur": "735196", "date": "2023-05-26 18:01:38"},
            "99": {"id_auteur": "783895", "date": "2023-05-26 17:44:51"},
        },
    },
    {
        "rel": "next",
        "href": "https://api.www.root-me.org/challenges/5?debut_validations=100",
    },
]
