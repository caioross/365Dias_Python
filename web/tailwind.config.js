/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                vscode: {
                    bg: '#1e1e1e',
                    sidebar: '#252526',
                    sidebarHover: '#2a2d2e',
                    header: '#333333',
                    border: '#3c3c3c',
                    text: '#cccccc',
                    textActive: '#ffffff',
                    primary: '#0e639c',
                    primaryHover: '#1177bb',
                    terminal: '#1e1e1e',
                    terminalBorder: '#424242',
                    lineNumber: '#858585',
                    folder: '#dcb67a',
                    python: '#3776ab',
                },
                vslight: {
                    bg: '#ffffff',
                    sidebar: '#f3f3f3',
                    sidebarHover: '#e8e8e8',
                    header: '#dddddd',
                    border: '#cccccc',
                    text: '#333333',
                    textActive: '#000000',
                    primary: '#007acc',
                    primaryHover: '#005999',
                    terminal: '#ffffff',
                    terminalBorder: '#e5e5e5',
                }
            },
            fontFamily: {
                mono: ['"Fira Code"', '"Cascadia Code"', 'Consolas', 'monospace'],
                sans: ['"Segoe UI"', 'system-ui', 'sans-serif'],
            }
        },
    },
    plugins: [],
}
