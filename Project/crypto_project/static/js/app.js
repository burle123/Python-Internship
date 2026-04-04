const root = document.documentElement;
const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

function applyTheme(preference) {
    const resolved = preference === 'system' ? (mediaQuery.matches ? 'dark' : 'light') : preference;
    root.classList.toggle('dark', resolved === 'dark');
    root.dataset.theme = preference;
    localStorage.setItem('theme-preference', preference);
}

function cycleTheme() {
    const current = root.dataset.theme || 'system';
    const order = ['system', 'light', 'dark'];
    const next = order[(order.indexOf(current) + 1) % order.length];
    applyTheme(next);
}

document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
    button.addEventListener('click', cycleTheme);
});

mediaQuery.addEventListener('change', () => {
    if ((root.dataset.theme || 'system') === 'system') {
        applyTheme('system');
    }
});

const sidebar = document.getElementById('sidebar');
const backdrop = document.getElementById('sidebar-backdrop');

function openSidebar() {
    if (!sidebar || !backdrop) {
        return;
    }
    sidebar.classList.remove('-translate-x-full');
    backdrop.classList.remove('hidden');
}

function closeSidebar() {
    if (!sidebar || !backdrop) {
        return;
    }
    sidebar.classList.add('-translate-x-full');
    backdrop.classList.add('hidden');
}

document.querySelector('[data-sidebar-open]')?.addEventListener('click', openSidebar);
document.querySelector('[data-sidebar-close]')?.addEventListener('click', closeSidebar);
backdrop?.addEventListener('click', closeSidebar);
