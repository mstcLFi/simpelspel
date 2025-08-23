from pydub import AudioSegment, silence
import os

print("Start")

# --- Config ---
input_file = r"C:\Users\e59050\OneDrive - NHL Stenden\Simpelspel\sounds\voxel brainrot\voxel brainrot.mp3"
output_dir = r"C:\Users\e59050\OneDrive - NHL Stenden\Simpelspel\sounds\voxel brainrot"
min_silence_len = 4500  # ms
silence_thresh = -80     # dBFS, pas aan voor zachtere/stille stukjes
start_padding = 100      # ms
end_padding = 200        # ms

names = [
    "baleno aeronauto",
    "bassolussino",
    "bifolato carnebovino",
    "buscorno gigantini",
    "capricoptero",
    "capronzo ferroviaia",
    "cavaldo triciclino",
    "coniglietto quattroruote",
    "elefanto motoretto",
    "felinella rotarino",
    "flaminoggio rollarossa",
    "girattino cursore",
    "granaglia maiali",
    "lumacardi rotellini",
    "orsorulla",
    "panda spingiterreni",
    "pecuura croccante",
    "pescarretto carbonello",
    "pollastro navigatto",
    "scorpione ghiacciatore",
    "serpenza pedalaio",
    "testuggino reclinetto",
    "uccello sommergino"
]

os.makedirs(output_dir, exist_ok=True)

# --- Load audio ---
audio = AudioSegment.from_mp3(input_file)
print("Audio geladen")
print("Gemiddelde volume:", audio.dBFS)

# --- Split op stilte ---
chunks = silence.split_on_silence(
    audio,
    min_silence_len=min_silence_len,
    silence_thresh=silence_thresh,
    keep_silence=0  # we voegen padding handmatig toe
)
print(f"Stukjes gehakt: {len(chunks)} chunks gevonden")

# --- Voeg padding toe en exporteer ---
for i, chunk in enumerate(chunks):
    if i < len(names):
        # Voeg stilte-padding toe
        new_chunk = AudioSegment.silent(duration=start_padding) + chunk + AudioSegment.silent(duration=end_padding)

        filename = os.path.join(output_dir, f"{names[i]}.mp3")
        new_chunk.export(filename, format="mp3")
        print(f"Exported: {filename}")
    else:
        print(f"Extra chunk {i+1} niet genoemd vanwege ontbrekende naam.")

print("Klaar!")
