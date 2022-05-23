import logging
import requests

from http import HTTPStatus

from thecoverproject import Consoles, Handhelds, Computers, urls


test_logger = logging.getLogger(__name__)


class TestConsoles:

    def test_reach_three_do(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.three_do]}")
        request = requests.get(urls.consoles[Consoles.three_do])
        assert request.status_code == HTTPStatus.OK

    def test_reach_amiga_cd_thirty_two(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.amiga_cd_thirty_two]}")
        request = requests.get(urls.consoles[Consoles.amiga_cd_thirty_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_two_six_zero_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.atari_two_six_zero_zero]}")
        request = requests.get(urls.consoles[Consoles.atari_two_six_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_five_two_zero_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.atari_five_two_zero_zero]}")
        request = requests.get(urls.consoles[Consoles.atari_five_two_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_seven_eight_zero_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.atari_seven_eight_zero_zero]}")
        request = requests.get(urls.consoles[Consoles.atari_seven_eight_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_jaguar(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.atari_jaguar]}")
        request = requests.get(urls.consoles[Consoles.atari_jaguar])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_xe(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.atari_xe]}")
        request = requests.get(urls.consoles[Consoles.atari_xe])
        assert request.status_code == HTTPStatus.OK

    def test_reach_colecovision(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.colecovision]}")
        request = requests.get(urls.consoles[Consoles.colecovision])
        assert request.status_code == HTTPStatus.OK

    def test_reach_dreamcast(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.dreamcast]}")
        request = requests.get(urls.consoles[Consoles.dreamcast])
        assert request.status_code == HTTPStatus.OK

    def test_reach_famicom_disk_system(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.famicom_disk_system]}")
        request = requests.get(urls.consoles[Consoles.famicom_disk_system])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gamecube(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.gamecube]}")
        request = requests.get(urls.consoles[Consoles.gamecube])
        assert request.status_code == HTTPStatus.OK

    def test_reach_genesis(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.genesis]}")
        request = requests.get(urls.consoles[Consoles.genesis])
        assert request.status_code == HTTPStatus.OK

    def test_reach_intellivision(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.intellivision]}")
        request = requests.get(urls.consoles[Consoles.intellivision])
        assert request.status_code == HTTPStatus.OK

    def test_reach_jaguar_cd(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.jaguar_cd]}")
        request = requests.get(urls.consoles[Consoles.jaguar_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_cd(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.neo_geo_cd]}")
        request = requests.get(urls.consoles[Consoles.neo_geo_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nes(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.nes]}")
        request = requests.get(urls.consoles[Consoles.nes])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_sixty_four(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.nintendo_sixty_four]}")
        request = requests.get(urls.consoles[Consoles.nintendo_sixty_four])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_switch(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.nintendo_switch]}")
        request = requests.get(urls.consoles[Consoles.nintendo_switch])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_wii(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.nintendo_wii]}")
        request = requests.get(urls.consoles[Consoles.nintendo_wii])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_wii_u(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.nintendo_wii_u]}")
        request = requests.get(urls.consoles[Consoles.nintendo_wii_u])
        assert request.status_code == HTTPStatus.OK

    def test_reach_odyssey_two(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.odyssey_two]}")
        request = requests.get(urls.consoles[Consoles.odyssey_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_pc_fx(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.pc_fx]}")
        request = requests.get(urls.consoles[Consoles.pc_fx])
        assert request.status_code == HTTPStatus.OK

    def test_reach_philips_cdi(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.philips_cdi]}")
        request = requests.get(urls.consoles[Consoles.philips_cdi])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_one(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.playstation_one]}")
        request = requests.get(urls.consoles[Consoles.playstation_one])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_two(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.playstation_two]}")
        request = requests.get(urls.consoles[Consoles.playstation_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_three(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.playstation_three]}")
        request = requests.get(urls.consoles[Consoles.playstation_three])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_four(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.playstation_four]}")
        request = requests.get(urls.consoles[Consoles.playstation_four])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_five(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.playstation_five]}")
        request = requests.get(urls.consoles[Consoles.playstation_five])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_thirty_two_x(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.sega_thirty_two_x]}")
        request = requests.get(urls.consoles[Consoles.sega_thirty_two_x])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_cd(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.sega_cd]}")
        request = requests.get(urls.consoles[Consoles.sega_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_master_system(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.sega_master_system]}")
        request = requests.get(urls.consoles[Consoles.sega_master_system])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_saturn(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.sega_saturn]}")
        request = requests.get(urls.consoles[Consoles.sega_saturn])
        assert request.status_code == HTTPStatus.OK

    def test_reach_super_nintendo(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.super_nintendo]}")
        request = requests.get(urls.consoles[Consoles.super_nintendo])
        assert request.status_code == HTTPStatus.OK

    def test_reach_turbografx_sixteen(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.turbografx_sixteen]}")
        request = requests.get(urls.consoles[Consoles.turbografx_sixteen])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.xbox]}")
        request = requests.get(urls.consoles[Consoles.xbox])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_three_six_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.xbox_three_six_zero]}")
        request = requests.get(urls.consoles[Consoles.xbox_three_six_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_one(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.xbox_one]}")
        request = requests.get(urls.consoles[Consoles.xbox_one])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_series_x(self):
        test_logger.info(f"Trying to reach {urls.consoles[Consoles.xbox_series_x]}")
        request = requests.get(urls.consoles[Consoles.xbox_series_x])
        assert request.status_code == HTTPStatus.OK


class TestHandhelds:

    def test_reach_three_ds(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.three_ds]}")
        request = requests.get(urls.handhelds[Handhelds.three_ds])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_lynx(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.atari_lynx]}")
        request = requests.get(urls.handhelds[Handhelds.atari_lynx])
        assert request.status_code == HTTPStatus.OK

    def test_reach_game_gear(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.game_gear]}")
        request = requests.get(urls.handhelds[Handhelds.game_gear])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.gameboy]}")
        request = requests.get(urls.handhelds[Handhelds.gameboy])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_advance(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.gameboy_advance]}")
        request = requests.get(urls.handhelds[Handhelds.gameboy_advance])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_advance_video(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.gameboy_advance_video]}")
        request = requests.get(urls.handhelds[Handhelds.gameboy_advance_video])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_color(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.gameboy_color]}")
        request = requests.get(urls.handhelds[Handhelds.gameboy_color])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_pocket(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.neo_geo_pocket]}")
        request = requests.get(urls.handhelds[Handhelds.neo_geo_pocket])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_pocket_color(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.neo_geo_pocket_color]}")
        request = requests.get(urls.handhelds[Handhelds.neo_geo_pocket_color])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_ds(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.nintendo_ds]}")
        request = requests.get(urls.handhelds[Handhelds.nintendo_ds])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_portable(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.playstation_portable]}")
        request = requests.get(urls.handhelds[Handhelds.playstation_portable])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_portable_video(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.playstation_portable_video]}")
        request = requests.get(urls.handhelds[Handhelds.playstation_portable_video])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_vita(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.playstation_vita]}")
        request = requests.get(urls.handhelds[Handhelds.playstation_vita])
        assert request.status_code == HTTPStatus.OK

    def test_reach_virtual_boy(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.virtual_boy]}")
        request = requests.get(urls.handhelds[Handhelds.virtual_boy])
        assert request.status_code == HTTPStatus.OK

    def test_reach_wonderswan(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.wonderswan]}")
        request = requests.get(urls.handhelds[Handhelds.wonderswan])
        assert request.status_code == HTTPStatus.OK

    def test_reach_wonderswan_color(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handhelds.wonderswan_color]}")
        request = requests.get(urls.handhelds[Handhelds.wonderswan_color])
        assert request.status_code == HTTPStatus.OK


class TestComputers:

    def test_reach_amiga(self):
        test_logger.info(f"Trying to reach {urls.computers[Computers.amiga]}")
        request = requests.get(urls.computers[Computers.amiga])
        assert request.status_code == HTTPStatus.OK

    def test_reach_linux(self):
        test_logger.info(f"Trying to reach {urls.computers[Computers.linux]}")
        request = requests.get(urls.computers[Computers.linux])
        assert request.status_code == HTTPStatus.OK

    def test_reach_mac(self):
        test_logger.info(f"Trying to reach {urls.computers[Computers.mac]}")
        request = requests.get(urls.computers[Computers.mac])
        assert request.status_code == HTTPStatus.OK

    def test_reach_ms_dos(self):
        test_logger.info(f"Trying to reach {urls.computers[Computers.ms_dos]}")
        request = requests.get(urls.computers[Computers.ms_dos])
        assert request.status_code == HTTPStatus.OK

    def test_reach_windows(self):
        test_logger.info(f"Trying to reach {urls.computers[Computers.windows]}")
        request = requests.get(urls.computers[Computers.windows])
        assert request.status_code == HTTPStatus.OK
