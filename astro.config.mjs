import { defineConfig } from 'astro/config';

// Static build, hosted on Vercel at the portfolio subdomain (served from the root path).
export default defineConfig({
  site: 'https://portfolio.siddharthkrishna.com',
  output: 'static',
});
