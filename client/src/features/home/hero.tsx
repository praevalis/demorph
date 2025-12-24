import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

import type { CtaData } from '@/types/ui';
import { Button } from '@/components/ui/button';
import { Section } from '@/components/ui/section';
import heroMobile from '@/assets/images/hero-mobile.png';
import heroDesktop from '@/assets/images/hero-desktop.png';

export default function Hero() {
	const { t } = useTranslation();
	const ctaData = t('hero.cta', { returnObjects: true }) as CtaData;

	return (
		<Section
			id='hero'
			className='flex items-end min-h-screen pb-10 md:pb-20 lg:pb-32'
		>
			<picture>
				<source media='(min-width: 768px)' srcSet={heroDesktop} />
				<img
					src={heroMobile}
					className='absolute inset-0 h-full w-full lg:object-cover -z-10'
				/>
			</picture>
			<div className='absolute inset-0 h-full w-full z-0 bg-gradient-to-r from-black/20 to-transparent'></div>
			<div className='flex flex-col max-w-lg gap-6 z-10'>
				<h3 className='font-primary font-semibold text-white text-3xl md:text-5xl leading-tight whitespace-pre-line'>
					{t('hero.headline')}
				</h3>
				<p className='font-secondary text-white/90 text-sm md:text-md md:max-w-md'>
					{t('hero.paragraph')}
				</p>
				<Button asChild>
					<Link to={ctaData.href}>{ctaData.label}</Link>
				</Button>
			</div>
		</Section>
	);
}
