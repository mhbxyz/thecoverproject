from http import HTTPStatus

import requests

from thecoverproject import Consoles, urls


class TestConsoles:

    def test_reach_three_do(self):
        request = requests.get(urls.consoles[Consoles.three_do])
        assert request.status_code == HTTPStatus.OK

    def test_reach_amiga_cd_thirty_two(self):
        request = requests.get(urls.consoles[Consoles.amiga_cd_thirty_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_two_six_zero_zero(self):
        request = requests.get(urls.consoles[Consoles.atari_two_six_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_five_two_zero_zero(self):
        request = requests.get(urls.consoles[Consoles.atari_five_two_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_seven_eight_zero_zero(self):
        request = requests.get(urls.consoles[Consoles.atari_seven_eight_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_jaguar(self):
        request = requests.get(urls.consoles[Consoles.atari_jaguar])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_xe(self):
        request = requests.get(urls.consoles[Consoles.atari_xe])
        assert request.status_code == HTTPStatus.OK

    def test_reach_colecovision(self):
        request = requests.get(urls.consoles[Consoles.colecovision])
        assert request.status_code == HTTPStatus.OK

    def test_reach_dreamcast(self):
        request = requests.get(urls.consoles[Consoles.dreamcast])
        assert request.status_code == HTTPStatus.OK

    def test_reach_famicom_disk_system(self):
        request = requests.get(urls.consoles[Consoles.famicom_disk_system])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gamecube(self):
        request = requests.get(urls.consoles[Consoles.gamecube])
        assert request.status_code == HTTPStatus.OK

    def test_reach_genesis(self):
        request = requests.get(urls.consoles[Consoles.genesis])
        assert request.status_code == HTTPStatus.OK

    def test_reach_intellivision(self):
        request = requests.get(urls.consoles[Consoles.intellivision])
        assert request.status_code == HTTPStatus.OK

    def test_reach_jaguar_cd(self):
        request = requests.get(urls.consoles[Consoles.jaguar_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_cd(self):
        request = requests.get(urls.consoles[Consoles.neo_geo_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nes(self):
        request = requests.get(urls.consoles[Consoles.nes])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_sixty_four(self):
        request = requests.get(urls.consoles[Consoles.nintendo_sixty_four])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_switch(self):
        request = requests.get(urls.consoles[Consoles.nintendo_switch])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_wii(self):
        request = requests.get(urls.consoles[Consoles.nintendo_wii])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_wii_u(self):
        request = requests.get(urls.consoles[Consoles.nintendo_wii_u])
        assert request.status_code == HTTPStatus.OK

    def test_reach_odyssey_two(self):
        request = requests.get(urls.consoles[Consoles.odyssey_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_pc_fx(self):
        request = requests.get(urls.consoles[Consoles.pc_fx])
        assert request.status_code == HTTPStatus.OK

    def test_reach_philips_cdi(self):
        request = requests.get(urls.consoles[Consoles.philips_cdi])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_one(self):
        request = requests.get(urls.consoles[Consoles.playstation_one])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_two(self):
        request = requests.get(urls.consoles[Consoles.playstation_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_three(self):
        request = requests.get(urls.consoles[Consoles.playstation_three])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_four(self):
        request = requests.get(urls.consoles[Consoles.playstation_four])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_five(self):
        request = requests.get(urls.consoles[Consoles.playstation_five])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_thirty_two_x(self):
        request = requests.get(urls.consoles[Consoles.sega_thirty_two_x])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_cd(self):
        request = requests.get(urls.consoles[Consoles.sega_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_master_system(self):
        request = requests.get(urls.consoles[Consoles.sega_master_system])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_saturn(self):
        request = requests.get(urls.consoles[Consoles.sega_saturn])
        assert request.status_code == HTTPStatus.OK

    def test_reach_super_nintendo(self):
        request = requests.get(urls.consoles[Consoles.super_nintendo])
        assert request.status_code == HTTPStatus.OK

    def test_reach_turbografx_sixteen(self):
        request = requests.get(urls.consoles[Consoles.turbografx_sixteen])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox(self):
        request = requests.get(urls.consoles[Consoles.xbox])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_three_six_zero(self):
        request = requests.get(urls.consoles[Consoles.xbox_three_six_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_one(self):
        request = requests.get(urls.consoles[Consoles.xbox_one])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_series_x(self):
        request = requests.get(urls.consoles[Consoles.xbox_series_x])
        assert request.status_code == HTTPStatus.OK
