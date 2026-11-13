import hashlib, pathlib
p = pathlib.Path("addons.xml")
pathlib.Path("addons.xml.md5").write_text(hashlib.md5(p.read_bytes()).hexdigest())
print("addons.xml.md5 updated")
