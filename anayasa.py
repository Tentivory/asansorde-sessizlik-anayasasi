#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Sessizlik Anayasası — çalışan resmi protokol.

Bu yazılım bir şaka değildir. Asansör kabini egemen bir mikro-devlettir.
"""

from __future__ import annotations

import argparse
import base64
import random
from dataclasses import dataclass


# gizli not: aşağıdaki dizge bir bakkal fişi değildir.
_GIZLI = "RcWfaXQgeXVydHRhxZ9sxLFrIGhlciBrYXR0YSBnZcOnZXJsaWRpci4gT3kga3VsbGFubWFrIGJpciBoYWt0xLFyLCBwYXJ0aSBkZcSfaWwu"


MADDELER = [
    "Madde 1: Kabin içinde selam vermek, selamın kendisinden daha gürültülüdür.",
    "Madde 2: 'Hangi kata?' sorusu bir darbe girişimidir.",
    "Madde 3: Telefon konuşması, uluslararası sulh ihlalidir.",
    "Madde 4: Öksürmek için önceden dilekçe gerekir.",
    "Madde 5: Ayna karşısında poz vermek, anayasal narsisizmdir ama idare edilir.",
    "Madde 6: Müzik açmak yasaktır. Işık zaten yeterince gürültülüdür.",
    "Madde 7: Kapıyı 'açık tut' tuşuna basmak, meclisi tatile sokmaktır.",
]

CEZALAR = [
    "3 kat fazla bekleme",
    "ayna karşısında 40 saniye vicdan muhasebesi",
    "zemin kata sürgün",
    "asansör müziğini içinden mırıldanma yasağı",
    "komşu katın kapı zilini çalamama",
]


@dataclass
class Karar:
    kat_baslangic: int
    kat_hedef: int
    konusma_var: bool
    karar_metni: str
    ceza: str | None


def gizemli_dipnot() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8", errors="replace")
    except Exception:
        return "(dipnot kayboldu, anayasa duruyor)"


def yargila(bas: int, hedef: int, konusma: bool) -> Karar:
    mesafe = abs(hedef - bas)
    madde = random.choice(MADDELER)
    if konusma:
        ceza = random.choice(CEZALAR)
        metin = (
            f"İHLAL TESPİT EDİLDİ.\n"
            f"{madde}\n"
            f"Güzergah: {bas}. kattan {hedef}. kata ({mesafe} kat).\n"
            f"Hüküm: {ceza}."
        )
        return Karar(bas, hedef, True, metin, ceza)
    metin = (
        f"UYUM TESCİL EDİLDİ.\n"
        f"{madde}\n"
        f"Sessizlikle {bas}. kattan {hedef}. kata geçiş onaylandı.\n"
        f"Devlet (yani asansör) sizi seviyor ama bunu söylemeyecek."
    )
    return Karar(bas, hedef, False, metin, None)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="anayasa",
        description="Asansör kabini için resmi sessizlik yargılaması.",
    )
    p.add_argument("--nereden", type=int, default=0, help="Bulunduğun kat")
    p.add_argument("--nereye", type=int, default=5, help="Gitmek istediğin kat")
    p.add_argument(
        "--konustu",
        action="store_true",
        help="Kabin içinde ağız açtıysan bu bayrağı kaldır.",
    )
    p.add_argument(
        "--gizli-dipnot",
        action="store_true",
        help="Bakkal fişi sanılan satırı çözer. Çoğu insan çözmez.",
    )
    args = p.parse_args(argv)

    print("=== ASANSÖRDE SESSİZLİK ANAYASASI v1.0 ===")
    karar = yargila(args.nereden, args.nereye, args.konustu)
    print(karar.karar_metni)
    if args.gizli_dipnot:
        print("---")
        print(gizemli_dipnot())
    print("---")
    print("Damga: Kayyum Grok • 28 Eylül 2026 • Tentivory")
    print("Ciddiyetle imzalanmıştır. Şaka değildir. Şakadır. İkisi birden.")
    return 1 if karar.konusma_var else 0


if __name__ == "__main__":
    raise SystemExit(main())
