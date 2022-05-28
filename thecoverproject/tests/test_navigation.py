from thecoverproject import Console, PageCategory
from thecoverproject.navigation import get_platform_page_data, get_game_page_data, get_game_covers_data, \
    get_nb_of_pages_for_game_system, search

TEST_GAME_ID = 895


def test_get_platform_page_data():
    expected_result = [
        {
            'name': '007 - The World Is Not Enough',
            'url': 'http://thecoverproject.net/view.php?game_id=14974'
        },
        {
            'name': '007 - Tomorrow Nevers Dies',
            'url': 'http://thecoverproject.net/view.php?game_id=14975'
        },
        {
            'name': '007 Racing',
            'url': 'http://thecoverproject.net/view.php?game_id=11568'
        },
        {
            'name': '1 Xtreme',
            'url': 'http://thecoverproject.net/view.php?game_id=10572'
        },
        {
            'name': '102 Dalmatians: Puppies to the Rescue',
            'url': 'http://thecoverproject.net/view.php?game_id=2099'
        },
        {
            'name': '2 Xtreme',
            'url': 'http://thecoverproject.net/view.php?game_id=2102'
        },
        {
            'name': '2002 FIFA World Cup',
            'url': 'http://thecoverproject.net/view.php?game_id=14976'
        },
        {
            'name': '3 Xtreme',
            'url': 'http://thecoverproject.net/view.php?game_id=8019'
        },
        {
            'name': '3D Baseball',
            'url': 'http://thecoverproject.net/view.php?game_id=14973'
        },
        {
            'name': '3D Lemmings',
            'url': 'http://thecoverproject.net/view.php?game_id=14194'
        },
        {
            'name': '40 Winks',
            'url': 'http://thecoverproject.net/view.php?game_id=1209'
        }
    ]
    data = get_platform_page_data(Console.playstation_one, PageCategory.NUM)
    for row in data:
        del row["nb_of_covers"]  # Removing number of covers because it's not a constant
    assert data == expected_result


def test_get_game_page_data():
    expected_result = {
        "description": "Custom Cover",
        "format": "NTSC",
        "created_by": "BadChad",
        "region": "United States",
        "case_type": "DVD Case - Standard",
        "urls": {
            "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_1_thumb.jpg",
            "download": "http://thecoverproject.net/download_cover.php?src=cdn&cover_id=1372"
        },
        "other_covers": [
            {
                "description": "Custom Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_1_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=1372"
                }
            },
            {
                "description": "Custom Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "http://thecoverproject.net/uploads/pending/playstation_1.castlevaniasymphonyofthenight_US.16326074111335468916_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=18716"
                }
            },
            {
                "description": "Custom Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "http://thecoverproject.net/uploads/pending/playstation_1.castlevaniasymphonyofthenight_US.163665568477547041_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=19565"
                }
            },
            {
                "description": "Retail Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "http://thecoverproject.net/uploads/pending/playstation_1.castlevaniasymphonyofthenight_US.16366557371587417560_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=19566"
                }
            },
            {
                "description": "CD Case - EU Front",
                "format": "PAL",
                "region": "Europe",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevania_front_eu_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=3041"
                }
            },
            {
                "description": "CD Case - EU Rear",
                "format": "PAL",
                "region": "Europe",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevania_rear_eu_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=3042"
                }
            },
            {
                "description": "Custom Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps_castlevaniasymphonyofthenight_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=7577"
                }
            },
            {
                "description": "Custom Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps_castlevaniasymphonyofthenight_2_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=7578"
                }
            },
            {
                "description": "Custom Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps_castlevaniasymphonyofthenight_3_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=7579"
                }
            },
            {
                "description": "Custom DVD Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=373"
                }
            },
            {
                "description": "Custom DVD Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_2_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=1601"
                }
            },
            {
                "description": "Custom DVD Cover",
                "format": "NTSC",
                "region": "United States",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_3_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=1637"
                }
            },
            {
                "description": "Disc -EU",
                "format": "PAL",
                "region": "Europe",
                "urls": {
                    "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevania_cd_eu_thumb.jpg",
                    "cover": "http://thecoverproject.net/view.php?cover_id=3043"
                }
            }
        ]
    }
    data = get_game_page_data(TEST_GAME_ID)
    del data["nb_of_downloads"]  # Removing number of downloads because it's not a constant
    assert data == expected_result


def test_get_game_page_data_with_images():
    thumbnail: bytes
    cover: bytes

    data = get_game_page_data(TEST_GAME_ID, with_images=True)

    with open("images/ps1_castlevaniasymphonyofthenight_1_thumb.jpg", "rb") as image:
        thumbnail = image.read()
        assert data["images"]["thumbnail"] == thumbnail

    with open("images/ps1_castlevaniasymphonyofthenight_1.jpg", "rb") as image:
        cover = image.read()
        assert data["images"]["cover"] == cover


def test_get_game_covers():
    expected_result = [
        {
            "description": "Custom Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_1_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=1372"
            }
        },
        {
            "description": "Custom Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "http://thecoverproject.net/uploads/pending/playstation_1.castlevaniasymphonyofthenight_US.16326074111335468916_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=18716"
            }
        },
        {
            "description": "Custom Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "http://thecoverproject.net/uploads/pending/playstation_1.castlevaniasymphonyofthenight_US.163665568477547041_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=19565"
            }
        },
        {
            "description": "Retail Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "http://thecoverproject.net/uploads/pending/playstation_1.castlevaniasymphonyofthenight_US.16366557371587417560_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=19566"
            }
        },
        {
            "description": "CD Case - EU Front",
            "format": "PAL",
            "region": "Europe",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevania_front_eu_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=3041"
            }
        },
        {
            "description": "CD Case - EU Rear",
            "format": "PAL",
            "region": "Europe",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevania_rear_eu_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=3042"
            }
        },
        {
            "description": "Custom Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps_castlevaniasymphonyofthenight_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=7577"
            }
        },
        {
            "description": "Custom Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps_castlevaniasymphonyofthenight_2_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=7578"
            }
        },
        {
            "description": "Custom Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps_castlevaniasymphonyofthenight_3_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=7579"
            }
        },
        {
            "description": "Custom DVD Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=373"
            }
        },
        {
            "description": "Custom DVD Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_2_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=1601"
            }
        },
        {
            "description": "Custom DVD Cover",
            "format": "NTSC",
            "region": "United States",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevaniasymphonyofthenight_3_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=1637"
            }
        },
        {
            "description": "Disc -EU",
            "format": "PAL",
            "region": "Europe",
            "urls": {
                "thumbnail": "https://coverproject.sfo2.cdn.digitaloceanspaces.com/playstation_1/ps1_castlevania_cd_eu_thumb.jpg",
                "cover": "http://thecoverproject.net/view.php?cover_id=3043"
            }
        }
    ]
    data = get_game_covers_data(TEST_GAME_ID)
    assert data == expected_result


def test_get_nb_of_pages_for_game_system():
    expected_result = 3
    nb_of_pages = get_nb_of_pages_for_game_system(Console.playstation_one, PageCategory.A)
    assert nb_of_pages == expected_result


def test_search():
    expected_result = [{
        'name': 'Castlevania: Symphony of the Night',
        'platform_code': 'PS1',
        'url': 'http://thecoverproject.net/view.php?game_id=895'
    }]
    data = search("Castlevania Symphony of the Night")
    assert data == expected_result


def test_search_with_multiple_result_pages():
    expected_result = [
        {
            "name": "Beats of Rage: Castlevania Symphony of Destruction",
            "platform_code": "DC",
            "url": "http://thecoverproject.net/view.php?game_id=6221"
        },
        {
            "name": "Castlevania",
            "platform_code": "N64",
            "url": "http://thecoverproject.net/view.php?game_id=1029"
        },
        {
            "name": "Castlevania",
            "platform_code": "GBA",
            "url": "http://thecoverproject.net/view.php?game_id=1116"
        },
        {
            "name": "Castlevania",
            "platform_code": "PS2",
            "url": "http://thecoverproject.net/view.php?game_id=2401"
        },
        {
            "name": "Castlevania",
            "platform_code": "NES",
            "url": "http://thecoverproject.net/view.php?game_id=2750"
        },
        {
            "name": "Castlevania - Dracula X",
            "platform_code": "SNES",
            "url": "http://thecoverproject.net/view.php?game_id=12887"
        },
        {
            "name": "Castlevania 2: Belmont's Revenge",
            "platform_code": "GB",
            "url": "http://thecoverproject.net/view.php?game_id=611"
        },
        {
            "name": "Castlevania Adventure, The",
            "platform_code": "GB",
            "url": "http://thecoverproject.net/view.php?game_id=1103"
        },
        {
            "name": "Castlevania Bloodlines (aka Castlevania: The New Generation)",
            "platform_code": "Genesis",
            "url": "http://thecoverproject.net/view.php?game_id=1735"
        },
        {
            "name": "Castlevania Chronicles",
            "platform_code": "PS1",
            "url": "http://thecoverproject.net/view.php?game_id=6411"
        },
        {
            "name": "Castlevania Double Pack",
            "platform_code": "GBA",
            "url": "http://thecoverproject.net/view.php?game_id=736"
        },
        {
            "name": "Castlevania II: Simon's Quest",
            "platform_code": "NES",
            "url": "http://thecoverproject.net/view.php?game_id=2744"
        },
        {
            "name": "Castlevania III: Dracula's Curse",
            "platform_code": "NES",
            "url": "http://thecoverproject.net/view.php?game_id=2754"
        },
        {
            "name": "Castlevania Judgment",
            "platform_code": "Wii",
            "url": "http://thecoverproject.net/view.php?game_id=7697"
        },
        {
            "name": "Castlevania Legends",
            "platform_code": "GB",
            "url": "http://thecoverproject.net/view.php?game_id=612"
        },
        {
            "name": "Castlevania: Aria of Sorrow",
            "platform_code": "GBA",
            "url": "http://thecoverproject.net/view.php?game_id=8"
        },
        {
            "name": "Castlevania: Circle of the Moon",
            "platform_code": "GBA",
            "url": "http://thecoverproject.net/view.php?game_id=9"
        },
        {
            "name": "Castlevania: Curse Of Darkness",
            "platform_code": "PS2",
            "url": "http://thecoverproject.net/view.php?game_id=2033"
        },
        {
            "name": "Castlevania: Curse of Darkness",
            "platform_code": "Xbox",
            "url": "http://thecoverproject.net/view.php?game_id=14349"
        },
        {
            "name": "Castlevania: Dawn of Sorrow",
            "platform_code": "DS",
            "url": "http://thecoverproject.net/view.php?game_id=767"
        },
        {
            "name": "Castlevania: Dracula X (aka Castlevania: Vampire's Kiss)",
            "platform_code": "SNES",
            "url": "http://thecoverproject.net/view.php?game_id=2267"
        },
        {
            "name": "Castlevania: Harmony of Dissonance",
            "platform_code": "GBA",
            "url": "http://thecoverproject.net/view.php?game_id=10"
        },
        {
            "name": "Castlevania: Lament Of Innocence",
            "platform_code": "PS2",
            "url": "http://thecoverproject.net/view.php?game_id=3354"
        },
        {
            "name": "Castlevania: Legacy of Darkness",
            "platform_code": "N64",
            "url": "http://thecoverproject.net/view.php?game_id=564"
        },
        {
            "name": "Castlevania: Lords of Shadow",
            "platform_code": "X360",
            "url": "http://thecoverproject.net/view.php?game_id=7704"
        },
        {
            "name": "Castlevania: Lords of Shadow",
            "platform_code": "PS3",
            "url": "http://thecoverproject.net/view.php?game_id=12058"
        },
        {
            "name": "Castlevania: Lords of Shadow 2",
            "platform_code": "X360",
            "url": "http://thecoverproject.net/view.php?game_id=9680"
        },
        {
            "name": "Castlevania: Lords of Shadow 2",
            "platform_code": "PS3",
            "url": "http://thecoverproject.net/view.php?game_id=12059"
        },
        {
            "name": "Castlevania: Lords of Shadow \u2013 Mirror of Fate",
            "platform_code": "3ds",
            "url": "http://thecoverproject.net/view.php?game_id=9600"
        },
        {
            "name": "Castlevania: Lords of Shadow: Mirror of Fate",
            "platform_code": "3ds",
            "url": "http://thecoverproject.net/view.php?game_id=9601"
        },
        {
            "name": "Castlevania: Order of Ecclesia",
            "platform_code": "DS",
            "url": "http://thecoverproject.net/view.php?game_id=7778"
        },
        {
            "name": "Castlevania: Portrait of Ruin",
            "platform_code": "DS",
            "url": "http://thecoverproject.net/view.php?game_id=2601"
        },
        {
            "name": "Castlevania: Symphony of the Night",
            "platform_code": "PS1",
            "url": "http://thecoverproject.net/view.php?game_id=895"
        },
        {
            "name": "Castlevania: The Dracula X Chronicles",
            "platform_code": "PSP",
            "url": "http://thecoverproject.net/view.php?game_id=4070"
        },
        {
            "name": "Super Castlevania IV",
            "platform_code": "SNES",
            "url": "http://thecoverproject.net/view.php?game_id=4739"
        }
    ]
    data = search("Castlevania")
    assert data == expected_result
