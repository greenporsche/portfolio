import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { CATEGORIES } from './data/categories';

// One entry per project: src/content/projects/<slug>/index.md, with its media beside it.
// The same collection drives the home tiles and /projects/<slug>/ pages.
const projects = defineCollection({
  loader: glob({ base: './src/content/projects', pattern: '*/index.md', generateId: ({ entry }) => entry.split('/')[0] }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      category: z.enum(CATEGORIES.map((c) => c.name) as [string, ...string[]]),
      subgroup: z.string().optional(),
      order: z.number().default(100),
      summary: z.string(),
      lede: z.string().optional(),
      wide: z.boolean().default(false),
      cover: image().optional(),
      coverAlt: z.string().optional(),
      video: z.string().optional(),
      caption: z.string().optional(),
      stats: z.array(z.object({ value: z.string(), label: z.string() })).default([]),
      when: z.string().optional(),
      builtWith: z.string().optional(),
      links: z.array(z.object({ label: z.string(), href: z.string() })).default([]),
      // Release switch: only projects with published: true get a home tile and a page.
      published: z.boolean().default(false),
    }),
});

export const collections = { projects };
