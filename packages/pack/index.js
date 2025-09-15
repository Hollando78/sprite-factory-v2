// Minimal deterministic sorter/packer interface (stub)
function packFrames(frames) {
  // frames: [{id, w, h}] -> returns rects with x,y,w,h in a simple row
  const sorted = [...frames].sort((a,b) =>
    (a.h - b.h) || (a.w - b.w) || (String(a.id).localeCompare(String(b.id)))
  );
  let x = 0; const y = 0; const padding = 1; const out = [];
  sorted.forEach(f => {
    out.push({ id: f.id, x, y, w: f.w, h: f.h });
    x += f.w + padding;
  });
  return { width: x ? x - padding : 0, height: sorted[0]?.h || 0, rects: out };
}

module.exports = { packFrames };
