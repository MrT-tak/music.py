#Music.py © 2024 by Takumi Fujiyama(MrT) is licensed under CC BY-ND 4.0 and with rightfulUseTerms

import pygame, logging, time, sys

MUSIC_MODULE_VERSION = "1.0.0"
logger = logging.getLogger("Music.py-{0}-{1}".format(MUSIC_MODULE_VERSION, __name__))

print("\n")
print("Music.py: Thank you for installing Music.py by MrT")
print("\n")
#print("Music.py: Legal disclaimer: The music played using this software is not owned by the creator of this plugin. Any copyright issue arised from playing music from ths software: the owner this plugin will not be responsible for misuse.")
#print("\n")


def music(music_file, ext, volume=100, loop=False, loopAmnt=0, isReplit=True):
  logger.info("Music.py: preparing to load audio...")
  logger.debug("Music.py: config:")
  logger.debug("Music.py:       NAME      | Ext | Volume | Loop | LoopAmnt")
  logger.debug("Music.py: " + str(music_file) + " | " + str(ext) + " | " + str(volume) + " | " + str(loop) + " | " + str(loopAmnt))
  logger.debug("Music.py: calculating volume")
  act_volume = volume / 100

  logger.info("Music.py: determing file path..")
  music_file_wExt = "./Musics/" + music_file + ext

  logger.info("Music.py: loading music file...")
  while True:
    try:
      if (isReplit == True):
        import replit
        audio = replit.audio.play_file(music_file_wExt, act_volume, loop,loopAmnt)
      elif (isReplit == False):
        # ! Pygame mixer dosen't work IN REPLIT
        audio = pygame.mixer.music.load(music_file_wExt, ext)
        pygame.mixer.music.play()
      else:
        try:
          audio = replit.audio.play_file(music_file_wExt, act_volume, loop,loopAmnt)
        except:
          try:
            audio = pygame.mixer.music.load(music_file, ext)
          except Exception as e:
            logger.critical(
              'Music.py: No possible way to load music file. Attempted Replit and pygame. Error: ' + str(e)
            )
            raise ValueError(
                'Music.py: No possible way to load music file. Attempted Replit and pygame. Error: '
                + str(e))
            break

    except Exception as e:
      logger.warning(e)
      logger.warning("Music.py: Error handler: ERROR: " + str(e))
      logger.info("Music.py: failed, trying again...")
      continue
    break

  logger.info("Music.py: music loaded!")
  logger.info("Music.py: Audio returning... closing...")
  return audio
