// Home page sections, in order (PO msg 1408 re-evaluation; proposal msg 1409).
export const CATEGORIES = [
  { name: 'Research', subgroups: [] },
  { name: 'Software I built', subgroups: [] },
  { name: 'Learning', subgroups: [] },
] as const;

export const slugify = (s: string) =>
  s.toLowerCase().replace(/\+/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
