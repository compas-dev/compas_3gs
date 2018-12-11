from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


__author__     = ['Juney Lee']
__copyright__  = 'Copyright 2018, BLOCK Research Group - ETH Zurich'
__license__    = 'MIT License'
__email__      = 'juney.lee@arch.ethz.ch'


__all__ = [
    'pair_hf_to_uv',
    'pair_uv_to_hf'
]


def pair_hf_to_uv(volmesh, network):
    """Pairs the directed halffaces of a volmesh to the corresponding edge (u, v) of the dual network.

    Parameters
    ----------
    volmesh : VolMesh
        A volmesh object representing a polyhedral force diagram.
    network : Network
        A network object representing a polyhedral form diagram.

    Returns
    -------
    dictionary
        A dictionary of u_hfkey-(u, v) pairs.

    Notes
    -----
    u_hfkey is an interior halfface of the volmesh that belongs to volmesh.cell[u], which points to volmesh.cell[v]. In another words, its pair (or opposite) halfface belongs to volmesh.cell[v].

    """
    pair_dict = {}

    for u, v in network.edges():
        u_hfkey, v_hfkey = volmesh.cell_pair_hfkeys(u, v)
        pair_dict[u_hfkey] = (u, v)

    return pair_dict


def pair_uv_to_hf(volmesh, network):
    """Pairs the directed edges (u, v) of a network to the corresponding halffaces of the dual volmesh.

    Parameters
    ----------
    volmesh : VolMesh
        A volmesh object representing a polyhedral force diagram.
    network : Network
        A network object representing a polyhedral form diagram.

    Returns
    -------
    dictionary
        A dictionary of (u, v)-u_hfkey pairs.

    """

    hf_uv_dict = pair_hf_to_uv(volmesh, network)
    uv_hf_dict = dict((uv, hfkey) for hfkey, uv in hf_uv_dict.items())

    return uv_hf_dict