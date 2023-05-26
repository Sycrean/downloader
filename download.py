from pytube import YouTube
import os

def video_download(url, output_path, download_as_mp3=False):
    try:
        youtube = YouTube(url)

        if not download_as_mp3:
            # Alternative Methode zur Auswahl der Auflösung
            video_streams = youtube.streams.filter(progressive=True).order_by('resolution').desc()
            available_resolutions = [stream.resolution for stream in video_streams]

            # Auflösungen anzeigen und Auswahl treffen
            print("Verfügbare Auflösungen:")
            for resolution in available_resolutions:
                print(resolution)

            selected_resolution = input("Geben Sie die gewünschte Auflösung ein: ")

            # Nächstbeste Auflösung auswählen
            resolution_stream = video_streams.get_by_resolution(selected_resolution)
            if not resolution_stream:
                resolution_stream = video_streams.first()

            # Video herunterladen
            file_name = input("Geben Sie den Dateinamen ein (ohne Dateierweiterung): ")
            output_file_path = os.path.join(output_path, file_name + ".mp4")
            resolution_stream.download(output_path=output_file_path)
            print("Das Video wurde erfolgreich heruntergeladen!")
        else:
            audio_stream = youtube.streams.filter(only_audio=True).first()

            # MP3-Datei herunterladen
            file_name = input("Geben Sie den Dateinamen ein (ohne Dateierweiterung): ")
            output_file_path = os.path.join(output_path, file_name + ".mp3")
            audio_stream.download(output_path=output_file_path)
            print("Die MP3-Datei wurde erfolgreich heruntergeladen!")
    except Exception as e:
        print("Fehler beim Herunterladen:", str(e))

# Benutzereingabe
video_url = input("Geben Sie die YouTube-URL des Videos ein: ")
output_folder = input("Geben Sie den Ausgabeordner ein: ")
download_type = input("Möchten Sie das Video als MP3 herunterladen? (ja/nein): ")

if download_type.lower() == "ja":
    video_download(video_url, output_folder, download_as_mp3=True)
else:
    video_download(video_url, output_folder)

