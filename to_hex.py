def str_to_hex_list(str):
    source = ["".join(["0x", x]) for x in str.split(" ")]
    #source.extend(["0x00"] * (length_command - len(source)))
    return source

def list_to_int(list_hex):
    return [int(i, 16) for i in list_hex]

if __name__ == '__main__':
    import re

    RAW_DATA = "raw.data"
    HEX_DATA = "hex.data"

    data = []
    with open(HEX_DATA, "r") as f:
        for s in f:
            source = str_to_hex_list(s[:-1])
            data.append(list_to_int(source))

    raw = []
    with open(RAW_DATA, "r") as f:
        for s in f:
            if ("f0" in s) and ("f2" in s):
                cmd_hex = "02"
                cmd_hex += s[s.find("f0"):s.find("f2")+2]
                cmd_hex = " ".join(re.findall('..', cmd_hex.replace(" ", "")))
                raw.append(cmd_hex)
                continue
            elif "f0" in s:
                cmd_hex = "02"
                cmd_hex += s[s.find("f0"):-1]
                continue
            elif "f2" in s:
                cmd_hex += s[:s.find("f2") + 2]
                cmd_hex = " ".join(re.findall('..', cmd_hex.replace(" ", "")))
                raw.append(cmd_hex)

    with open(HEX_DATA, "w") as f:
        for s in raw:
            f.write(s)
            f.write("\n")