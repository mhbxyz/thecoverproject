from thecoverproject import Consoles, PageIndex
from thecoverproject.navigation import get_game_system_page_data


def test_get_game_system_page_data():
    expected_result = [
        {
            'name': '007 - The World Is Not Enough',
            'nb_of_covers': 2,
            'url': 'http://thecoverproject.net/view.php?game_id=14974'
        },
        {
            'name': '007 - Tomorrow Nevers Dies',
            'nb_of_covers': 2,
            'url': 'http://thecoverproject.net/view.php?game_id=14975'
        },
        {
            'name': '007 Racing',
            'nb_of_covers': 4,
            'url': 'http://thecoverproject.net/view.php?game_id=11568'
        },
        {
            'name': '1 Xtreme',
            'nb_of_covers': 5,
            'url': 'http://thecoverproject.net/view.php?game_id=10572'
        },
        {
            'name': '102 Dalmatians: Puppies to the Rescue',
            'nb_of_covers': 1,
            'url': 'http://thecoverproject.net/view.php?game_id=2099'
        },
        {
            'name': '2 Xtreme',
            'nb_of_covers': 4,
            'url': 'http://thecoverproject.net/view.php?game_id=2102'
        },
        {
            'name': '2002 FIFA World Cup',
            'nb_of_covers': 2,
            'url': 'http://thecoverproject.net/view.php?game_id=14976'
        },
        {
            'name': '3 Xtreme',
            'nb_of_covers': 4,
            'url': 'http://thecoverproject.net/view.php?game_id=8019'
        },
        {
            'name': '3D Baseball',
            'nb_of_covers': 2,
            'url': 'http://thecoverproject.net/view.php?game_id=14973'
        },
        {
            'name': '3D Lemmings',
            'nb_of_covers': 4,
            'url': 'http://thecoverproject.net/view.php?game_id=14194'
        },
        {
            'name': '40 Winks',
            'nb_of_covers': 10,
            'url': 'http://thecoverproject.net/view.php?game_id=1209'
        }
    ]
    data = get_game_system_page_data(Consoles.playstation_one, PageIndex.NUM)
    assert data == expected_result
