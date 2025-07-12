# 🛠️ Build System Migration Guide

This document explains how to migrate from the current pre-compiled setup to a modern build system.

## 📋 Current State

Your project currently uses:
- **Pre-compiled Svelte application** in `main.js` (9,808 lines, minified)
- **Manual song management** in `music-stuff/songs.js`
- **Basic HTML structure** in `index.html`
- **Python customization script** in `customize.py`

## 🚀 New Build System

The new build system provides:
- **Vite** for fast development and building
- **Svelte** with TypeScript support
- **Hot module replacement** for development
- **Source maps** for debugging
- **Code splitting** and optimization
- **Modern development tools** (ESLint, Prettier)

## 📁 New Project Structure

```
├── src/
│   ├── components/          # Svelte components
│   │   ├── Game.svelte     # Main game component
│   │   ├── AudioPlayer.svelte
│   │   ├── GuessInput.svelte
│   │   ├── GameResult.svelte
│   │   └── Modal.svelte
│   ├── stores/             # Svelte stores
│   │   └── game.ts         # Game state management
│   ├── types/              # TypeScript type definitions
│   │   └── game.ts
│   ├── lib/                # Utility libraries
│   │   └── songs.ts        # Song management
│   ├── utils/              # Helper functions
│   ├── main.ts             # Application entry point
│   └── app.css             # Global styles
├── scripts/                # Build and migration scripts
│   ├── setup-build.js      # Setup script
│   └── extract-songs.js    # Song extraction script
├── dist/                   # Build output (generated)
├── backups/                # Backup files (generated)
├── package.json            # Dependencies and scripts
├── vite.config.js          # Vite configuration
├── svelte.config.js        # Svelte configuration
├── tsconfig.json           # TypeScript configuration
├── .eslintrc.cjs           # ESLint configuration
└── .prettierrc             # Prettier configuration
```

## 🔧 Installation & Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Run Migration Script

```bash
npm run migrate
```

This will:
- Create necessary directories
- Backup existing files
- Extract songs from `music-stuff/songs.js`
- Set up the new project structure

### 3. Start Development Server

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## 📝 Available Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |
| `npm run lint` | Check code with ESLint |
| `npm run format` | Format code with Prettier |
| `npm run check` | Type check with Svelte Check |
| `npm run customize` | Run Python customization script |
| `npm run setup` | Set up build system directories |
| `npm run extract-songs` | Extract songs from existing file |
| `npm run migrate` | Complete migration setup |

## 🔄 Migration Process

### Phase 1: Setup (Complete)
- ✅ Create build system configuration
- ✅ Set up TypeScript and linting
- ✅ Create project structure
- ✅ Backup existing files

### Phase 2: Component Extraction (In Progress)
- 🔄 Extract components from `main.js`
- 🔄 Create individual Svelte components
- 🔄 Set up state management
- 🔄 Migrate song data

### Phase 3: Integration (Pending)
- ⏳ Integrate with existing customization script
- ⏳ Test all functionality
- ⏳ Optimize build output
- ⏳ Deploy new version

## 🎯 Benefits of New Build System

### Development Experience
- **Hot reload** - See changes instantly
- **TypeScript** - Better code quality and IDE support
- **Source maps** - Debug original code, not minified
- **ESLint/Prettier** - Consistent code style

### Performance
- **Code splitting** - Load only what's needed
- **Tree shaking** - Remove unused code
- **Optimized builds** - Smaller, faster bundles
- **Modern bundling** - Better caching and loading

### Maintainability
- **Modular code** - Easy to understand and modify
- **Type safety** - Catch errors early
- **Component-based** - Reusable and testable
- **Modern tooling** - Better debugging and profiling

## 🚨 Important Notes

### Backups
- All original files are backed up in `backups/` directory
- Original `main.js` is preserved
- Songs data is extracted but original remains

### Compatibility
- The new build system maintains the same functionality
- All game logic is preserved
- Customization script still works
- External dependencies (SoundCloud) unchanged

### Deployment
- Build output goes to `dist/` directory
- Can be deployed to any static hosting service
- Maintains compatibility with GitHub Pages

## 🆘 Troubleshooting

### Common Issues

1. **"Cannot find module" errors**
   - Run `npm install` to install dependencies
   - Check that all files are in correct locations

2. **TypeScript errors**
   - Run `npm run check` to see specific issues
   - Check import paths in components

3. **Build failures**
   - Check console for specific error messages
   - Ensure all required files exist
   - Verify Vite configuration

4. **Missing songs**
   - Run `npm run extract-songs` to regenerate songs file
   - Check `music-stuff/songs.js` exists

### Getting Help

1. Check the console for error messages
2. Verify all dependencies are installed
3. Ensure file paths are correct
4. Check TypeScript configuration

## 📚 Next Steps

After successful migration:

1. **Complete component extraction** - Break down `main.js` into components
2. **Add tests** - Unit and integration tests
3. **Optimize performance** - Bundle analysis and optimization
4. **Add features** - New game modes, analytics, etc.
5. **Deploy** - Set up CI/CD pipeline

## 🔗 Resources

- [Vite Documentation](https://vitejs.dev/)
- [Svelte Documentation](https://svelte.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [SvelteKit Documentation](https://kit.svelte.dev/)