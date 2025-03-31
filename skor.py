def skor():
    try:
        skor = int(input("Masukkan skor (0-100): "))
        
        if skor < 0 or skor > 100:
            print("Error: Skor harus di antara 0-100")
            return
        
        if skor >= 90:
            nilai_huruf = "A"
            predikat = "Dengan Pujian"
            
        elif skor >= 80:  
            nilai_huruf = "B"
            predikat = "Sangat Memuaskan"
            
        elif skor >= 70: 
            nilai_huruf = "C"
            predikat = "Memuaskan"
            
        elif skor >= 60: 
            nilai_huruf = "D"
            predikat = "Tidak Memuaskan"
            
        else:            
            nilai_huruf = "E"
            predikat = "TIDAK LULUS"
        
        
        print(f"Skor Anda: {skor}")
        print(f"Nilai Huruf: {nilai_huruf}")
        print(f"Predikat   : {predikat}")
    
    except ValueError:
        print("Error: Masukkan nilai numerik (bilangan bulat).")

skor()
