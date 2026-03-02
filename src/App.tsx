import { useState, useEffect } from 'react';
import { Sidebar } from './components/Sidebar';
import { TopBar } from './components/TopBar';
import { EditorArea } from './components/EditorArea';
import { TerminalArea } from './components/TerminalArea';
import type { PythonCode, Theme } from './types';
import Joyride, { STATUS } from 'react-joyride';
import type { CallBackProps } from 'react-joyride';
import { TerminalSquare } from 'lucide-react';

function App() {
  const [theme, setTheme] = useState<Theme>('dark');
  const [codes, setCodes] = useState<PythonCode[]>([]);
  const [selectedCode, setSelectedCode] = useState<PythonCode | null>(null);

  const [editorValue, setEditorValue] = useState('');
  const [isTerminalVisible, setIsTerminalVisible] = useState(true);
  const [terminalOutput, setTerminalOutput] = useState<string[]>(['Inicializando ambiente Python (Pyodide)... Aguarde.']);
  const [terminalExpanded, setTerminalExpanded] = useState(false);

  const [pyodideInstance, setPyodideInstance] = useState<any>(null);
  const [isRunning, setIsRunning] = useState(false);

  const [runTour, setRunTour] = useState(false);

  const tourSteps = [
    { target: 'body', content: 'Bem-vindo ao 365 Python Web! Vamos conhecer a plataforma através desta jornada incrível.', placement: 'center' as const, disableBeacon: true },
    { target: '.bg-vscode-sidebar', content: 'Nesta aba lateral elegante, explore e interaja com todos os códigos separados por datas!' },
    { target: 'button[title="Buscar Código"]', content: 'A pesquisa ultra rápida ajuda a encontrar scripts por título, tema ou bibliotecas.' },
    { target: 'button[title="Calendário"]', content: 'A vista Calendário mapeia perfeitamente os 365 dias. Útil para acompanhar sua maratona Python!' },
    { target: 'button[title="Dia Atual"]', content: 'Você não tem tempo a perder! Pule direto para o aprendizado do dia de hoje com este prático atalho.' },
    { target: 'button[title="Fazer Download"]', content: 'Gostou do que construiu? Clique no ícone de download para salvar o arquivo de onde você estiver.' },
    { target: '.monaco-editor', content: 'Aqui é o epicentro! O Editor Monacco injetado traz a exata sensação do VS Code.' },
    { target: '#run-button', content: 'A cereja do bolo: execute o código internamente no navegador sob demanda do Pyodide, sem usar servidores de terceiros.' },
    { target: '#readme-button', content: 'Com uma dúvida no código focado? Este botão acionará uma rica documentação do script que está testando.' },
    { target: 'footer', content: 'Tudo feito com imenso carinho e foco no seu total aprendizado. Aproveite o projeto e até o fim do desafio!' }
  ];

  const TourTooltip = ({ index, isLastStep, step, backProps, primaryProps, skipProps, tooltipProps }: any) => (
    <div {...tooltipProps} className="bg-vscode-bg/50 backdrop-blur-2xl border border-white/10 shadow-2xl rounded-2xl p-6 max-w-sm text-vscode-text">
      {step.title && <h3 className="text-xl font-bold mb-2 text-vscode-textActive bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">{step.title}</h3>}
      <div className="text-sm font-medium leading-relaxed opacity-90 mb-6 drop-shadow-md">{step.content}</div>
      <div className="flex items-center justify-between">
        <button {...skipProps} className="text-sm text-vscode-text opacity-50 hover:opacity-100 transition-opacity font-semibold">
          Pular Tour
        </button>
        <div className="flex gap-3">
          {index > 0 && (
            <button {...backProps} className="px-4 py-2 rounded-xl text-sm bg-vscode-editor/90 hover:bg-vscode-sidebarHover text-vscode-text transition-colors border border-vscode-border">
              Voltar
            </button>
          )}
          <button {...primaryProps} className="px-5 py-2 rounded-xl text-sm bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-500 hover:to-blue-400 text-white font-bold transition-all shadow-[0_0_15px_rgba(59,130,246,0.5)]">
            {isLastStep ? 'Concluir' : 'Próximo'}
          </button>
        </div>
      </div>
    </div>
  );

  const handleJoyrideCallback = (data: CallBackProps) => {
    const { status } = data;
    const finishedStatuses: string[] = [STATUS.FINISHED, STATUS.SKIPPED];
    if (finishedStatuses.includes(status)) {
      setRunTour(false);
    }
  };

  const handleTodayClick = () => {
    const today = new Date();
    const dayStr = String(today.getDate()).padStart(2, '0');
    const monthStr = String(today.getMonth() + 1).padStart(2, '0');
    const yearStr = String(today.getFullYear());
    const dateStr = `${yearStr}-${monthStr}-${dayStr}`;

    // As datas estão no formato "YYYY-MM-DD"
    const todayCode = codes.find(c => c.date === dateStr);
    if (todayCode) {
      handleSelectScript(todayCode);
    } else {
      alert(`Nenhum script encontrado para o dia de hoje (${dateStr}).`);
    }
  };

  const handleDownloadClick = () => {
    if (!selectedCode) return;
    const blob = new Blob([editorValue], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = selectedCode.filename;
    a.click();
    URL.revokeObjectURL(url);
  };

  // Load Data
  useEffect(() => {
    fetch('/data.json')
      .then(res => res.json())
      .then(data => setCodes(data))
      .catch(err => console.error("Falha ao ler data.json:", err));
  }, []);

  // Sync Theme with HTML class
  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.remove('light');
    } else {
      document.documentElement.classList.add('light');
    }
  }, [theme]);

  // Handle Select Script
  const handleSelectScript = async (code: PythonCode) => {
    // Tenta carregar o código para ter certeza de que CodeUrl está válido
    try {
      const res = await fetch(code.codeUrl);
      const content = await res.text();
      // O React state vai armazenar o code. O component EditorArea lerá do origin.
      setSelectedCode({ ...code, codeUrl: content }); // Passando string temporariamente no codeUrl (gambiarra rápida para ter a string no editor via prop)
    } catch (err) {
      setSelectedCode({ ...code, codeUrl: "# Erro ao carregar script Python" });
    }
  };

  // Init Pyodide
  useEffect(() => {
    async function initPyodide() {
      try {
        // We load pyodide via CDN to avoid serving heavy blobs locally, or local via npm. 
        // Vite handles it if configured, but CDN is foolproof for dynamic loading.
        // @ts-ignore
        if (window.loadPyodide) {
          // @ts-ignore
          const pyodide = await window.loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
          });
          setPyodideInstance(pyodide);
          setTerminalOutput(prev => [...prev, 'Python pronto para uso! 🚀']);
        }
      } catch (err) {
        setTerminalOutput(prev => [...prev, 'Erro ao carregar o interpretador Python.']);
        console.error(err);
      }
    }

    // Inject Script dynamcially if missing
    // @ts-ignore
    if (!window.loadPyodide) {
      const script = document.createElement('script');
      script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
      script.onload = initPyodide;
      document.head.appendChild(script);
    } else {
      initPyodide();
    }
  }, []);

  // Executar Código
  const runPython = async (editorValueStr: string) => {
    if (!pyodideInstance || isRunning) return;

    setIsRunning(true);
    setTerminalOutput([]); // Clear prior to run
    setTerminalExpanded(true); // Auto expand slightly

    try {
      // Overwrite stdout to capture print() in TerminalArea
      pyodideInstance.setStdout({ batched: (str: string) => setTerminalOutput(prev => [...prev, str]) });
      pyodideInstance.setStderr({ batched: (str: string) => setTerminalOutput(prev => [...prev, str]) });

      // Patch synchronous input() to use window.prompt so beginner scripts don't crash
      await pyodideInstance.runPythonAsync(`
import builtins
def _mock_input(prompt=""):
    import js
    return js.prompt(prompt) or ""
builtins.input = _mock_input
      `);

      // Async run
      await pyodideInstance.runPythonAsync(editorValueStr);
      setTerminalOutput(prev => [...prev, '\n[Execução finalizada com sucesso]']);

    } catch (err: any) {
      setTerminalOutput(prev => [...prev, err.toString()]);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="flex flex-col h-screen w-full overflow-hidden">
      <Joyride
        steps={tourSteps}
        run={runTour}
        continuous={true}
        showSkipButton={true}
        tooltipComponent={TourTooltip}
        callback={handleJoyrideCallback}
        floaterProps={{ disableAnimation: false }}
        styles={{ options: { zIndex: 10000 } }}
      />
      <TopBar
        theme={theme}
        toggleTheme={() => setTheme(t => t === 'dark' ? 'light' : 'dark')}
        onStartTour={() => {
          if (!selectedCode && codes.length > 0) {
            handleSelectScript(codes[0]); // Seleciona o primeiro script para que os painéis (Readme, Terminal) renderizem botões caso necessário
          }
          setTimeout(() => setRunTour(true), 300); // Dá um atraso sutil para o React renderizar botões em tela
        }}
        onTodayClick={handleTodayClick}
        onDownloadClick={handleDownloadClick}
        canDownload={!!selectedCode}
      />

      <div className="flex flex-1 overflow-hidden h-full">
        {/* Sidebar Left */}
        <Sidebar codes={codes} onSelect={handleSelectScript} selectedCode={selectedCode} />

        {/* Main Content Area */}
        <div className="flex-1 flex flex-col h-full bg-vscode-bg min-w-0 relative">
          <EditorArea
            code={selectedCode}
            editorValue={editorValue}
            onChangeEditor={setEditorValue}
            isRunning={isRunning}
            onRun={runPython}
            theme={theme}
          />
          {selectedCode && isTerminalVisible && (
            <TerminalArea
              output={terminalOutput}
              onClear={() => setTerminalOutput([])}
              isExpanded={terminalExpanded}
              toggleExpanded={() => setTerminalExpanded(!terminalExpanded)}
              onClose={() => setIsTerminalVisible(false)}
            />
          )}

          {selectedCode && !isTerminalVisible && (
            <button
              onClick={() => setIsTerminalVisible(true)}
              className="absolute bottom-4 right-4 bg-vscode-primary hover:bg-blue-600 text-white p-3 rounded-full shadow-lg transition-all hover:scale-105 z-50 flex items-center justify-center group border border-blue-400/30"
              title="Restaurar Terminal"
            >
              <TerminalSquare size={20} />
              <span className="max-w-0 overflow-hidden group-hover:max-w-[150px] transition-all duration-300 ease-in-out whitespace-nowrap ml-0 group-hover:ml-2 text-sm font-semibold">
                Mostrar Terminal
              </span>
            </button>
          )}
        </div>
      </div>

      {/* The Footer */}
      <footer className="w-full bg-vscode-bg/95 backdrop-blur-md border-t border-vscode-border py-1.5 flex justify-center items-center text-xs text-vscode-text opacity-80 z-50 font-medium tracking-wide">
        Feito com <span className="text-red-500 animate-pulse mx-1.5 text-sm">♥</span> para quem quer aprender e dominar Python.
      </footer>
    </div>
  );
}

export default App;
