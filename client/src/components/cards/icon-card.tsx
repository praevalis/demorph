import { Card, CardProps } from '@/components/ui/card';

import { cn } from '@/utils/cn';

export interface IconCardProps extends CardProps {
	icon: React.ReactNode;
	heading: string;
	text: string;
	layout?: 'vertical' | 'horizontal';
}

export default function IconCard({
	icon,
	heading,
	text,
	className,
	layout = 'vertical',
	...props
}: IconCardProps) {
	return (
		<Card
			className={cn(
				'flex flex-col gap-4',
				{ 'lg:flex-row lg:items-start': layout === 'horizontal' },
				className,
			)}
			{...props}
		>
			<div className='w-fit shrink-0 bg-primary text-white p-2 rounded-lg'>
				{icon}
			</div>
			<div className='flex flex-col gap-3'>
				<h3 className='font-semibold text-sm text-white leading-tight'>
					{heading}
				</h3>
				<p className='text-sm'>{text}</p>
			</div>
		</Card>
	);
}
