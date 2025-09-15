// Minimal JSON Schema validator for the subset we use (draft-07 features used here)
// Supports: type, required, properties, additionalProperties (boolean), enum, items
// Not supported: allOf/anyOf/oneOf/$ref/format/pattern/min/max, etc.

function typeOf(val) {
  if (Array.isArray(val)) return 'array';
  if (val === null) return 'null';
  return typeof val; // 'object','string','number','boolean'
}

function matchesType(val, expected) {
  const t = typeOf(val);
  if (expected === 'integer') return t === 'number' && Number.isInteger(val);
  if (expected === 'number') return t === 'number' && Number.isFinite(val);
  return t === expected;
}

function validate(obj, schema, path = '') {
  const errors = [];
  const here = path || '';

  // type
  if (schema.type) {
    const expected = Array.isArray(schema.type) ? schema.type : [schema.type];
    const ok = expected.some((et) => matchesType(obj, et));
    if (!ok) {
      errors.push(`${here || '<root>'}: expected type ${expected.join('|')}, got ${typeOf(obj)}`);
      return errors; // further checks would be noisy
    }
  }

  // enum
  if (schema.enum && !schema.enum.includes(obj)) {
    errors.push(`${here || '<root>'}: value ${JSON.stringify(obj)} not in enum`);
  }

  if (schema.type === 'object') {
    const props = schema.properties || {};
    const req = schema.required || [];
    // required
    req.forEach((k) => {
      if (!(k in obj)) errors.push(`${here || '<root>'}: missing required property '${k}'`);
    });
    // properties
    for (const [k, v] of Object.entries(obj || {})) {
      if (k in props) {
        errors.push(...validate(v, props[k], here ? `${here}.${k}` : k));
      } else {
        if (schema.additionalProperties === false) {
          if (!String(k).startsWith('$')) { // allow $schema/$id metadata
            errors.push(`${here || '<root>'}: additional property not allowed: '${k}'`);
          }
        }
      }
    }
  }

  if (schema.type === 'array') {
    const items = schema.items;
    if (items) {
      (obj || []).forEach((it, idx) => {
        errors.push(...validate(it, items, `${here}[${idx}]`));
      });
    }
  }

  return errors;
}

module.exports = { validate };
