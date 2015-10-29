# Copyright (c) 2013-2015 by Ron Frederick <ronf@timeheart.net>.
# All rights reserved.
#
# This program and the accompanying materials are made available under
# the terms of the Eclipse Public License v1.0 which accompanies this
# distribution and is available at:
#
#     http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#     Ron Frederick - initial implementation, API, and documentation

"""Elliptic curve public key utility functions"""

_curve_param_map = {}

# Short variable names are used here, matching names in the spec
# pylint: disable=invalid-name


def register_prime_curve(curve_id, p, a, b, point, n):
    """Register an elliptic curve prime domain

       This function registers an elliptic curve prime domain by
       specifying the SSH identifier for the curve, the OID used to
       identify the curve in PKCS#1 and PKCS#8 private and public keys,
       and the set of parameters describing the curve, generator point,
       and order.

    """

    _curve_param_map[p, a % p, b % p, point, n] = curve_id


def lookup_ec_curve_by_params(p, a, b, point, n):
    """Look up an elliptic curve by its parameters

       This function looks up an elliptic curve by its parameters
       and returns the curve's name.

    """

    try:
        return _curve_param_map[p, a % p, b % p, point, n]
    except (KeyError, ValueError):
        raise ValueError('Unknown elliptic curve parameters')


# pylint: disable=line-too-long

register_prime_curve(b'nistp521',
                     6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,
                     -3,
                     1093849038073734274511112390766805569936207598951683748994586394495953116150735016013708737573759623248592132296706313309438452531591012912142327488478985984,
                     b'\x04\x00\xc6\x85\x8e\x06\xb7\x04\x04\xe9\xcd\x9e>\xcbf#\x95\xb4B\x9cd\x819\x05?\xb5!\xf8(\xaf`kM=\xba\xa1K^w\xef\xe7Y(\xfe\x1d\xc1\'\xa2\xff\xa8\xde3H\xb3\xc1\x85jB\x9b\xf9~~1\xc2\xe5\xbdf\x01\x189)jx\x9a;\xc0\x04\\\x8a_\xb4,}\x1b\xd9\x98\xf5DIW\x9bDh\x17\xaf\xbd\x17\'>f,\x97\xeer\x99^\xf4&@\xc5P\xb9\x01?\xad\x07a5<p\x86\xa2r\xc2@\x88\xbe\x94v\x9f\xd1fP',
                     6864797660130609714981900799081393217269435300143305409394463459185543183397655394245057746333217197532963996371363321113864768612440380340372808892707005449)

register_prime_curve(b'nistp384',
                     39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319,
                     -3,
                     27580193559959705877849011840389048093056905856361568521428707301988689241309860865136260764883745107765439761230575,
                     b'\x04\xaa\x87\xca"\xbe\x8b\x057\x8e\xb1\xc7\x1e\xf3 \xadtn\x1d;b\x8b\xa7\x9b\x98Y\xf7A\xe0\x82T*8U\x02\xf2]\xbfU)l:T^8rv\n\xb76\x17\xdeJ\x96&,o]\x9e\x98\xbf\x92\x92\xdc)\xf8\xf4\x1d\xbd(\x9a\x14|\xe9\xda1\x13\xb5\xf0\xb8\xc0\n`\xb1\xce\x1d~\x81\x9dzC\x1d|\x90\xea\x0e_',
                     39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643)

register_prime_curve(b'nistp256',
                     115792089210356248762697446949407573530086143415290314195533631308867097853951,
                     -3,
                     41058363725152142129326129780047268409114441015993725554835256314039467401291,
                     b'\x04k\x17\xd1\xf2\xe1,BG\xf8\xbc\xe6\xe5c\xa4@\xf2w\x03}\x81-\xeb3\xa0\xf4\xa19E\xd8\x98\xc2\x96O\xe3B\xe2\xfe\x1a\x7f\x9b\x8e\xe7\xebJ|\x0f\x9e\x16+\xce3Wk1^\xce\xcb\xb6@h7\xbfQ\xf5',
                     115792089210356248762697446949407573529996955224135760342422259061068512044369)
