UserID = int
UserName = str

KEEPSAKE_GAMES: dict[UserID, UserName] = {
    # Developers
    98073678935236608: "martymatsu",
    324163770920206338: "kappische",
    495267602831114271: "claesengdal",
    1199263621058932746: "keephan",
    1145715905972666429: "louisekeepsake",
    179593007828434944: "madnessbox",
    421396824209752077: "olofwallentin",
    501725642249994240: "tob.mo",

    # Other
    162303657059155968: "cthulhutheking",
    209049051474165761: "meatmanalfons",
    240882268313223169: "oskmos",
    476695441849974785: ".coulianos",

    636265207185801227: "lars"
}

MODERATORS: dict[UserID, UserName] = {
    147843262776868868: "sircorewin",
    204748535957159936: "the_ryu",
    173170091477827584: "upgradecap",
}


def is_keepsake_employee(user_id: UserID) -> bool:
    return user_id in KEEPSAKE_GAMES.keys()
