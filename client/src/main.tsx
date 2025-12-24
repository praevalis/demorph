import { Suspense, StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';

import '@fontsource/poppins/400.css';
import '@fontsource/montserrat/600.css';
import '@fontsource/montserrat/700.css';

import '@/lib/i18n';
import '@/index.css';
import { routes } from '@/lib/app-config';

function App() {
	return <RouterProvider router={createBrowserRouter(routes)} />;
}

createRoot(document.getElementById('root')!).render(
	<StrictMode>
		<Suspense fallback=''>
			<App />
		</Suspense>
	</StrictMode>,
);
