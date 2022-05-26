import logging
import requests

from http import HTTPStatus

from thecoverproject import Console, Handheld, Computer, urls


test_logger = logging.getLogger(__name__)


class TestConsoles:

    def test_reach_three_do(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.three_do]}")
        request = requests.get(urls.consoles[Console.three_do])
        assert request.status_code == HTTPStatus.OK

    def test_reach_amiga_cd_thirty_two(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.amiga_cd_thirty_two]}")
        request = requests.get(urls.consoles[Console.amiga_cd_thirty_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_two_six_zero_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.atari_two_six_zero_zero]}")
        request = requests.get(urls.consoles[Console.atari_two_six_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_five_two_zero_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.atari_five_two_zero_zero]}")
        request = requests.get(urls.consoles[Console.atari_five_two_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_seven_eight_zero_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.atari_seven_eight_zero_zero]}")
        request = requests.get(urls.consoles[Console.atari_seven_eight_zero_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_jaguar(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.atari_jaguar]}")
        request = requests.get(urls.consoles[Console.atari_jaguar])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_xe(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.atari_xe]}")
        request = requests.get(urls.consoles[Console.atari_xe])
        assert request.status_code == HTTPStatus.OK

    def test_reach_colecovision(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.colecovision]}")
        request = requests.get(urls.consoles[Console.colecovision])
        assert request.status_code == HTTPStatus.OK

    def test_reach_dreamcast(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.dreamcast]}")
        request = requests.get(urls.consoles[Console.dreamcast])
        assert request.status_code == HTTPStatus.OK

    def test_reach_famicom_disk_system(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.famicom_disk_system]}")
        request = requests.get(urls.consoles[Console.famicom_disk_system])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gamecube(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.gamecube]}")
        request = requests.get(urls.consoles[Console.gamecube])
        assert request.status_code == HTTPStatus.OK

    def test_reach_genesis(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.genesis]}")
        request = requests.get(urls.consoles[Console.genesis])
        assert request.status_code == HTTPStatus.OK

    def test_reach_intellivision(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.intellivision]}")
        request = requests.get(urls.consoles[Console.intellivision])
        assert request.status_code == HTTPStatus.OK

    def test_reach_jaguar_cd(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.jaguar_cd]}")
        request = requests.get(urls.consoles[Console.jaguar_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_cd(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.neo_geo_cd]}")
        request = requests.get(urls.consoles[Console.neo_geo_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nes(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.nes]}")
        request = requests.get(urls.consoles[Console.nes])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_sixty_four(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.nintendo_sixty_four]}")
        request = requests.get(urls.consoles[Console.nintendo_sixty_four])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_switch(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.nintendo_switch]}")
        request = requests.get(urls.consoles[Console.nintendo_switch])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_wii(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.nintendo_wii]}")
        request = requests.get(urls.consoles[Console.nintendo_wii])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_wii_u(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.nintendo_wii_u]}")
        request = requests.get(urls.consoles[Console.nintendo_wii_u])
        assert request.status_code == HTTPStatus.OK

    def test_reach_odyssey_two(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.odyssey_two]}")
        request = requests.get(urls.consoles[Console.odyssey_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_pc_fx(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.pc_fx]}")
        request = requests.get(urls.consoles[Console.pc_fx])
        assert request.status_code == HTTPStatus.OK

    def test_reach_philips_cdi(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.philips_cdi]}")
        request = requests.get(urls.consoles[Console.philips_cdi])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_one(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.playstation_one]}")
        request = requests.get(urls.consoles[Console.playstation_one])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_two(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.playstation_two]}")
        request = requests.get(urls.consoles[Console.playstation_two])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_three(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.playstation_three]}")
        request = requests.get(urls.consoles[Console.playstation_three])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_four(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.playstation_four]}")
        request = requests.get(urls.consoles[Console.playstation_four])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_five(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.playstation_five]}")
        request = requests.get(urls.consoles[Console.playstation_five])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_thirty_two_x(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.sega_thirty_two_x]}")
        request = requests.get(urls.consoles[Console.sega_thirty_two_x])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_cd(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.sega_cd]}")
        request = requests.get(urls.consoles[Console.sega_cd])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_master_system(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.sega_master_system]}")
        request = requests.get(urls.consoles[Console.sega_master_system])
        assert request.status_code == HTTPStatus.OK

    def test_reach_sega_saturn(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.sega_saturn]}")
        request = requests.get(urls.consoles[Console.sega_saturn])
        assert request.status_code == HTTPStatus.OK

    def test_reach_super_nintendo(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.super_nintendo]}")
        request = requests.get(urls.consoles[Console.super_nintendo])
        assert request.status_code == HTTPStatus.OK

    def test_reach_turbografx_sixteen(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.turbografx_sixteen]}")
        request = requests.get(urls.consoles[Console.turbografx_sixteen])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.xbox]}")
        request = requests.get(urls.consoles[Console.xbox])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_three_six_zero(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.xbox_three_six_zero]}")
        request = requests.get(urls.consoles[Console.xbox_three_six_zero])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_one(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.xbox_one]}")
        request = requests.get(urls.consoles[Console.xbox_one])
        assert request.status_code == HTTPStatus.OK

    def test_reach_xbox_series_x(self):
        test_logger.info(f"Trying to reach {urls.consoles[Console.xbox_series_x]}")
        request = requests.get(urls.consoles[Console.xbox_series_x])
        assert request.status_code == HTTPStatus.OK


class TestHandhelds:

    def test_reach_three_ds(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.three_ds]}")
        request = requests.get(urls.handhelds[Handheld.three_ds])
        assert request.status_code == HTTPStatus.OK

    def test_reach_atari_lynx(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.atari_lynx]}")
        request = requests.get(urls.handhelds[Handheld.atari_lynx])
        assert request.status_code == HTTPStatus.OK

    def test_reach_game_gear(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.game_gear]}")
        request = requests.get(urls.handhelds[Handheld.game_gear])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.gameboy]}")
        request = requests.get(urls.handhelds[Handheld.gameboy])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_advance(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.gameboy_advance]}")
        request = requests.get(urls.handhelds[Handheld.gameboy_advance])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_advance_video(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.gameboy_advance_video]}")
        request = requests.get(urls.handhelds[Handheld.gameboy_advance_video])
        assert request.status_code == HTTPStatus.OK

    def test_reach_gameboy_color(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.gameboy_color]}")
        request = requests.get(urls.handhelds[Handheld.gameboy_color])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_pocket(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.neo_geo_pocket]}")
        request = requests.get(urls.handhelds[Handheld.neo_geo_pocket])
        assert request.status_code == HTTPStatus.OK

    def test_reach_neo_geo_pocket_color(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.neo_geo_pocket_color]}")
        request = requests.get(urls.handhelds[Handheld.neo_geo_pocket_color])
        assert request.status_code == HTTPStatus.OK

    def test_reach_nintendo_ds(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.nintendo_ds]}")
        request = requests.get(urls.handhelds[Handheld.nintendo_ds])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_portable(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.playstation_portable]}")
        request = requests.get(urls.handhelds[Handheld.playstation_portable])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_portable_video(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.playstation_portable_video]}")
        request = requests.get(urls.handhelds[Handheld.playstation_portable_video])
        assert request.status_code == HTTPStatus.OK

    def test_reach_playstation_vita(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.playstation_vita]}")
        request = requests.get(urls.handhelds[Handheld.playstation_vita])
        assert request.status_code == HTTPStatus.OK

    def test_reach_virtual_boy(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.virtual_boy]}")
        request = requests.get(urls.handhelds[Handheld.virtual_boy])
        assert request.status_code == HTTPStatus.OK

    def test_reach_wonderswan(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.wonderswan]}")
        request = requests.get(urls.handhelds[Handheld.wonderswan])
        assert request.status_code == HTTPStatus.OK

    def test_reach_wonderswan_color(self):
        test_logger.info(f"Trying to reach {urls.handhelds[Handheld.wonderswan_color]}")
        request = requests.get(urls.handhelds[Handheld.wonderswan_color])
        assert request.status_code == HTTPStatus.OK


class TestComputers:

    def test_reach_amiga(self):
        test_logger.info(f"Trying to reach {urls.computers[Computer.amiga]}")
        request = requests.get(urls.computers[Computer.amiga])
        assert request.status_code == HTTPStatus.OK

    def test_reach_linux(self):
        test_logger.info(f"Trying to reach {urls.computers[Computer.linux]}")
        request = requests.get(urls.computers[Computer.linux])
        assert request.status_code == HTTPStatus.OK

    def test_reach_mac(self):
        test_logger.info(f"Trying to reach {urls.computers[Computer.mac]}")
        request = requests.get(urls.computers[Computer.mac])
        assert request.status_code == HTTPStatus.OK

    def test_reach_ms_dos(self):
        test_logger.info(f"Trying to reach {urls.computers[Computer.ms_dos]}")
        request = requests.get(urls.computers[Computer.ms_dos])
        assert request.status_code == HTTPStatus.OK

    def test_reach_windows(self):
        test_logger.info(f"Trying to reach {urls.computers[Computer.windows]}")
        request = requests.get(urls.computers[Computer.windows])
        assert request.status_code == HTTPStatus.OK
