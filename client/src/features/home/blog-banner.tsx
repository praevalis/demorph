import { useTranslation } from 'react-i18next';

import type { CtaData } from '@/types/ui';

import { Button } from '@/components/ui/button';
import { Section } from '@/components/ui/section';

export default function BlogBanner() {
	const { t } = useTranslation();
	const cta = t('blog.cta', { returnObjects: true }) as CtaData;

	return (
		<Section
			id='blog-banner'
			className='px-0 md:px-[5vw] lg:px-[5vw] bg-background'
		>
			<div className='flex flex-col md:flex-row md:justify-between md:items-center gap-6 w-full px-4 py-14 md:p-16 rounded-2xl bg-primary-light'>
				<div className='flex flex-col max-w-lg gap-2 text-white font-poppins'>
					<h3 className='text-2xl md:text-3xl font-semibold'>
						{t('blog.heading')}
					</h3>
					<p className='text-white/90'>{t('blog.subheading')}</p>
				</div>

				<Button asChild intent='white' size='large'>
					<a href={cta.href} title={cta.label} target='_blank' rel='noreferrer'>
						{cta.label}
					</a>
				</Button>
			</div>
		</Section>
	);
}
