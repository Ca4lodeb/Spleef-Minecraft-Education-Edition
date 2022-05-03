# Spleef-Minecraft-Education-Edition

def on_on_chat(spleef):
    blocks.fill(LAVA,
        pos(24, -1, 24),
        pos(spleef, -1, spleef),
        FillOperation.REPLACE)
    blocks.fill(SNOW,
        pos(24, 4, 24),
        pos(spleef, 4, spleef),
        FillOperation.REPLACE)
    mobs.teleport_to_position(mobs.target(ALL_PLAYERS), pos(spleef / 2, 5, spleef / 2))
    gameplay.set_game_mode(SURVIVAL, mobs.target(ALL_PLAYERS))
player.on_chat("Start Spleef" or "Start spleef" or "start spleef" or "start Spleef", on_on_chat)
