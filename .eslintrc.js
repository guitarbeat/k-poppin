module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: ['airbnb-base', 'prettier'],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  rules: {
    'no-console': 'off',
    'import/prefer-default-export': 'off',
    'no-restricted-syntax': 'off',
  },
  overrides: [
    {
      files: ['data/*.js', 'bg/data/*.js'],
      parserOptions: {
        sourceType: 'script',
      },
      globals: {
        songs: 'writable',
      },
      rules: {
        'no-var': 'off',
        'prefer-const': 'off',
        'no-unused-vars': 'off',
      },
    },
  ],
};
