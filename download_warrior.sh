#!/bin/bash
# Download all Warrior_M01 files for manual loading into viewer

mkdir -p warrior_files
cd warrior_files

echo "Downloading Warrior_M01 sprite files..."

# Core files
curl -O http://127.0.0.1:5173/dist/Warrior_M01/frames_index.json
curl -O http://127.0.0.1:5173/dist/Warrior_M01/character.meta.json

# Atlas JSON and PNG pairs
curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_walk.json
curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_walk.png

curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_run.json
curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_run.png

curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_attack_slash.json
curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_attack_slash.png

curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_hit.json
curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_hit.png

curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_die.json
curl -O http://127.0.0.1:5173/dist/Warrior_M01/atlas_64_die.png

echo "Done! All files downloaded to warrior_files/"
echo "Now select all files in this folder using the file picker in the viewer"
ls -la