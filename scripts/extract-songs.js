#!/usr/bin/env node

import fs from 'fs';
import path from 'path';

// Read the existing songs.js file
const songsPath = path.join(process.cwd(), 'music-stuff', 'songs.js');
const outputPath = path.join(process.cwd(), 'src', 'lib', 'songs.ts');

try {
	const songsContent = fs.readFileSync(songsPath, 'utf8');
	
	// Extract the songs array using regex
	const songsMatch = songsContent.match(/let songs = \[([\s\S]*?)\];/);
	
	if (!songsMatch) {
		console.error('Could not find songs array in songs.js');
		process.exit(1);
	}
	
	const songsArrayContent = songsMatch[1];
	
	// Convert to TypeScript format
	const tsContent = `import type { Song } from '../types/game';

export const songs: Song[] = ${songsArrayContent};

export function getSongForDay(day: number): Song | null {
	if (day >= songs.length) {
		return null;
	}
	return songs[day];
}

export function getCurrentSong(): Song | null {
	const today = new Date();
	const startDate = new Date('2025-04-08');
	const day = Math.floor((today.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24));
	return getSongForDay(day);
}
`;
	
	// Write the new file
	fs.writeFileSync(outputPath, tsContent);
	console.log(`✅ Successfully extracted songs to ${outputPath}`);
	
} catch (error) {
	console.error('Error extracting songs:', error);
	process.exit(1);
}