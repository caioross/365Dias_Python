import { Minus, Maximize2, X, Code2, Moon, Sun, Github, Linkedin, Globe, Map, CalendarClock, Download } from 'lucide-react';

interface TopBarProps {
    theme: 'dark' | 'light';
    toggleTheme: () => void;
    onStartTour: () => void;
    onTodayClick: () => void;
    onDownloadClick: () => void;
    canDownload: boolean;
}

export function TopBar({ theme, toggleTheme, onStartTour, onTodayClick, onDownloadClick, canDownload }: TopBarProps) {
    return (
        <div className="h-10 flex border-b border-vscode-border bg-vscode-header items-center justify-between px-3 select-none">
            <div className="flex items-center gap-2">
                <Code2 size={18} className="text-vscode-primary" />
                <span className="text-xs font-semibold text-vscode-text hidden sm:inline-block">365 Dias de Python</span>
                <div className="ml-4 flex gap-4 text-xs">
                    <a href="#" className="hover:text-vscode-textActive cursor-pointer transition-colors hidden md:block">Documentação</a>
                    <a href="#" className="hover:text-vscode-textActive cursor-pointer transition-colors hidden md:block">Repositório Origem</a>
                </div>
            </div>

            {/* Title */}
            <div className="absolute left-1/2 -translate-x-1/2 text-xs text-vscode-text flex items-center gap-2 opacity-80">
                <span>365-python-web - Visual Studio Code</span>
            </div>

            <div className="flex items-center gap-3 text-vscode-text">
                <div className="flex items-center gap-2 mr-2 opacity-80">
                    <button onClick={onTodayClick} title="Script de Hoje" id="today-button" className="hover:text-vscode-textActive hover:bg-vscode-sidebarHover p-1 rounded-sm transition-colors text-vscode-primary">
                        <CalendarClock size={14} />
                    </button>
                    <button onClick={onDownloadClick} disabled={!canDownload} title="Baixar Script Atual" id="download-button" className={`hover:text-vscode-textActive hover:bg-vscode-sidebarHover p-1 rounded-sm transition-colors ${!canDownload ? 'opacity-50 cursor-not-allowed' : 'text-vscode-primary'}`}>
                        <Download size={14} />
                    </button>

                    <div className="w-px h-4 bg-vscode-border mx-1"></div>

                    <a href="https://github.com/caioross/365Dias_Python" target="_blank" title="Repositório GitHub" className="hover:text-vscode-textActive hover:bg-vscode-sidebarHover p-1 rounded-sm transition-colors">
                        <Github size={14} />
                    </a>
                    <a href="https://www.linkedin.com/in/caiorossi/" target="_blank" title="Perfil no LinkedIn" className="hover:text-vscode-textActive hover:bg-vscode-sidebarHover p-1 rounded-sm transition-colors">
                        <Linkedin size={14} />
                    </a>
                    <a href="https://caioross.github.io/" target="_blank" title="Site Pessoal" className="hover:text-vscode-textActive hover:bg-vscode-sidebarHover p-1 rounded-sm transition-colors">
                        <Globe size={14} />
                    </a>
                    <button onClick={onStartTour} title="Iniciar Tour Virtual" id="tour-button" className="hover:text-vscode-textActive hover:bg-vscode-sidebarHover p-1 rounded-sm transition-colors text-vscode-primary">
                        <Map size={14} />
                    </button>
                </div>

                <button
                    onClick={toggleTheme}
                    className="hover:bg-vscode-sidebarHover p-1 rounded-sm transition-colors text-vscode-text"
                    title={`Trocar para ${theme === 'dark' ? 'Claro' : 'Escuro'}`}
                >
                    {theme === 'dark' ? <Sun size={14} /> : <Moon size={14} />}
                </button>
                <div className="flex gap-2 opacity-50">
                    <Minus size={14} className="cursor-not-allowed" />
                    <Maximize2 size={12} className="cursor-not-allowed" />
                    <X size={14} className="cursor-not-allowed" />
                </div>
            </div>
        </div>
    );
}
