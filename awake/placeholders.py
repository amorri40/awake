# This file is part of Awake - GB decompiler.
# Copyright (C) 2012  Wojciech Marczenko (devdri) <wojtek.marczenko@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from awake import address
from awake.operand import Constant, Condition, Dereference, Register

BC = Register("BC_16bit_Register")
DE = Register("DE_16bit_Register")
HL = Register("HL_16bit_Register")
SP = Register("SP_16bit_Register")
AF = Register("AF_16bit_Register")

B = Register("B_8bit_Register")
C = Register("C_8bit_Register")
D = Register("D_8bit_Register")
E = Register("E_8bit_Register")
H = Register("H_8bit_Register")
L = Register("L_8bit_Register")
A = Register("A_8bit_Register")
deref_HL = Dereference(HL, address.fromVirtual(0))  # XXX: TODO: very very bad

FNZ = Condition("FNZ")
FZ = Condition("FZ")
FNC = Condition("FNC")
FC = Condition("FC")
ALWAYS = Condition("ALWAYS")

ROMBANK = Register('ROMBANK')

tab = dict(
    R=[BC, DE, HL, SP],
    Q=[BC, DE, HL, AF],
    S=[B, C, D, E, H, L, deref_HL, A],
    Z=[B, C, D, E, H, L, deref_HL, A],
    F=[FNZ, FZ, FNC, FC],
)

def get(name, value):
    if name in tab:
        return tab[name][value]
    elif name == "N":
        return Constant(value * 0x08)
    elif name == "I":
        return Constant(value)

