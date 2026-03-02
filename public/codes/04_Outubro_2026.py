import wave
import struct
import numpy as np

# Definição das constantes
FREQUENCIA_BEEP = 800  # Hz
DURACAO_BEEP = 0.1  # segundos
DURACAO_PAUSA = 0.1  # segundos
SAMPLE_RATE = 44100  # Hz
BITS_PER_SAMPLE = 16
CHANNELS = 1

# Código Morse para cada letra e número
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def gerar_sinal_beep(duracao):
    """Gera um sinal de beep com a duração especificada."""
    t = np.linspace(0, duracao, int(duracao * SAMPLE_RATE), endpoint=False)
    beep = 0.5 * np.sin(2.0 * np.pi * FREQUENCIA_BEEP * t)
    return beep

def gerar_sinal_pausa(duracao):
    """Gera uma pausa com a duração especificada."""
    return np.zeros(int(duracao * SAMPLE_RATE))

def texto_para_morse(texto):
    """Converte um texto em código Morse."""
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in texto)

def gerar_audio_morse(morse_code):
    """Gera um arquivo de áudio .wav com o código Morse."""
    audio = np.array([], dtype=np.float32)
    for char in morse_code:
        if char == '.':
            audio = np.concatenate((audio, gerar_sinal_beep(DURACAO_BEEP)))
            audio = np.concatenate((audio, gerar_sinal_pausa(DURACAO_PAUSA)))
        elif char == '-':
            audio = np.concatenate((audio, gerar_sinal_beep(3 * DURACAO_BEEP)))
            audio = np.concatenate((audio, gerar_sinal_pausa(DURACAO_PAUSA)))
        elif char == ' ':
            audio = np.concatenate((audio, gerar_sinal_pausa(3 * DURACAO_PAUSA)))
        elif char == '/':
            audio = np.concatenate((audio, gerar_sinal_pausa(7 * DURACAO_PAUSA)))
    
    # Normalizar o áudio para o intervalo [-1, 1]
    audio = audio / np.max(np.abs(audio))
    
    # Converter para int16
    audio = (audio * 32767).astype(np.int16)
    
    # Escrever o arquivo .wav
    with wave.open('output.wav', 'w') as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(BITS_PER_SAMPLE // 8)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(struct.pack(f'{len(audio)}h', *audio))

def main():
    texto = input("Digite o texto que deseja converter para código Morse: ")
    morse_code = texto_para_morse(texto)
    print(f"Código Morse: {morse_code}")
    gerar_audio_morse(morse_code)
    print("Áudio gerado com sucesso como 'output.wav'.")

if __name__ == '__main__':
    main()