import Home from '@/pages/home';
import Error from '@/pages/error';

export const routes = [
	{
		path: '/',
		element: <Home />,
		errorElement: <Error />,
	},
];
