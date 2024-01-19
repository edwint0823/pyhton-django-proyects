table = [
    {
        'category': 'ACCION',
        'games': [
            "GTA",
            "COD",
            "PUBG"
        ]
    },
    {
        'category': "AVENTURA",
        'games': [
            "ASSASSINS CREED",
            "CRASH",
            "PRINCE OF PERSIA"
        ],
    },
    {
        'category': "DEPORTES",
        'games': [
            "FIFA 21",
            "PRO 21",
            "MOTO GP 21"
        ],
    }
]

for element in table:
    print(f"---------------- {element['category']} ----------------")
    for game in element['games']:
        print(game)
