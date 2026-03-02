import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PARENT_DIR = path.resolve(__dirname, '..');
const SOURCE_YEAR_DIR = path.join(PARENT_DIR, '2026');
const LIST_FILE = path.join(PARENT_DIR, 'lista.txt');

const PUBLIC_DIR = path.join(__dirname, 'public');
const CODES_DIR = path.join(PUBLIC_DIR, 'codes');
const DATA_FILE = path.join(PUBLIC_DIR, 'data.json');

// Ensure directories exist
if (!fs.existsSync(PUBLIC_DIR)) fs.mkdirSync(PUBLIC_DIR, { recursive: true });
if (!fs.existsSync(CODES_DIR)) fs.mkdirSync(CODES_DIR, { recursive: true });

// Month mapping
const monthMap = {
  'Janeiro': '01',
  'Fevereiro': '02',
  'Março': '03',
  'Abril': '04',
  'Maio': '05',
  'Junho': '06',
  'Julho': '07',
  'Agosto': '08',
  'Setembro': '09',
  'Outubro': '10',
  'Novembro': '11',
  'Dezembro': '12'
};

// 1. Read lista.txt and build a lookup table
const dateDescriptionMap = {};
if (fs.existsSync(LIST_FILE)) {
  const listContent = fs.readFileSync(LIST_FILE, 'utf-8');
  const lines = listContent.split('\n');
  lines.forEach(line => {
    // 01_01_2026_nome_arquivo.py - Descrição...
    const match = line.match(/^(\d{2})_(\d{2})_(\d{4})_.*\.py\s+-\s+(.+)$/);
    if (match) {
      const key = `${match[1]}_${match[2]}_${match[3]}`; // DD_MM_YYYY
      dateDescriptionMap[key] = match[4].trim();
    }
  });
}

// 2. Scan the 2026 folder recursively
const allCodes = [];

function walkDir(dir) {
  if (!fs.existsSync(dir)) return;
  const list = fs.readdirSync(dir);

  list.forEach(item => {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      walkDir(fullPath);
    } else if (item === 'main.py') {
      // It's a python script inside a day folder
      // Let's assume folder structure is .../Ano/Mês/Dia/main.py
      const parts = fullPath.split(path.sep);
      // reverse indexing: [..., yearDir, monthDir, dayDir, 'main.py']
      const dayDir = parts[parts.length - 2];
      const monthDir = parts[parts.length - 3];
      const yearDir = parts[parts.length - 4];

      const monthNum = monthMap[monthDir];
      if (!monthNum) return; // skip if invalid

      const dateKey = `${dayDir}_${monthNum}_${yearDir}`;
      const desc = dateDescriptionMap[dateKey] || 'Script diário do 365 Dias de Python.';

      const codeContent = fs.readFileSync(fullPath, 'utf-8');
      const targetFilename = `${dayDir}_${monthDir}_${yearDir}.py`;
      const destPath = path.join(CODES_DIR, targetFilename);

      fs.writeFileSync(destPath, codeContent);

      // Ler README
      const readmePath = path.join(dir, 'readme.md');
      let readmeContent = '';
      if (fs.existsSync(readmePath)) {
        readmeContent = fs.readFileSync(readmePath, 'utf-8');
      }

      allCodes.push({
        filename: targetFilename,
        date: `${yearDir}-${monthNum}-${dayDir}`,
        day: dayDir,
        month: monthDir,
        year: yearDir,
        description: desc,
        codeUrl: `/codes/${targetFilename}`,
        readmeContent: readmeContent,
        importedLibs: Array.from(codeContent.matchAll(/^import\s+([a-zA-Z0-9_]+)/gm)).map(m => m[1])
          .concat(Array.from(codeContent.matchAll(/^from\s+([a-zA-Z0-9_]+)\s+import/gm)).map(m => m[1]))
      });
    }
  });
}

console.log('Varrendo pasta 2026...');
walkDir(SOURCE_YEAR_DIR);

allCodes.sort((a, b) => a.date.localeCompare(b.date));

fs.writeFileSync(DATA_FILE, JSON.stringify(allCodes, null, 2));

console.log(`Sucesso! Processados ${allCodes.length} ficheiros.`);
