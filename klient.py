import ffmpeg
import os
import time
import uuid
import requests

def optymalizuj_wideo_kompatybilne(sciezka_wejsciowa, sciezka_wyjsciowa, poziom_jakosci=23):
    """Kompresuje wideo przy użyciu uniwersalnego kodeka H.264."""
    if not os.path.exists(sciezka_wejsciowa):
        print(f"❌ Błąd: Plik {sciezka_wejsciowa} nie istnieje!")
        return

    rozmir_przed = os.path.getsize(sciezka_wejsciowa) / (1024 * 1024)
    print(f"🎬 Rozpoczynam optymalizację (Wersja H.264): {sciezka_wejsciowa}")
    print(f"📊 Rozmiar początkowy około: {rozmir_przed:.2f} MB")
    
    start_time = time.time()

    try:
        (
            ffmpeg
            .input(sciezka_wejsciowa)
            .output(
                sciezka_wyjsciowa, 
                vcodec='libx264', 
                crf=poziom_jakosci, 
                preset='veryfast',  # Przyspieszona wersja dla szybszych testów
                pix_fmt='yuv420p', 
                acodec='copy'
            )
            .overwrite_output()
            .run(quiet=True)
        )

        czas_trwania = time.time() - start_time
        rozmiar_po = os.path.getsize(sciezka_wyjsciowa) / (1024 * 1024)
        oszczednosc = ((rozmir_przed - rozmiar_po) / rozmir_przed) * 100

        print("\n✅ Sukces! Optymalizacja zakończona.")
        print(f"⏱️ Czas operacji: {czas_trwania:.1f} sekund")
        print(f"📉 Nowy rozmiar około: {rozmiar_po:.2f} MB")
        print(f"💎 Zaoszczędzono miejsce około: {oszczednosc:.1f}%")

    except ffmpeg.Error as e:
        print(f"❌ Wystąpił błąd podczas przetwarzania FFmpeg: {e}")

if __name__ == "__main__":
    print("=== Inteligentny Kompresor Wideo Premium ===")
    
    # 1. Pobieramy unikalny identyfikator sprzętowy komputera
    user_id = str(uuid.getnode())
    
    # URL Twojego lokalnego serwera testowego (który masz otwarty w pierwszej karcie)
    URL_SERWERA = "http://127.0.0.1:5000/sprawdz-limit"
    
    print("⏳ Sprawdzanie licencji w chmurze...")
    try:
        # 2. Wysyłamy zapytanie do serwera sprawdzającego limity
        odpowiedz = requests.post(URL_SERWERA, json={"user_id": user_id}, timeout=5)
        dane = odpowiedz.json()
        
        if odpowiedz.status_code == 403:
            print(f"\n❌ {dane['komunikat']}")
            print("🔗 Kup pełną wersję tutaj: https://twoja-strona-gumroad.com")
            input("\nNaciśnij Enter, aby zamknąć...")
            exit()
            
        elif odpowiedz.status_code == 200:
            print(f"🎁 Wersja próbna: {dane['komunikat']}\n")
            
    except requests.exceptions.RequestException:
        print("\n❌ Błąd połączenia z serwerem licencji. Upewnij się, że serwer działa.")
        input("\nNaciśnij Enter, aby zamknąć...")
        exit()

    # 3. Pobieranie pliku od użytkownika, jeśli serwer zezwolił na uruchomienie
    plik_wejsciowy = input("Wpisz nazwę pliku wideo (np. film_testowy.mp4): ").strip()
    
    nazwa, rozszerzenie = os.path.splitext(plik_wejsciowy)
    plik_wyjsciowy = f"{nazwa}_zmniejszony{rozszerzenie}"
    
    # 4. Uruchomienie kompresji
    optymalizuj_wideo_kompatybilne(plik_wejsciowy, plik_wyjsciowy)
    
    input("\nNaciśnij Enter, aby zamknąć program...")