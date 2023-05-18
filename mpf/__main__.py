"""Command dispatcher of the Mission Pinball Framework."""
import sys
import mpf.commands.game

"""Added all of the dynamic imports that mc_demo needs to start, so that PyInstaller will package them naturally."""
"""The empty lines/groups here are related to the order I got errors - so a log of what loads at what time."""
import mpf.devices.dual_wound_coil
import mpf.devices.shot_profile
import mpf.devices.score_reel
import mpf.devices.score_reel_group
import mpf.devices.playfield_transfer
import mpf.devices.digital_score_reel
import mpf.devices.light_group
import mpf.devices.kickback
import mpf.devices.timed_switch
import mpf.devices.power_supply_unit
import mpf.devices.timer
import mpf.devices.sequence_shot
import mpf.devices.hardware_sound_system
import mpf.devices.ball_routing
import mpf.devices.show_queue

import mpf.platforms.driver_light_platform

import mpf.config_players.coil_player
import mpf.config_players.event_player
import mpf.config_players.block_event_player
import mpf.config_players.queue_event_player
import mpf.config_players.queue_relay_player
import mpf.config_players.flasher_player
import mpf.config_players.light_player
import mpf.config_players.random_event_player
import mpf.config_players.variable_player
import mpf.config_players.segment_display_player
import mpf.config_players.hardware_sound_player
import mpf.config_players.score_queue_player
import mpf.config_players.blinkenlight_player

import mpf.modes.attract.code.attract

import mpf.core.bcp.bcp_socket_client

import mpf.plugins.info_lights;
import mpf.plugins.switch_player;
import mpf.plugins.twitch_bot;

def main(args=None):
    """Dispatche commands to our handlers."""
    if args is None:
        args = sys.argv[1:]

    """For now bypassing commands handler and just always running game."""
    """Not sure yet if the ideal deployment would have a separate EXE for MP and MPF MC or just all in one."""
    """All in one is more fool-proof and predictable and avoids unsupported version combinations."""
    mpf.commands.game.Command('', '', args)

if __name__ == "__main__":
    main()
