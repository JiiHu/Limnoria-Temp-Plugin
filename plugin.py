###
# Copyright (c) 2014, Jiihu
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import os
import subprocess

try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Temp')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x




def haeLampoMittarilta( id ):
    p = subprocess.Popen(["cat", "/sys/bus/w1/devices/"+id+"/w1_slave"], stdout=subprocess.PIPE)

    output, err = p.communicate()

    output1, output2 = output.split('t=')
    output2 = int(output2) / 100
    output2 = float(output2) / 10

    return output2


def haeLampo( parametri ):
  temp = -100
  while (temp < -10) or (temp > 30):
      try:
          temp = haeLampoMittarilta( parametri )
      except:
          pass

        return str(temp)


class Temp(callbacks.Plugin):
    threaded = True

    def temp(self, irc, msg, args):

      reply = 'Fridge: ' + haeLampo("28-00044315c1ff") + 'c'
      #reply = reply + 'Bedroom: ' + haeLampo("28-000005826db9") + 'c, '
      #reply = reply + 'Out: ' + haeLampo("28-000005e39598") + 'c'

      irc.reply(reply)

      temp = wrap(temp)

Class = Temp

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
