import { cn } from '@/utils/cn';
import Navbar from '@/components/navigation/navbar/navbar';
import Footer from '@/components/navigation/footer/footer';

export interface PageProps {
	children: React.ReactNode;
	className?: string;
}

export default function DefaultLayout({ children, className }: PageProps) {
	return (
		<div
			className={cn(
				'flex flex-col justify-between items-center min-h-screen',
				className,
			)}
		>
			<Navbar />

			{children}

			<Footer />
		</div>
	);
}
