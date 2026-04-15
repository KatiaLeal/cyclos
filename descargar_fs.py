from gem5.resources.resource import Resource

# Esto descargará el kernel y la imagen de disco oficial en tu carpeta ~/.cache/gem5
print("Descargando kernel...")
kernel = Resource("riscv-boot-exit-kernel")
print(f"Kernel descargado en: {kernel.get_local_path()}")

print("Descargando imagen de disco...")
disk = Resource("riscv-boot-exit-disk")
print(f"Disco descargado en: {disk.get_local_path()}")
