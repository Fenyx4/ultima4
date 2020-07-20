import zlib
import struct
import array


def output_chunk(out, chunk_type, data):
    out.write(struct.pack("!I", len(data)))
    out.write(bytes(chunk_type, 'utf-8'))
    out.write(data)
    checksum = zlib.crc32(data, zlib.crc32(bytes(chunk_type, 'utf-8')))
    out.write(struct.pack("!I", checksum))


def get_data(width, height, pixels):
    compressor = zlib.compressobj()
    data = array.array("B")
    for y in range(height):
        data.append(0)
        for x in range(width):
            data.extend(pixels[y * width + x])
    compressed = compressor.compress(data.tostring())
    flushed = compressor.flush()
    return compressed + flushed


def write_png(filename, width, height, pixels):
    out = open(filename, "wb")
    out.write(struct.pack("8B", 137, 80, 78, 71, 13, 10, 26, 10))
    output_chunk(out, "IHDR", struct.pack("!2I5B", width, height, 8, 2, 0, 0, 0))
    output_chunk(out, "IDAT", get_data(width, height, pixels))
    output_chunk(out, "IEND", b'')
    out.close()
