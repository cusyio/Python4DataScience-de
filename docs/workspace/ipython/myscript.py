# SPDX-FileCopyrightText: 2020 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause


def square(x):
    return x**2


for N in range(1, 4):
    print(N, "squared is", square(N))
