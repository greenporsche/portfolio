// Category order and sub-groups, from kiku's write-up (room 78, #46584) plus Research (#46590).
export const CATEGORIES = [
  { name: 'Research', subgroups: [] },
  { name: 'Racing', subgroups: [] },
  { name: 'Utils', subgroups: ['Personal productivity', 'More tools'] },
  { name: 'Catalog + Consume', subgroups: ['Music', 'Movies', 'CourseTube'] },
  {
    name: 'MetaMatx Learning',
    subgroups: ['Codecrafters style', 'AoPS / Math Academy style', 'Articulate & Sana style', 'More'],
  },
] as const;

export const slugify = (s: string) =>
  s.toLowerCase().replace(/\+/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
