# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports
#+---------------------------------------------------------------------------+
from locale import gettext as _
import logging
from ASAPClusteringConfigurationView import ASAPClusteringConfigurationView

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+


class ASAPClusteringConfigurationController(object):
    """Controller for the configuration of the ASAP Clustering process"""

    def __init__(self, ASAPClustering):
        self.ASAPClustering = ASAPClustering
        self.log = logging.getLogger(__name__)
        self._view = ASAPClusteringConfigurationView(self)

    @property
    def view(self):
        return self._view

    def getAlgorithm(self):
        return self.ASAPClustering

    def clusteringThresholdAdjustment_value_changed_cb(self, widget):
        try:
            value = float(widget.get_value())
        except Exception, e:
            self.log.warn("Invalid Clustering threshold ({0}))".format(e))
            value = None
        self.ASAPClustering.setClusteringThreshold(value)

    def run(self, attachedView):
        self._view.run(attachedView)

    def destroy(self):
        self._view.destroy()