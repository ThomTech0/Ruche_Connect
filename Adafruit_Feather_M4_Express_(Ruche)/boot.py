import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D5)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the D0 is connected to ground with a wire
# CircuitPython can write to the drive
storage.remount("/", switch.value)

#cela permet d'écrire les données des capteurs sur un fichier texte pour pouvoir les récupérer avec le raspberry.
