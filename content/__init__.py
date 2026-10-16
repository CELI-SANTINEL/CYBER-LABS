# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("06b1361cc85cc90d76f585ce0173e877b86a694605dc23e9f7a6e7d8bf6c0d53f19c0a9e6a687d7cbdfa323c9d0eeb64ef41cd845d58e5b6440fed74e99ebdf7")
_K2 = bytes.fromhex("c0f3431e56ff8e83f0685627d456975b371263031571e99eff97d3f50a927d0f1bf99dfac59ec336e67ff3e94936cd0092637c177e69ca4b91e66094f95ba816")
_K3 = bytes.fromhex("2ae71c55b74e9e827407e548b59347fccf253bd99be1c894416c2c7d1f38fcac6a003a1564361028bb00403bc656ec8cec8fd61b6d6c0f6eb6f903088f55537b")
_S = """lz$>IY425B2&pYG2-YyN5If=ce;3QMP0!$5IDbi#6Z$zPkz6u5av$TFnXT;Kt_V}FoAaoa$*mUs*X$(x
h`~iQD__~VtBRo"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)
