# Encoded By PyEncryptor
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob

import marshal, base64, zlib

exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))