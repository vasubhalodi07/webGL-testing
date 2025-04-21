import brotli

# List of .br files to decompress
files = [
    "Build/WebGL.framework.js.br",
    "Build/WebGL.data.br",
    "Build/WebGL.wasm.br"
]

for file in files:
    with open(file, "rb") as f:
        compressed_data = f.read()
        decompressed_data = brotli.decompress(compressed_data)

    # Save to the same filename without .br
    output_file = file[:-3]  # Remove '.br'
    with open(output_file, "wb") as f:
        f.write(decompressed_data)

    print(f"✅ Decompressed: {output_file}")
