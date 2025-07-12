#!/usr/bin/env node

import fs from 'fs';
import path from 'path';

console.log('🚀 Setting up build system for K-Pop Heardle...\n');

// Create necessary directories
const directories = [
	'src/components',
	'src/stores', 
	'src/utils',
	'src/types',
	'src/lib',
	'dist',
	'backups'
];

directories.forEach(dir => {
	if (!fs.existsSync(dir)) {
		fs.mkdirSync(dir, { recursive: true });
		console.log(`✅ Created directory: ${dir}`);
	}
});

// Backup existing files
const filesToBackup = [
	'main.js',
	'index.html',
	'music-stuff/songs.js'
];

const backupDir = 'backups';
const timestamp = new Date().toISOString().replace(/[:.]/g, '-');

filesToBackup.forEach(file => {
	if (fs.existsSync(file)) {
		const backupPath = path.join(backupDir, `${path.basename(file)}.${timestamp}`);
		fs.copyFileSync(file, backupPath);
		console.log(`✅ Backed up: ${file} -> ${backupPath}`);
	}
});

// Create a basic .gitignore if it doesn't exist
const gitignoreContent = `# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Build outputs
dist/
build/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Logs
logs
*.log

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/

# SvelteKit
.svelte-kit/

# Vite
.vite/
`;

if (!fs.existsSync('.gitignore')) {
	fs.writeFileSync('.gitignore', gitignoreContent);
	console.log('✅ Created .gitignore');
}

console.log('\n🎉 Build system setup complete!');
console.log('\nNext steps:');
console.log('1. Run: npm install');
console.log('2. Run: npm run dev');
console.log('3. Start developing with the new build system!');