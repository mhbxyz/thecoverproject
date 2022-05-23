import requests

from http import HTTPStatus

from thecoverproject import Consoles, Handhelds, Computers, urls


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


class TestHandhelds:

    def test_reach_three_ds(self):
        request = requests.get(urls.handhelds[Handhelds.three_ds])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_lynx(self):
        request = requests.get(urls.handhelds[Handhelds.atari_lynx])
        assert request.status_code == HTTPStatus.OK

    def test_reach_game_gear(self):
        request = requests.get(urls.handhelds[Handhelds.game_gear])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy(self):
        request = requests.get(urls.handhelds[Handhelds.gameboy])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_advance(self):
        request = requests.get(urls.handhelds[Handhelds.gameboy_advance])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_advance_video(self):
        request = requests.get(urls.handhelds[Handhelds.gameboy_advance_video])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_color(self):
        request = requests.get(urls.handhelds[Handhelds.gameboy_color])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_pocket(self):
        request = requests.get(urls.handhelds[Handhelds.neo_geo_pocket])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_pocket_color(self):
        request = requests.get(urls.handhelds[Handhelds.neo_geo_pocket_color])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_ds(self):
        request = requests.get(urls.handhelds[Handhelds.nintendo_ds])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_portable(self):
        request = requests.get(urls.handhelds[Handhelds.playstation_portable])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_portable_video(self):
        request = requests.get(urls.handhelds[Handhelds.playstation_portable_video])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_vita(self):
        request = requests.get(urls.handhelds[Handhelds.playstation_vita])
        assert request.status_code == HTTPStatus.OK

    def test_reach_virtual_boy(self):
        request = requests.get(urls.handhelds[Handhelds.virtual_boy])
        assert request.status_code == HTTPStatus.OK

    def test_reach_wonderswan(self):
        request = requests.get(urls.handhelds[Handhelds.wonderswan])
        assert request.status_code == HTTPStatus.OK

    def test_reach_wonderswan_color(self):
        request = requests.get(urls.handhelds[Handhelds.wonderswan_color])
        assert request.status_code == HTTPStatus.OK


class TestComputers:

    def test_reach_amiga(self):
        request = requests.get(urls.computers[Computers.amiga])
        assert request.status_code == HTTPStatus.OK

    def test_reach_linux(self):
        request = requests.get(urls.computers[Computers.linux])
        assert request.status_code == HTTPStatus.OK

    def test_reach_mac(self):
        request = requests.get(urls.computers[Computers.mac])
        assert request.status_code == HTTPStatus.OK

    def test_reach_ms_dos(self):
        request = requests.get(urls.computers[Computers.ms_dos])
        assert request.status_code == HTTPStatus.OK

    def test_reach_windows(self):
        request = requests.get(urls.computers[Computers.windows])
        assert request.status_code == HTTPStatus.OK
