import './bootstrap';
import './css/style.css';
import './charts/ChartjsConfig';

import Dashboard from './pages/Dashboard';
import { createRoot } from 'react-dom/client';
import { createInertiaApp } from '@inertiajs/react';
import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers';

const appName = window.document.getElementsByTagName('title')[0]?.innerText || 'Laravel';

createInertiaApp({
    title: (title) => `${title} - ${appName}`,
    resolve: (name) => resolvePageComponent(`./Pages/${name}.jsx`, import.meta.glob('./Pages/**/*.jsx')),
    setup({ el, App, props }) {
        const root = createRoot(el);

        root.render(<App {...props} />);
    },
    progress: {
        color: '#4B5563',
    },
});


// import React, { useEffect } from 'react';
// import {
//   Routes,
//   Route,
//   useLocation
// } from 'react-router-dom';
//
// import './css/style.css';
//
// import './charts/ChartjsConfig';
//
// // Import pages
// import Dashboard from './pages/Dashboard';
//
// function App() {
//
//   const location = useLocation();
//
//   useEffect(() => {
//     document.querySelector('html').style.scrollBehavior = 'auto'
//     window.scroll({ top: 0 })
//     document.querySelector('html').style.scrollBehavior = ''
//   }, [location.pathname]); // triggered on route change
//
//   return (
//     <>
//       <Routes>
//         <Route exact path="/" element={<Dashboard />} />
//       </Routes>
//     </>
//   );
// }
//
// export default App;
