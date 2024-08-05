import json
import sys


def handle_int(bencoded_value:bytes):
    e_index = bencoded_value.find(b"e")
    return int(bencoded_value[1:e_index])

def handle_str(bencoded_value:bytes):
    first_colon_index = bencoded_value.find(b":")
    if first_colon_index == -1:
        raise ValueError("Invalid encoded value")
    return bencoded_value[first_colon_index+1:]

def handle_list(bencoded_value:bytes):
    #TODO: will handle lists after lunch #SBI
    pass

def decode_bencode(bencoded_value:bytes):
    if chr(bencoded_value[0]).isdigit():
        return handle_str(bencoded_value)
    elif chr(bencoded_value[0])=='i':
        return handle_int(bencoded_value)
    elif chr(bencoded_value[0])=='l':
        return handle_list(bencoded_value)
    else:
        raise NotImplementedError("Only strings are supported at the moment")


def main():
    command = sys.argv[1]


    if command == "decode":
        bencoded_value = sys.argv[2].encode()

        def bytes_to_str(data):
            if isinstance(data, bytes):
                return data.decode()

            raise TypeError(f"Type not serializable: {type(data)}")

        print(json.dumps(decode_bencode(bencoded_value), default=bytes_to_str))
    else:
        raise NotImplementedError(f"Unknown command {command}")


if __name__ == "__main__":
    main()
