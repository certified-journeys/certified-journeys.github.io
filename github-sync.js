'use strict';
const GHSync = (() => {
  const CREDS_KEY = 'cj_github_creds';
  let creds = null;
  let fileSHAs = {};
  let saveTimers = {};

  function loadCreds() {
    try { const s = localStorage.getItem(CREDS_KEY); if (s) creds = JSON.parse(s); } catch(e) {}
  }

  function saveCreds(c) {
    creds = c;
    try {
      if (c) localStorage.setItem(CREDS_KEY, JSON.stringify(c));
      else localStorage.removeItem(CREDS_KEY);
    } catch(e) {}
  }

  function getCreds() { return creds; }

  function isConnected() {
    return !!(creds && creds.pat && creds.owner && creds.repo);
  }

  function hdrs() {
    return {
      'Authorization': `Bearer ${creds.pat}`,
      'Accept': 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json',
    };
  }

  function apiUrl(courseId) {
    return `https://api.github.com/repos/${creds.owner}/${creds.repo}/contents/courses/${courseId}/progress.json`;
  }

  async function fetchState(courseId) {
    if (!isConnected()) return null;
    try {
      const branch = creds.branch || 'main';
      const res = await fetch(`${apiUrl(courseId)}?ref=${branch}`, { headers: hdrs() });
      if (res.status === 404) return null;
      if (!res.ok) return null;
      const data = await res.json();
      fileSHAs[courseId] = data.sha;
      const raw = data.content.replace(/\n/g, '');
      return JSON.parse(new TextDecoder().decode(Uint8Array.from(atob(raw), c => c.charCodeAt(0))));
    } catch(e) { console.warn('GHSync.fetchState:', e); return null; }
  }

  async function pushState(courseId, state, onDone) {
    if (!isConnected()) return false;
    try {
      const branch = creds.branch || 'main';
      const encoded = new TextEncoder().encode(JSON.stringify(state, null, 2));
      const content = btoa(String.fromCharCode(...encoded));
      const body = { message: `chore: update ${courseId} progress`, content, branch };
      if (fileSHAs[courseId]) body.sha = fileSHAs[courseId];
      const res = await fetch(apiUrl(courseId), {
        method: 'PUT', headers: hdrs(), body: JSON.stringify(body),
      });
      if (!res.ok) { if (onDone) onDone(false); return false; }
      const data = await res.json();
      fileSHAs[courseId] = data.content.sha;
      if (onDone) onDone(true);
      return true;
    } catch(e) { console.warn('GHSync.pushState:', e); if (onDone) onDone(false); return false; }
  }

  function saveDebounced(courseId, state, delay, onStart, onDone) {
    clearTimeout(saveTimers[courseId]);
    if (onStart) onStart();
    saveTimers[courseId] = setTimeout(() => pushState(courseId, state, onDone), delay || 2500);
  }

  async function testConnection() {
    if (!isConnected()) return { ok: false, msg: 'No credentials set.' };
    try {
      const res = await fetch(
        `https://api.github.com/repos/${creds.owner}/${creds.repo}`,
        { headers: hdrs() }
      );
      if (res.status === 401) return { ok: false, msg: 'Invalid token.' };
      if (res.status === 404) return { ok: false, msg: 'Repo not found — check owner/repo.' };
      if (!res.ok) return { ok: false, msg: `GitHub error ${res.status}.` };
      const d = await res.json();
      return { ok: true, msg: `Connected · ${d.full_name}` };
    } catch(e) { return { ok: false, msg: 'Network error.' }; }
  }

  function exportConfig() {
    if (!creds) return '';
    return btoa(JSON.stringify(creds));
  }

  function importConfig(str) {
    try {
      const c = JSON.parse(atob(str.trim()));
      if (!c || !c.pat || !c.owner || !c.repo) return null;
      return c;
    } catch { return null; }
  }

  loadCreds();
  return { isConnected, saveCreds, getCreds, fetchState, pushState, saveDebounced, testConnection, exportConfig, importConfig };
})();
