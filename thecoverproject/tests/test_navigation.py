from thecoverproject import Console, PageCategory
from thecoverproject.navigation import get_game_system_page_data, get_game_page_data, get_game_covers_data, \
    get_nb_of_pages_for_game_system, search

TEST_GAME_ID = 895


def test_get_game_system_page_data():
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
    data = get_game_system_page_data(Console.playstation_one, PageCategory.NUM)
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
