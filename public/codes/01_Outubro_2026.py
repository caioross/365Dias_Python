import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f'Arquivo criado: {event.src_path}')

    def on_deleted(self, event):
        if not event.is_directory:
            print(f'Arquivo deletado: {event.src_path}')

def monitor_directory(path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    directory_to_watch = input("Digite o caminho do diretório que deseja monitorar: ")
    if os.path.isdir(directory_to_watch):
        monitor_directory(directory_to_watch)
    else:
        print("O caminho fornecido não é um diretório válido.")

if __name__ == '__main__':
    main()