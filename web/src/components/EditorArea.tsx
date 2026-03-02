import { useState, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { Play, Loader2, BookOpen, X, Copy, Check } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import type { PythonCode } from '../types';

interface EditorAreaProps {
    code: PythonCode | null;
    editorValue: string;
    onChangeEditor: (val: string) => void;
    isRunning: boolean;
    onRun: (code: string) => void;
    theme: 'dark' | 'light';
}

export function EditorArea({ code, editorValue, onChangeEditor, onRun, isRunning, theme }: EditorAreaProps) {
    const [showReadme, setShowReadme] = useState(false);
    const [copied, setCopied] = useState(false);

    useEffect(() => {
        if (code && code.codeUrl) {
            onChangeEditor(code.codeUrl);
        } else {
            onChangeEditor('# Selecione um arquivo para começar');
            setShowReadme(false);
        }
    }, [code]);

    const handleCopy = () => {
        navigator.clipboard.writeText(editorValue);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div className="flex-1 flex flex-col min-h-0 h-full bg-vscode-bg relative z-0">
            {/* Editor Header / Breadcrumbs */}
            {code ? (
                <>
                    <div className="flex bg-vscode-bg border-b border-vscode-border">
                        <div className="px-3 py-2 bg-vscode-editor text-vscode-textActive border-t-2 border-vscode-primary text-xs font-medium flex items-center gap-2">
                            <span className="text-vscode-python font-bold">py</span>
                            {code.filename}
                        </div>
                    </div>

                    {/* Toolbar */}
                    <div className="px-4 py-2 flex justify-between items-center bg-vscode-editor border-b border-vscode-border">
                        <div className="text-sm font-semibold opacity-90 text-vscode-text">{code.description}</div>
                        <div className="flex items-center gap-2">
                            {code.readmeContent && (
                                <button
                                    onClick={() => setShowReadme(!showReadme)}
                                    title="Ver Documentação (README)"
                                    id="readme-button"
                                    className={`flex items-center gap-1.5 px-3 py-1 text-xs font-semibold rounded-sm transition-colors ${showReadme ? 'bg-vscode-sidebarHover text-vscode-textActive' : 'bg-transparent text-vscode-text hover:bg-vscode-sidebarHover'}`}
                                >
                                    <BookOpen size={14} /> README
                                </button>
                            )}
                            {code && (
                                <button
                                    onClick={handleCopy}
                                    title="Copiar Código"
                                    className="flex items-center gap-1.5 px-3 py-1 text-xs font-semibold rounded-sm transition-colors bg-transparent text-vscode-text hover:bg-vscode-sidebarHover"
                                >
                                    {copied ? <Check size={14} className="text-green-500" /> : <Copy size={14} />}
                                    Copiar
                                </button>
                            )}
                            <button
                                onClick={() => onRun(editorValue)}
                                disabled={isRunning}
                                title="Executar Código"
                                id="run-button"
                                className="flex items-center gap-1.5 bg-green-600 hover:bg-green-700 text-white px-3 py-1 rounded-sm text-xs font-semibold disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            >
                                <Play size={14} fill="currentColor" />
                                {isRunning ? 'Executando...' : 'Run'}
                            </button>
                        </div>
                    </div>
                </>
            ) : (
                <div className="h-9 flex items-center justify-between px-3 bg-vscode-bg border-b border-vscode-border select-none">
                    <span className="text-xs text-vscode-text opacity-50">Nenhum ficheiro selecionado</span>
                </div>
            )}


            {/* Split Pane: Editor and Optional Readme */}
            <div className="flex-1 flex overflow-hidden min-h-0 relative">
                <div className="flex-1 relative">
                    {code ? (
                        <Editor
                            height="100%"
                            language="python"
                            theme={theme === 'dark' ? 'vs-dark' : 'light'}
                            value={editorValue}
                            onChange={(value) => onChangeEditor(value || '')}
                            options={{
                                minimap: { enabled: false },
                                fontSize: 14,
                                wordWrap: 'on',
                                readOnly: false,
                                scrollBeyondLastLine: false,
                                smoothScrolling: true,
                                cursorBlinking: 'smooth',
                                padding: { top: 16 }
                            }}
                            loading={
                                <div className="flex items-center justify-center h-full text-vscode-text opacity-70">
                                    <Loader2 className="animate-spin mr-2" size={24} /> Carregando motor inteligente...
                                </div>
                            }
                        />
                    ) : (
                        <div className="w-full h-full flex flex-col items-center justify-center opacity-30 select-none text-vscode-text">
                            <div className="mb-4">
                                <svg viewBox="0 0 128 128" width="60" height="60" fill="currentColor">
                                    <path d="M64 128c-35.3 0-64-28.7-64-64S28.7 0 64 0s64 28.7 64 64-28.7 64-64 64zm0-120C33.1 8 8 33.1 8 64s25.1 56 56 56 56-25.1 56-56S94.9 8 64 8z" />
                                </svg>
                            </div>
                            <p className="text-lg font-light tracking-wide">Bem-vindo ao 365 Dias de Python</p>
                            <p className="text-sm mt-2 opacity-80">Selecione um ficheiro na barra lateral para iniciar.</p>
                        </div>
                    )}
                </div>
                {showReadme && code && code.readmeContent && (
                    <div className="w-full md:w-2/5 min-w-[300px] max-w-[500px] border-l border-vscode-border bg-vscode-editor/95 backdrop-blur-xl p-6 overflow-y-auto absolute md:relative right-0 top-0 h-full z-40 shadow-2xl transition-all duration-300">
                        <div className="flex justify-between items-center mb-4 pb-2 border-b border-vscode-border">
                            <h3 className="font-bold text-vscode-textActive flex items-center gap-2"><BookOpen size={16} /> Documentação</h3>
                            <button onClick={() => setShowReadme(false)} className="text-vscode-text hover:text-vscode-textActive"><X size={16} /></button>
                        </div>
                        <div className="prose prose-sm dark:prose-invert max-w-none text-vscode-text leading-relaxed mt-4
                            prose-headings:text-vscode-textActive prose-a:text-vscode-python prose-a:no-underline hover:prose-a:underline
                            prose-code:text-pink-400 prose-code:bg-vscode-bgHover prose-code:px-1 prose-code:rounded
                            prose-pre:bg-vscode-bg prose-pre:border prose-pre:border-vscode-border">
                            <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]}>
                                {code.readmeContent}
                            </ReactMarkdown>
                        </div>
                    </div>
                )}
            </div>

        </div>
    );
}
