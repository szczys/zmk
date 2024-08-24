# Zephyr™ Mechanical Keyboard (ZMK) Firmware

## Build Instructions

Use the helper scripts to build and flash firmware:

```
# Build firmware
cd app
./autobuild

# Copy firmware to left half
./copyleft

# Copy firmware to right half
./copyright
```

## Manual Build Instructions

```
cd app
west build -d build/left -b nice_nano -p -- -DSHIELD=corne_left
west build -d build/right -b nice_nano -p -- -DSHIELD=corne_right
cp build/left/zephyr/zmk.uf2 /media/mike/NICENANO/.
cp build/right/zephyr/zmk.uf2 /media/mike/NICENANO/.
```
