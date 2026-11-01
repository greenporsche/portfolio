import { defineConfig } from 'astro/config';

// Static build. `site` and `base` are set when the hosting destination is decided (board S2.1).
export default defineConfig({
  output: 'static',
});
