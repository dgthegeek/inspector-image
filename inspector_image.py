import sys
from PIL import Image
import exifread
import re

def extract_metadata(image_path):
    """
    Extrait et affiche les métadonnées de l'image, y compris les coordonnées GPS.
    """
    try:
        with open(image_path, 'rb') as image_file:
            tags = exifread.process_file(image_file)
            gps_latitude = tags.get('GPS GPSLatitude')
            gps_longitude = tags.get('GPS GPSLongitude')
            if gps_latitude and gps_longitude:
                lat = convert_to_degrees(gps_latitude)
                lon = convert_to_degrees(gps_longitude)
                print(f"Lat/Lon:\t({lat}) / ({lon})")
            else:
                print("Les coordonnées GPS ne sont pas disponibles.")
    except Exception as e:
        print(f"Erreur lors de l'extraction des métadonnées: {e}")

def convert_to_degrees(value):
    """
    Convertit les coordonnées GPS en degrés décimaux.
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)

def extract_pgp_key(image_path):
    """
    Extrait la clé PGP de l'image en cherchant dans les métadonnées et le contenu de l'image.
    """
    try:
        # Vérifier d'abord les métadonnées
        with open(image_path, 'rb') as image_file:
            tags = exifread.process_file(image_file)
            for tag in tags.values():
                if isinstance(tag.values, str) and "BEGIN PGP PUBLIC KEY BLOCK" in tag.values:
                    return tag.values

        # Si pas trouvé dans les métadonnées, chercher dans le contenu de l'image
        with open(image_path, 'rb') as image_file:
            content = image_file.read().decode('utf-8', errors='ignore')
            pgp_key_match = re.search(r'-----BEGIN PGP PUBLIC KEY BLOCK-----.*?-----END PGP PUBLIC KEY BLOCK-----', content, re.DOTALL)
            if pgp_key_match:
                return pgp_key_match.group(0)

        return "Aucune clé PGP trouvée dans l'image."
    except Exception as e:
        return f"Erreur lors de l'extraction de la clé PGP: {e}"

def main():
    """
    Point d'entrée principal du programme. Gère les arguments en ligne de commande.
    """
    if len(sys.argv) != 3:
        print("Usage: image -[map|steg] image.jpeg")
        return

    option = sys.argv[1]
    image_path = sys.argv[2]

    if option == '-map':
        extract_metadata(image_path)
    elif option == '-steg':
        pgp_key = extract_pgp_key(image_path)
        print(pgp_key)
    else:
        print("Option non reconnue. Utilisez '-map' pour les métadonnées ou '-steg' pour la stéganographie.")

if __name__ == "__main__":
    main()