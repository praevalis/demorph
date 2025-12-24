import { FaLock } from 'react-icons/fa6';
import { IoIosSearch } from 'react-icons/io';
import { useTranslation } from 'react-i18next';
import { FaWaveSquare, FaRegFilePdf } from 'react-icons/fa';

import type { AboutCardData } from '@/types/ui';
import { Section } from '@/components/ui/section';
import IconCard from '@/components/cards/icon-card';

export default function About() {
	const { t } = useTranslation();
	const cards = t('about.cards', { returnObjects: true }) as AboutCardData[];
	const aboutCards = Array.isArray(cards) ? cards : [];

	const iconMap: Record<string, React.ReactNode> = {
		scan: <IoIosSearch size={24} />,
		activity: <FaWaveSquare size={24} />,
		lock: <FaLock size={24} />,
		file: <FaRegFilePdf size={24} />,
	};

	return (
		<Section id='about' className='min-h-screen pb-20 bg-dark-gray'>
			<div className='flex flex-col gap-4 max-w-md font-secondary'>
				<h3 className='text-2xl md:text-4xl text-white'>
					{t('about.heading')}
				</h3>
				<p className='text-sm text-white/80'>{t('about.subheading')}</p>
			</div>
			<div className='grid grid-cols-1 md:grid-cols-3 gap-6 mt-10'>
				<div className='md:col-span-2 flex flex-col gap-6'>
					{aboutCards.slice(0, 3).map((card, idx) => (
						<IconCard
							key={idx}
							icon={iconMap[card.icon] || <FaWaveSquare size={24} />}
							layout={card.layout}
							heading={card.heading}
							text={card.text}
						/>
					))}
				</div>

				<div className='md:col-span-1'>
					{aboutCards.slice(3, 4).map((card, idx) => (
						<IconCard
							key={idx}
							icon={iconMap[card.icon] || <FaWaveSquare size={24} />}
							layout={card.layout}
							heading={card.heading}
							text={card.text}
							className='h-full md:justify-center'
						/>
					))}
				</div>
			</div>
		</Section>
	);
}
