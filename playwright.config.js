const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  webServer: {
    command: 'echo "Using Flask, not Playwright server"',
    port: 3000,
  },
});
